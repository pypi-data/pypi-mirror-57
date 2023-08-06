#!%PYTHON_HOME%\python.exe
# coding: utf-8
# version: python37

import time, datetime
from functools import reduce
import scipy.optimize as spopt
import numpy as np

from yutils.tools import istype
from yutils.exceptions import InputError, CodeMistake
from yutils.tools.numpy_tools import r2c, is_matrix, TWO_D_ARRAY_INTS_FLOATS_TYPE, TWO_D_ARRAY_TYPE
from yutils.tools.itertools import disperse_length
from yutils.ml.regression import Regression


GOLDEN_RATIO = (1 + 5 ** 0.5) / 2


class NeuralNetwork(Regression):
    DEFAULT_ITERATIONS = 50
    DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT = 3

    _REACHED_MAX_ITERATION_MESSAGE = 'Maximum number of iterations has been exceeded.'

    _INPUT_TYPES = dict(original_training_data=TWO_D_ARRAY_INTS_FLOATS_TYPE,
                        training_results=TWO_D_ARRAY_TYPE,
                        nn_architecture=(tuple, int),
                        num_hidden_layers=int,
                        iterations=int,
                        normalization=bool,
                        add_polynomial_features=bool,
                        additional_features_max_exponent=int,
                        regularization=bool,
                        verbose=bool,
                        use_optimized_gradient_descent=bool,
                        gradient_checking=bool)
    _INPUT_DEFAULTS = dict(nn_architecture=(),
                           num_hidden_layers=1,
                           iterations=DEFAULT_ITERATIONS,
                           normalization=True,
                           add_polynomial_features=False,
                           additional_features_max_exponent=DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT,
                           regularization=True,
                           verbose=True,
                           use_optimized_gradient_descent=True,
                           gradient_checking=False)

    def __init__(self, training_data, training_results, **kwargs):
        """
        Creates a regression object, for use in linearization/classification problems.

        :param training_data: Data to train algorithm to - columns are features and rows are training examples
        :type training_data: 2-D numpy array
        :param training_results: Results of each training algorithm
        :type training_results: numpy array

        :param kwargs: Additional keyword arguments


            Available kwargs:

        :param nn_architecture: The amount of nodes/units in every layer of the Neural Network
                                (including the input layer, output layer, and all hidden layers.
        :default nn_architecture: Will create a (num_hidden_layers + 2)-layer Neural Network:
                                  default: (input_layer_size, hidden_layer_size, output_layer_size)
                                        input_layer_size: length of training_data row
                                        hidden_layer_size: int(input_layer_size * golden_ratio)
                                        output_layer_size: amount of output classes defined in training_results
                                  raising the number of num_hidden_layers creates more hidden_layers of the same size.
        :type nn_architecture: tuple of ints

        :param num_hidden_layers: To be used instead of nn_architecture - to easily create a Neural Network
                                    with more than one hidden layer
                                  The amount of units in each layer will be the same, and defined as:
                                        hidden_layer_size: int(input_layer_size * golden_ratio)
        :default num_hidden_layers: 1
        :type num_hidden_layers: int

        :param iterations: Number of iterations to descend
        :default iterations: cls.DEFAULT_ITERATIONS
        :type iterations: int

        :param normalization: If to normalize the training data (turn them ~ -1 - 1 or ~ -0.5 - 0.5)
                                to make the regression faster and more exact
        :default normalization: True
        :type normalization: bool

        :param add_polynomial_features: If to add polynomial variations of the current training data features,
                                        in order to find a more exact graphical match to the training data
        :default add_polynomial_features: False
        :type add_polynomial_features: bool

        :param additional_features_max_exponent: Highest exponent of new ponynomial features to add
        :default additional_features_max_exponent: cls.DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT
        :type additional_features_max_exponent: int

        :param regularization: If to regularize the gradient descent, in order to prevent overfitting the training data
        :default regularization: True
        :type regularization: bool

        :param gradient_checking: If to check the gradient function against a numerical gradient, to debug
        :default gradient_checking: False
        :type gradient_checking: bool

        :param verbose: If to print messages
        :default verbose: True
        :type verbose: bool
        """
        super().__init__(training_data, training_results, **kwargs)
        self.num_input_units = self._get_num_input_units()
        self.output_classes, self.num_output_classes = self._get_num_output_classes()
        self.original_training_results, self.training_results = self.training_results, \
                                                                self.output_classes == self.training_results
        self._check_inputs()
        self._create_nn_architecture()
        
        self._layer_outputs_a = [None] * len(self.nn_architecture)
        self._layer_inputs_z = [None] * len(self.nn_architecture)

        self._cur_iteration = 0
    
    def _check_inputs(self):
        if self.nn_architecture:
            if not self.nn_architecture[0] == self.num_input_units:
                raise InputError("Input 'nn_architecture' first item should be the length of training_data row")

            if not self.nn_architecture[-1] == self.num_output_classes:
                raise InputError("Input 'nn_architecture' last item should be the number of training_results labels")

    def _get_num_input_units(self):
        original_num_input_units = self.original_training_data.shape[1]
        if self.add_polynomial_features:
            return disperse_length(self.additional_features_max_exponent, original_num_input_units)
        return original_num_input_units

    def _get_num_output_classes(self):
        classes = np.array(list(set(self.training_results[:, 0])))
        classes.sort()
        num = len(classes)
        if num == 2:
            return [max(classes)], 1
        return classes, num

    def _create_nn_architecture(self):
        if not self.nn_architecture:
            self.nn_architecture = (self.num_input_units,) + \
                                   (int(self.num_input_units * GOLDEN_RATIO),) * self.num_hidden_layers + \
                                   (self.num_output_classes,)

    def _initialize_theta(self):
        self.theta = [self._rand_initialize_weights(from_layer, self.nn_architecture[from_layer_index + 1])
                      for from_layer_index, from_layer in enumerate(self.nn_architecture[:-1])]

    @staticmethod
    def _rand_initialize_weights(layer_size_in, layer_size_out):
        """
        Returns a random initialization of weights in the range of -epsion to +epsilon
        Epsilon will be sqrt(6) / sqrt(layer_size_in + layer_size_out)

        :param layer_size_in: number of units in the layer adjacent to Theta(l) (before it)
        :type layer_size_in: int
        :param layer_size_out: number of units in the layer adjacent to Theta(l) (after it)
        :type layer_size_out: int

        :return: Random weights (array of size layer_size_in by (layer_size_out + 1)
        :rtype: numpy.ndarray
        """
        epsilon_init = round((6 ** 0.5) / ((layer_size_in + layer_size_out) ** 0.5), 4)
        return np.random.random((layer_size_out, layer_size_in + 1)) * 2 * epsilon_init - epsilon_init

    def _hypothesis(self, X, theta, bias_unit_already_added=True):
        if not bias_unit_already_added:
            X = self._add_ones(X)

        if is_matrix(X):
            return self._hypothesis_multiple(X, theta)

        if len(X.shape) == 1:
            X = r2c(X)
        return self._hypothesis_single(X, theta)

    def _hypothesis_single(self, X, theta):
        return self._hypothesis_generic(r2c(X), theta, lambda a, thet: thet @ a)

    def _hypothesis_multiple(self, X, theta):
        return self._hypothesis_generic(X, theta, lambda a, thet: a @ thet.T)

    def _hypothesis_generic(self, X, theta, matrix_mult_func):
        self._layer_outputs_a[0] = X
        for layer_index in range(len(self.nn_architecture) - 1):
            if layer_index != 0:
                self._layer_outputs_a[layer_index] = self._add_ones(self._layer_outputs_a[layer_index])
            self._layer_inputs_z[layer_index + 1] = matrix_mult_func(self._layer_outputs_a[layer_index],
                                                                     theta[layer_index])
            self._layer_outputs_a[layer_index + 1] = self._sigmoid(self._layer_inputs_z[layer_index + 1])
        return self._layer_outputs_a[-1]

    @staticmethod
    def _sigmoid(z):
        return 1 / (1 + np.exp(-z))

    @classmethod
    def _sigmoid_gradient(cls, z):
        return cls._sigmoid(z) * (1 - cls._sigmoid(z))

    def compute_cost(self, X, y, theta, regularization=True, architecture=None):
        """
        Should return the cost of a certain theta prediction

        :param X: training info (1-column-padded)
        :type X: 2-D array
        :param y: training results (answers)
        :type y: column array
        :param theta: list of weights for each layer of network (current theta)
        :type theta: list of 2-D arrays, or 1-D array that function will unravel
        :param regularization: if cost should use a regularization term to regularize thetas (except for theta zero)
        :type regularization: bool
        :param architecture: The number of units in each layer of your Neural Network architecture
                                Left blank this will default to self.nn_architecture
        :type architecture: tuple of ints

        :return: the cost of the prediction
        :rtype: float
        """
        architecture = self.nn_architecture if architecture is None else architecture
        theta = theta if istype(theta, (list, np.ndarray)) else self._unroll(theta, architecture=architecture)
        m = y.shape[0]

        y_true_computation = (-1 * y) * np.log(self._hypothesis(X, theta))
        y_false_computation = (1 - y) * np.log(1 - self._hypothesis(X, theta))

        if regularization:
            regularization_term = (self.REGULARIZATION_LAMBDA / (2 * m)) * sum(sum(sum(t[:, 1:] ** 2)) for t in theta)
        else:
            regularization_term = 0

        j_cost_no_reg = (1 / m) * sum(sum(y_true_computation - y_false_computation))
        j_cost = j_cost_no_reg + regularization_term
        return j_cost

    def get_gradient(self, X, y, theta, regularization=True, architecture=None):
        """
        This method should change self.theta.

        :param X: training info (1-column-padded)
        :type X: 2-D array
        :param y: training results (answers)
        :type y: 2-D array
        :param theta: list of weights for each layer of network (current theta)
        :type theta: list of 2-D arrays, or 1-D array that function will unravel
        :param regularization: if gradient should use a regularization term to regularize thetas (except for theta zero)
        :type regularization: bool
        :param architecture: The number of units in each layer of your Neural Network architecture
                                Left blank this will default to self.nn_architecture
        :type architecture: tuple of ints

        :return: gradient for all thetas - an array with a length of all thetas - rolled out to single 1-D array
        :rtype: list of numpy.ndarrays
        """
        architecture = self.nn_architecture if architecture is None else architecture
        theta = theta if istype(theta, (list, np.ndarray)) else self._unroll(theta, architecture=architecture)
        m = y.shape[0]
        final_delta = [np.zeros(shape=t.shape) for t in theta]
        gradient = [np.zeros(shape=t.shape) for t in theta]
        
        for i in range(m):
            hypothesis = self._hypothesis(X[i], theta)
            delta = [None] * len(self.nn_architecture)
            delta[-1] = hypothesis - r2c(y[i])
            for l in range(len(self.nn_architecture) - 2, 0, -1):
                delta[l] = (theta[l][:, 1:].T @ delta[l + 1]) * self._sigmoid_gradient(self._layer_inputs_z[l])
            for l in range(len(final_delta)):
                final_delta[l] = final_delta[l] + (delta[l + 1] * self._layer_outputs_a[l].T)

        for l in range(len(gradient)):
            gradient[l] = (1 / m) * final_delta[l]

        if regularization:
            for l in range(len(gradient)):
                gradient[l][:, 1:] = gradient[l][:, 1:] + ((self.REGULARIZATION_LAMBDA / m) * theta[l][:, 1:])

        return gradient

    def _unroll(self, array, architecture=None):
        architecture = self.nn_architecture if architecture is None else architecture
        output = []
        index = 0
        for l in range(len(architecture) - 1):
            in_layer, out_layer = architecture[l], architecture[l + 1]
            length = (in_layer + 1) * out_layer
            output.append(np.reshape(array[index:index + length], (out_layer, in_layer + 1)))
            index += length
        return output

    @staticmethod
    def _roll(lst_of_arrays):
        return reduce(np.append, lst_of_arrays)

    def _theta_minimizer_callback_func(self, cur_theta):
        theta = self._unroll(cur_theta)
        prediction_percentage = self.check_prediction(theta)
        cost = self.compute_cost(self.training_data, self.training_results, theta, self.regularization)
        self._cur_iteration += 1
        if self.verbose:
            print('Iteration:', self._cur_iteration,
                  ' ~ Prediction Accuracy:', round(prediction_percentage, 3),
                  ' ~ Cost Function Value:', round(cost, 6),
                  ' ~ Time:', datetime.datetime.fromtimestamp(time.time()))

    def _run_gradient_descent_optimized(self):
        def _get_cost_and_gradient(theta):
            return self.compute_cost(self.training_data, self.training_results, theta, self.regularization), \
                   self._roll(self.get_gradient(self.training_data, self.training_results, theta, self.regularization))

        result = spopt.minimize(_get_cost_and_gradient,
                                self._roll(self.theta),
                                jac=True,
                                callback=self._theta_minimizer_callback_func,
                                options=dict(maxiter=self.iterations, disp=self.verbose))
        #
        # if self.verbose:
        #     print()  # To place an empty line after printing of iterations in callback function

        if not result.success:
            if result.message != self._REACHED_MAX_ITERATION_MESSAGE:
                raise Exception(result.message)

        self.theta = self._unroll(result.x)

    def predict(self, input_data, theta=None):
        predictions = super().predict(input_data, theta)
        if is_matrix(predictions):
            indexes = np.argmax(predictions, axis=1)
        else:
            indexes = np.argmax(predictions)
        return self.output_classes[indexes]

    def check_prediction(self, theta=None):
        predictions = self.predict(self.original_training_data, theta)
        return np.mean(predictions == self.original_training_results[:, 0]) * 100
