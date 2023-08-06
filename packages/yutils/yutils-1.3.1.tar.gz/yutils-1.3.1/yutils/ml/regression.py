#!%PYTHON_HOME%\python.exe
# coding: utf-8
# version: python37

import numpy as np
from abc import ABCMeta, abstractmethod
import scipy.optimize as spopt

from yutils.exceptions import InputError
from yutils.tools.numpy_tools import to_array, r2c, is_matrix, TWO_D_ARRAY_INTS_FLOATS_TYPE
from yutils.ml.ml_base import MLObject
from yutils.ml.features import FeatureNormalizer, AddPolynomialFeatures
from yutils.ml.gradient_checking import GradientChecker


class Regression(MLObject):
    __metaclass__ = ABCMeta

    DEFAULT_ITERATIONS = 3000
    DEFAULT_LEARNING_RATE = 0.01    # TODO: check for best learning rate - look at graphs and see which is best
    DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT = 6
    REGULARIZATION_LAMBDA = 1

    _INPUT_TYPES = dict(original_training_data=TWO_D_ARRAY_INTS_FLOATS_TYPE,
                        training_results=TWO_D_ARRAY_INTS_FLOATS_TYPE,
                        learning_rate=float,
                        iterations=int,
                        normalization=bool,
                        add_polynomial_features=bool,
                        additional_features_max_exponent=int,
                        regularization=bool,
                        verbose=bool,
                        assess_for_warning=bool,
                        use_optimized_gradient_descent=bool,
                        gradient_checking=bool)

    _INPUT_DEFAULTS = dict(learning_rate=DEFAULT_LEARNING_RATE,
                           iterations=DEFAULT_ITERATIONS,
                           normalization=True,
                           add_polynomial_features=True,
                           additional_features_max_exponent=DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT,
                           regularization=True,
                           verbose=True,
                           assess_for_warning=True,
                           use_optimized_gradient_descent=True,
                           gradient_checking=False)

    _PREDICT_INPUT_LENGTH_ERROR = "Function predict() input_data should be of same length of training data examples:\n" \
                                  "{} != {}"

    def __init__(self, training_data, training_results, **kwargs):
        """
        Creates a regression object, for use in linearization/classification problems.

        :param training_data: Data to train algorithm to - columns are features and rows are training examples
        :type training_data: 2-D numpy array
        :param training_results: Results of each training algorithm
        :type training_results: numpy array

        :param kwargs: Additional keyword arguments


            Available kwargs:

        :param learning_rate: Alpha Coefficient for managing descent speed
        :default learning_rate: cls.DEFAULT_LEARNING_RATE
        :type learning_rate: float

        :param iterations: Number of iterations to descend
        :default iterations: cls.DEFAULT_ITERATIONS
        :type iterations: int

        :param normalization: If to normalize the training data (turn them ~ -1 - 1 or ~ -0.5 - 0.5)
                                to make the regression faster and more exact
        :default normalization: True
        :type normalization: bool

        :param add_polynomial_features: If to add polynomial variations of the current training data features,
                                        in order to find a more exact graphical match to the training data
        :default add_polynomial_features: True
        :type add_polynomial_features: bool

        :param additional_features_max_exponent: Highest exponent of new ponynomial features to add
        :default additional_features_max_exponent: cls.DEFAULT_ADDITIONAL_FEATURES_MAX_EXPONENT
        :type additional_features_max_exponent: int

        :param regularization: If to regularize the gradient descent, in order to prevent overfitting the training data
        :default regularization: True
        :type regularization: bool

        :param assess_for_warning: If to raise warnings if they emerge
        :default assess_for_warning: True
        :type assess_for_warning: bool

        :param use_optimized_gradient_descent: If you would rather use a more advanced optimizer (scipy.optimize.minimize)
                                                to run gradient descent, than a self-created implementation here
        :default use_optimized_gradient_descent: True
        :type use_optimized_gradient_descent: bool

        :param gradient_checking: If to check the gradient function against a numerical gradient, to debug
        :default gradient_checking: False
        :type gradient_checking: bool

        :param verbose: If to print messages
        :default verbose: True
        :type verbose: bool
        """
        super().__init__(original_training_data=to_array(training_data),
                         training_results=r2c(to_array(training_results)),
                         **kwargs)
        self.m = self.training_results.size

        self.training_data = self.original_training_data
        self.training_results = self.training_results  # This is just to syntactic, to remove errors in IDE highlights

        # Initialize Variables
        self.j_cost_history = np.zeros(shape=(self.iterations, 1))
        self.theta = None
        self._normalizer = None
        self._feature_adder = None
        self._exponents_of_original_features_in_order = None

        self._assess_for_warnings()

    def run(self):
        self._initialize_all_data()
        self._gradient_checking()
        
        if self.use_optimized_gradient_descent:
            self._run_gradient_descent_optimized()
        else:
            self._run_gradient_descent_self_implementation()

    def _run_gradient_descent_optimized(self):
        def _get_cost_and_gradient(theta):
            return self.compute_cost(self.training_data, self.training_results, theta, self.regularization), \
                   self.get_gradient(self.training_data, self.training_results, theta, self.regularization)[:, 0]

        result = spopt.minimize(_get_cost_and_gradient,
                                self.theta,
                                jac=True,
                                options=dict(maxiter=self.iterations, disp=self.verbose))

        if not result.success:
            raise Exception(result.message)

        self.theta = result.x

    def _run_gradient_descent_self_implementation(self):
        for i in range(0, self.iterations):
            gradient = self.get_gradient(self.training_data, self.training_results, self.theta, self.regularization)
            self._gradient_descent_single_step(gradient)
            self.j_cost_history[i] = self.compute_cost(self.training_data, self.training_results,
                                                       self.theta, self.regularization)

    def _initialize_all_data(self):
        self._create_all_data_features()
        self._normalize_features()
        self._initialize_theta()
    
    def _initialize_theta(self):
        self.theta = np.zeros(shape=(self.training_data.shape[1], 1))

    def _create_all_data_features(self):
        if self.add_polynomial_features:
            self._feature_adder = AddPolynomialFeatures(self.training_data, self.additional_features_max_exponent)
            self._feature_adder.add()
            self.training_data = self._feature_adder.info
            self._exponents_of_original_features_in_order = self._feature_adder.powers_order
        else:
            self.training_data = self._add_ones(self.training_data)
            num_of_features = self.original_training_data.shape[1]
            self._exponents_of_original_features_in_order = np.append(np.zeros(shape=(1, num_of_features)),
                                                                      np.eye(num_of_features),
                                                                      axis=0)

    def _normalize_features(self):
        if not self.normalization:
            return

        self._normalizer = FeatureNormalizer(self.training_data[:, 1:])
        self.training_data[:, 1:] = self._normalizer.normalize()

    def _gradient_checking(self):
        """
        Compare the _get_gradient function with numerical gradient using two points on the function (epsilon to each side)

        :return: True/False
        """
        if not self.gradient_checking:
            return

        theta_is_array = isinstance(self.theta, np.ndarray)
        x, y, test_theta, architecture = GradientChecker.get_constant_values_to_check(theta_is_array)

        if theta_is_array:
            def cost_func(theta):
                return self.compute_cost(x, y, theta, self.regularization)

            def gradient_func(theta):
                return self.get_gradient(x, y, theta, self.regularization)
        else:
            def cost_func(theta):
                return self.compute_cost(x, y, theta, self.regularization, architecture)

            def gradient_func(theta):
                return self.get_gradient(x, y, theta, self.regularization, architecture)

        checker = GradientChecker(cost_func, gradient_func, self.verbose)
        checker.check(test_theta)

    def _gradient_descent_single_step(self, gradient):
        self.theta = self.theta - (self.learning_rate * gradient)

    @classmethod
    def get_gradient(cls, X, y, theta, regularization=True):
        """
        This method should change self.theta.

        :param X: training info (1-column-padded)
        :type X: 2-D array
        :param y: training results (answers)
        :type y: column array
        :param theta: specific prediction to check (current theta)
        :type theta: array
        :param regularization: if gradient should use a regularization term to regularize thetas (except for theta zero)
        :type regularization: bool

        :return: gradient for all thetas - an array with a length of all thetas
        :rtype: n + 1 sized array of floats
        """
        theta = r2c(theta)
        if regularization:
            return cls._get_gradient_with_regularization(X, y, theta)
        else:
            return cls._get_gradient_without_regularization(X, y, theta)

    @classmethod
    def _get_gradient_with_regularization(cls, X, y, theta):
        m = y.size

        theta_zero_summation = (cls._hypothesis(X, theta) - y) * r2c(X[:, 0])
        theta_zero_gradient = (1 / m) * r2c(sum(theta_zero_summation))

        theta_rest_summation = (cls._hypothesis(X, theta) - y) * X[:, 1:]
        theta_rest_regularized_term = (cls.REGULARIZATION_LAMBDA / m) * theta[1:]
        theta_rest_gradient = ((1 / m) * r2c(sum(theta_rest_summation))) + theta_rest_regularized_term

        gradient = np.append(theta_zero_gradient, theta_rest_gradient, axis=0)

        return gradient

    @classmethod
    def _get_gradient_without_regularization(cls, X, y, theta):
        m = y.size

        summation = (cls._hypothesis(X, theta) - y) * X
        gradient = (1 / m) * r2c(sum(summation))

        return gradient

    @classmethod
    @abstractmethod
    def _hypothesis(cls, X, theta):
        """
        A function that predicts a training result based on training data inputs, and the current theta prediction

        :param X: training info (1-column-padded)
        :type X: 2-D array
        :param theta: specific prediction to check
        :type theta: array

        :return: The hypothesis result
        :rtype: m sized array of floats (m being the amount of training examples - the number of rows in X)
        """
        pass

    @classmethod
    @abstractmethod
    def compute_cost(cls, X, y, theta, regularization=True):
        """
        Should return the cost of a certain theta prediction

        :param X: training info (1-column-padded)
        :type X: 2-D array
        :param y: training results (answers)
        :type y: column array
        :param theta: specific prediction to check
        :type theta: array
        :param regularization: if cost should use a regularization term to regularize thetas (except for theta zero)
        :type regularization: bool

        :return: the cost of the prediction
        :rtype: float
        """
        theta = r2c(theta)
        m = y.size
        pass

    def _assess_for_warnings(self):
        pass

    def predict(self, input_data, theta=None):
        if theta is None:
            theta = self.theta
        data = self._edit_input_data_for_predict(input_data)
        return self._hypothesis(data, theta)

    def _edit_input_data_for_predict(self, data):
        data = to_array(data)
        matrix = is_matrix(data)
        num_of_features = data.shape[1] if matrix else data.size

        if not num_of_features == self.original_training_data.shape[1]:
            raise InputError(self._PREDICT_INPUT_LENGTH_ERROR.format(num_of_features,
                                                                     self.original_training_data.shape[1]))

        data = self._upgrade_predict_data_by_exponents(data, matrix)

        if self.normalization:
            data = self._normalizer.use(data)

        data = self._add_ones(data)

        if not matrix:
            data = r2c(data)

        return data

    def _upgrade_predict_data_by_exponents(self, data, matrix):
        exponents = self._exponents_of_original_features_in_order
        if np.all(exponents[1:] == np.eye(exponents.shape[0] - 1)):
            return data

        if matrix:
            return to_array([self._upgrade_predict_data_by_exponents_single_row(row)
                             for row in data])
        return self._upgrade_predict_data_by_exponents_single_row(data)

    def _upgrade_predict_data_by_exponents_single_row(self, data):
        return np.product(np.power(data,
                                   self._exponents_of_original_features_in_order),
                          axis=1)[1:]