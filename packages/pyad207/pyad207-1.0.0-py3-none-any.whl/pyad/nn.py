import pyad.reverse_mode as rev
import numpy as np
import time


def linear_activation(x):
    return x


def softmax_activation(x):
    z = rev.exp(x)
    return z / z.sum(axis=0)


def log_softmax_activation(x):
    return x - rev.log(rev.exp(x).sum(axis=0))


def tanh_activation(x):
    return rev.tanh(x)


def logistic_activation(x):
    return rev.logistic(x)


def relu_activation(x):
    return x * (x >= 0)


def mse_loss(y_pred, y_true):
    return ((y_pred - y_true) ** 2).mean()


def rmse_loss(y_pred, y_true):
    return rev.sqrt(mse_loss(y_pred, y_true))


def nll_loss(y_log_probs, y_true):
    true_idx = y_true.value if isinstance(y_true, rev.Tensor) else y_true
    true_idx = np.array(true_idx, dtype=int)
    return -y_log_probs[true_idx, np.arange(len(true_idx))].mean()


def cross_entropy_loss(y_logits, y_true):
    y_log_probs = log_softmax_activation(y_logits)
    return nll_loss(y_log_probs, y_true)


class NeuralNet:
    """
    A complete neural network class which contains functions for building the
    network, training, evaluation, and prediction.
    """
    activation_funcs = {
        'linear': linear_activation,
        'softmax': softmax_activation,
        'log_softmax': log_softmax_activation,
        'tanh': tanh_activation,
        'logistic': logistic_activation,
        'relu': relu_activation
    }

    loss_functions = {
        'mse': mse_loss,
        'rmse': rmse_loss,
        'nll': nll_loss,
        'cross_entropy': cross_entropy_loss,
    }

    def __init__(self, loss_fn='mse'):
        """
        Initializes an empty NeuralNet with a particular loss function. The
        loss function specified determines what kind of task this neural
        network will be performing.

            `nll` and `cross_entropy` imply classification
            `mse` and `rmse` imply regression

        Parameters
        ----------
        loss_fn: string
            Which loss function should be used. The options are given by
            NeuralNet.loss_functions
        """
        if loss_fn not in self.loss_functions:
            raise ValueError(f'Invalid loss function: {loss_fn}')

        self.layers = []
        self.loss_fn = NeuralNet.loss_functions[loss_fn]
        self.loss_fn_name = loss_fn

    def add_layer(self, in_size, out_size, activation='linear'):
        """
        Adds a layer to the network. The size of the next layer must be
        compatible with the size of the previous layer

        Parameters
        ----------
        in_size: int
            The number of nodes in the previous layer of the network

        out_size: int
            The number of nodes in the next layer of the network

        activation: string
            The name of the activation function which should be used for this
            layer. The options are given by `NeuralNet.activation_funcs`
        """
        if self.layers:
            if self.layers[-1]['out_size'] != in_size:
                raise ValueError('Input size of next layer must match '
                                 'output size of the previous layer.')

        if activation not in self.activation_funcs:
            raise ValueError(f'Invalidation activation function: {activation}')

        # Xavier initialization of weights
        xavier_init_mult = np.sqrt(2 / (out_size * in_size))
        weight_init = np.random.randn(out_size, in_size) * xavier_init_mult
        bias_init = np.zeros((out_size, 1))

        self.layers.append({
            'in_size': in_size,
            'out_size': out_size,
            'weights': rev.Tensor(weight_init),
            'bias': rev.Tensor(bias_init),
            'activation': self.activation_funcs[activation],
        })

    def evaluate(self, x):
        """
        Evaluates the neural network on a given input.

        Parameters
        ----------
        x: np.array
            The input to the network

        Returns
        -------
        rev.Tensor
            The result of running the input through the network
        """
        result = rev.Tensor(x.T)
        for l in self.layers:
            result = l['weights'] @ result + l['bias']
            result = l['activation'](result)
        return result

    def predict(self, x):
        """
        Similar to evaluate(). However, if the loss function is intended
        for a classification task, e.g. nll or cross_entropy, then the
        result will be the actual predicted classes.


        Parameters
        ----------
        x: np.array
            The input to the network

        Returns
        -------
        np.array
            The result of running the input through the network
        """
        res = self.evaluate(x)
        if self.loss_fn_name in ('nll', 'cross_entropy'):
            return res.value.argmax(axis=0)
        return res.value

    def accuracy(self, x, y_true):
        """
        Computes the accuracy of the predictions. This only works for
        classificiation loss functions, i.e. nll or cross_entropy.

        Parameters
        ----------
        x: np.array
            The inputs to the network

        y: np.array
            The true classes

        Returns
        -------
        float
            The accuracy as a float in [0, 1.0]
        """
        if self.loss_fn_name not in ('nll', 'cross_entropy'):
            raise ValueError(f'Cannot compute accuracy for loss_fn {self.loss_fn_name}')

        preds = self.predict(x)
        return (preds == y_true).mean()

    def score(self, x, y):
        """
        Evaluates the loss function on the input.

        Parameters
        ----------
        x: np.array
            The inputs to the network

        y: np.array
            The true values or classes for the given inputs


        Returns
        -------
        float
            The loss
        """
        return self.loss_fn(self.evaluate(x), y)

    def _reset_weight_grads(self):
        """
        Internal helper function for reseting the gradients of all of the
        weights in network
        """
        for l in self.layers:
            l['weights'].reset_grad()
            l['bias'].reset_grad()

    def _update_weights(self, learning_rate, batch_size):
        """
        Internal helper function for performing gradient descent using
        stochastic gradient descent. The gradients are normalized by the
        size of the batch
        """
        learning_rate = learning_rate / batch_size
        for l in self.layers:
            l['weights'] = l['weights'] - l['weights'].grad * learning_rate
            l['bias'] = l['bias'] - l['bias'].grad * learning_rate
        self._reset_weight_grads()

    def train(self, x_train, y_train, x_val, y_val, *,
              batch_size=20, epochs=20, learning_rate=1e-3, verbose=True):
        """
        Iterates through the training data multiple times, and computes the loss
        of the neural network. The weights are then updated by taking their
        gradient w.r.t. the loss using SGD. Periodically logs some output
        about the training progress.

        Parameters
        ----------
        x_train: np.array
            The data which should be used to train the network

        y_train: np.array
            The associated y values for the training data

        x_val: np.array
            The data which should be used to log validation output

        y_val: np.array
            The associated y values for the validation data

        batch_size: int
            How many data samples to use in each SGD batch

        epochs: int
            How many training loops through the data should be executed

        learning_rate: float
            Controls the speed of the SGD update

        verbose: bool
            Whether or not logs should be outputted
        """
        self._reset_weight_grads()

        for epoch in range(epochs):
            try:
                start_time = time.time()
                total_train_loss = 0
                tot_train_correct = 0

                for batch in range(0, len(x_train), batch_size):
                    x_batch = x_train[batch:batch+batch_size]
                    y_batch = y_train[batch:batch+batch_size]
                    y_batch_pred = self.evaluate(x_batch)

                    loss = self.loss_fn(y_batch_pred, y_batch)
                    loss.backward()
                    self._update_weights(learning_rate, len(x_batch))

                    total_train_loss += loss.value * len(x_batch)

                    if self.loss_fn_name in ('nll', 'cross_entropy'):
                        tot_train_correct += (y_batch_pred.value.argmax(0) == y_batch).sum()

                with rev.no_grad():
                    val_preds = self.evaluate(x_val)
                    avg_val_loss = self.loss_fn(val_preds, y_val).value

                if verbose:
                    # Logging some information
                    header = f'Epoch {epoch + 1}'
                    print(header + '\n' + '=' * len(header))
                    print(f'Duration: {time.time() - start_time:.3f} sec')
                    print(f'Avg train loss: {total_train_loss / len(x_train):.3g}')
                    print(f'Avg validation loss: {avg_val_loss:.3g}')

                    if self.loss_fn_name in ('nll', 'cross_entropy'):
                        train_acc = tot_train_correct / len(x_train)
                        val_acc = (val_preds.value.argmax(axis=0) == y_val).mean()
                        print(f'Avg train acc: {train_acc:.3g}')
                        print(f'Avg validation acc: {val_acc:.3g}')

                    print()
            except KeyboardInterrupt:
                print(f'Stopping training after {epoch} epochs...')
                break
