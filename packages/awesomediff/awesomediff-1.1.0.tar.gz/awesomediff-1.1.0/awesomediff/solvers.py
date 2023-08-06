from inspect import signature

import random

from awesomediff.core import variable
from awesomediff.core import evaluate

from awesomediff.func import sin
from awesomediff.func import cos
from awesomediff.func import tan
from awesomediff.func import log
from awesomediff.func import sqrt
from awesomediff.func import exp
from awesomediff.func import sinh
from awesomediff.func import cosh
from awesomediff.func import tanh


def l1_norm(vals):
    return sum([abs(v) for v in vals])

def l2_norm(vals):
    return sqrt(sum([v**2 for v in vals])).val

def mean(vals):
    return sum([v for v in vals])/len(vals)

def variance(vals):
    mu = mean(vals)
    return sum([(v-mu)**2 for v in vals])/len(vals)
 
def mean_squared_error(y_true,y_pred):
 
    assert len(y_true)==len(y_pred)
    return sum([(true-pred)**2 for true,pred in zip(y_true,y_pred)]) / len(y_true)
 
def sum_square_residuals(y_true,y_pred):
 
    assert len(y_true)==len(y_pred)
    return sum([(true-pred)**2 for true,pred in zip(y_true,y_pred)])
 
def total_sum_squares(y_true):
 
    y_bar = mean(y_true)
    return sum([(true-y_bar)**2 for true in y_true])
 
def r2_score(y_true,y_pred):
 
    assert len(y_true)==len(y_pred)
    rss = sum_square_residuals(y_true,y_pred)
    tss = total_sum_squares(y_true)
    return 1 - rss/tss

def transpose(M,check=True):
    """Transpose a matrix (list of lists)."""

    if check:
        M = _check_inputs(M)
    
    n_rows = len(M)
    n_cols = len(M[0])
    new_M = []

    for c in range(n_cols):
        new_row = []
        for r in range(n_rows):
            new_row.append( M[r][c] )
        new_M.append( new_row )
    
    return new_M


def standardize(M,check=True,return_stats=False):
    """
        Transform a matrix (list of lists) so that each column has mean 0 and standard deviation 1.
        If `return_stats==True`, returns a tuple: transposed_matrix, list_of_means, list_of_standard_deviations.
        If `check==True`, ensures that the input is a list of lists.
    """

    if check:
        M = _check_inputs(M)
    M_ = []
    Mt = transpose(M,check=False)
    mus = []
    sigmas = []
    for row in Mt:
        mu = mean(row)
        sigma = sqrt(variance(row)).val
        M_.append( [(v-mu)/sigma for v in row] )
        mus.append(mu)
        sigmas.append(sigma)
    M_ = transpose(M_,check=False)
    if return_stats:
        return (M_,mus,sigmas)
    else:
        return M_


def _check_inputs(X,y=None):
    """Converts a matrix X into a list of lists and a vector y into a list."""

    new_X = []
    
    for row in X:
        new_row = []
        for val in row:
            new_row.append( float(val) )
        new_X.append( new_row )

    if y is None:

        return new_X

    else:
        
        new_y = []

        for val in y:
            try:
                new_y.append( float(val) )
            except:
                new_y.append( float(val[0]) )

        assert len(X)==len(y), "Dimensions of X and y do not match."

        return new_X,new_y


class Solver:

    def __init__(self,model,**solver_params):
        self.model = model
        raise NotImplementedError

    def solve(self,model_params,initial_weights,X,y):
        raise NotImplementedError


class GradientDescent(Solver):
    
    def __init__(self,model,learning_rate=0.01,rel_tol=1e-5,abs_tol=1e-8,max_iter=10000,random_seed=None,verbose=False):
        
        self.model = model
        self.learning_rate = learning_rate
        self.rel_tol = rel_tol
        self.abs_tol = abs_tol
        self.max_iter = max_iter
        self.random_seed = random_seed
        self.verbose = verbose

    def solve(self,model_params,initial_weights,X,y):

        # Set random seed:
        if self.random_seed is not None:
            random.seed(self.random_seed)
        else:
            random.seed()
        alpha = self.learning_rate
        def loss_func(*weights):
            return self.model._loss(model_params,weights,X,y)
            
        prev_loss = None
        prev_weights = initial_weights

        converged = False
        iteration = 0
        while not converged:
            iteration += 1
            loss,grad = evaluate(loss_func,prev_weights)
            weights = [w - alpha * gr for w,gr in zip(prev_weights,grad)]
            if self.verbose:
                print("Step {}: loss={}; grad={}".format(iteration,loss,grad))
                #print("Step {}: loss={}".format(iteration,loss))
            # Check for stopping conditions:
            if iteration >= self.max_iter:
                converged = True
                if self.verbose:
                    print("Stop : iteration={}".format(iteration))
                break
            if (prev_loss is not None) and (abs(loss-prev_loss) < self.abs_tol):
                converged = True
                if self.verbose:
                    print("Stop : abs_tol={}".format(abs(loss-prev_loss)))
                break
            if (prev_loss is not None) and (abs((loss-prev_loss)/prev_loss) < self.rel_tol):
                converged = True
                if self.verbose:
                    print("Stop : rel_tol={}".format(abs((loss-prev_loss)/prev_loss)))
                break
            prev_loss = loss
            prev_weights = weights
        
        if not converged:
            print("Warning: Gradient descent did not converge.")
        
        # Un-set random seed:
        random.seed()
            
        return weights


class Model:

    def __init__(self):
        """Initialize the model."""
        pass

    @classmethod
    def _pack_weights(cls,model_params,placeholder):
        """Create a single list of weights to pass to the solver."""
        raise NotImplementedError

    @classmethod
    def _unpack_weights(cls,model_params,weights):
        """Extract weights from list returned by the solver."""
        raise NotImplementedError

    @classmethod
    def _loss(cls,model_params,weights,X,y):
        """Calculate the loss between y and the predictions made with X using specified parameters and weights."""
        raise NotImplementedError

    @classmethod
    def _predict(cls,model_params,weights,X):
        """Predict X using specified parameters and weights."""
        raise NotImplementedError

    def predict(self,X):
        """Predict X."""
        raise NotImplementedError

    def fit(self,X,y):
        """Fit the model to X and y."""
        raise NotImplementedError

    def score(self,X,y):
        """Return the score of y and the predictions made with X."""
        raise NotImplementedError


class LinearRegression(Model):
    """Ordinary least squares regression."""

    def __init__(self,fit_intercept=True,standardize=False,solver='gradient_descent',**solver_kwargs):
        """Initialize the model."""

        valid_solvers = ['gradient_descent']
        if solver=='gradient_descent':
            self.solver = GradientDescent(model=self,**solver_kwargs)
        else:
            raise ValueError("Solver must be one of the following: {}".format(", ".join(valid_solvers)))
        
        self.standardize = standardize  # Ensure that features have mean zero and standrd deviation one before solving.
        self.fit_intercept = fit_intercept
        self.intercept = None
        self.coefs = []

        # Store model parameters to pass to solver:
        self.model_params = { 'fit_intercept' : self.fit_intercept }

    @classmethod
    def _pack_weights(cls,model_params,intercept,coefs):
        """Create a single list of weights to pass to the solver."""

        if model_params['fit_intercept']:
            return [intercept]+coefs
        else:
            return coefs

    @classmethod
    def _unpack_weights(cls,model_params,weights):
        """Extract weights from list returned by the solver."""

        fit_intercept = model_params['fit_intercept']

        if (fit_intercept==True) and len(weights)==1:
            intercept = weights[0]
            coefs = []
        elif (fit_intercept==True) and len(weights)>1:
            intercept = weights[0]
            coefs = weights[1:]
        elif (fit_intercept==False):
            intercept = 0
            coefs = weights
        
        return intercept,coefs

    @classmethod
    def _loss(cls,model_params,weights,X,y):
        """Calculate the loss between y and the predictions made with X using specified parameters and weights."""

        return mean_squared_error( y , cls._predict(model_params,weights,X) )
    
    @classmethod
    def _predict(cls,model_params,weights,X):
        """Predict X using specified parameters and weights."""

        intercept,coefs = cls._unpack_weights(model_params,weights)
        predictions = []
        for vals in X:
            pred = intercept
            for x,coef in zip(vals,coefs):
                pred += x*coef
            predictions.append(pred)
        return predictions

    def predict(self,X):
        """Predict X."""

        X = _check_inputs(X,y=None)
        assert len(X[0])==len(self.coefs), "X does not match dimensions of fitted model."
        if self.standardize:
            X = standardize(X,check=False,return_stats=False)
        predictions = []
        for vals in X:
            pred = sum([x*coef for x,coef in zip(vals,self.coefs)])
            pred += self.intercept if self.fit_intercept else 0
            predictions.append(pred)
        return predictions

    def fit(self,X,y):
        """Fit the model to X and y."""

        # Check inputs:
        X,y = _check_inputs(X,y)
        n_features = len(X[0])
        n_weights = n_features+1 if self.fit_intercept==True else n_features

        # Standardize data:
        if self.standardize:
            X = standardize(X,check=False,return_stats=False)

        # Prepare parameters and initialize weights:
        #initial_weights = [random.uniform(0,1) for _ in range(n_weights)]
        initial_weights = [0 for _ in range(n_weights)]

        # Invoke solver (on standardized data):
        weights = self.solver.solve(self.model_params,initial_weights,X,y)

        # Expose final values to user:
        intercept,coefs = LinearRegression._unpack_weights(self.model_params,weights)
        self.intercept = intercept if self.fit_intercept else None
        self.coefs = coefs

    def score(self,X,y):
        """Return the score of y and the predictions made with X."""

        X,y = _check_inputs(X,y)
        return r2_score(y,self.predict(X))


class LassoRegression(LinearRegression):
    """Linear regression model with L1 regularization."""

    def __init__(self,l1_penalty=0.1,fit_intercept=True,standardize=False,solver='gradient_descent',**solver_kwargs):
        """Initialize LinearRegression model with adjustments for L2 regularization."""

        super().__init__(fit_intercept=True,standardize=False,solver='gradient_descent',**solver_kwargs)

        # Store model parameters to pass to solver:
        self.l1_penalty = l1_penalty
        self.model_params = { 'fit_intercept' : self.fit_intercept, 'l1_penalty' : self.l1_penalty }

    @classmethod
    def _loss(cls,model_params,weights,X,y):
        """Calculate the loss between y and the predictions made with X using specified parameters and weights."""

        l1_penalty = model_params['l1_penalty']
        return mean_squared_error( y , cls._predict(model_params,weights,X) ) + l1_penalty * l1_norm(weights)


class RidgeRegression(LinearRegression):
    """Linear regression model with L2 regularization."""

    def __init__(self,l2_penalty=0.1,fit_intercept=True,standardize=False,solver='gradient_descent',**solver_kwargs):
        """Initialize LinearRegression model with adjustments for L2 regularization."""

        super().__init__(fit_intercept=True,standardize=False,solver='gradient_descent',**solver_kwargs)

        # Store model parameters to pass to solver:
        self.l2_penalty = l2_penalty
        self.model_params = { 'fit_intercept' : self.fit_intercept, 'l2_penalty' : self.l2_penalty }

    @classmethod
    def _loss(cls,model_params,weights,X,y):
        """Calculate the loss between y and the predictions made with X using specified parameters and weights."""

        l2_penalty = model_params['l2_penalty']
        return mean_squared_error( y , cls._predict(model_params,weights,X) ) + l2_penalty * l2_norm(weights)



def gradientDescent(func, initial, rate=0.01, precision=0.00001, iteration = 2000):
	# df = func
	count = 0
	current = initial
	while (step>precision and count <iteration):
		last = current
		current = current - rate*func(last)
		step = abs(current-last)
		count+=1

	return current


# Newton-Raphson Method
def uni_Newton(func, initial, max_iter=200, epsilon=1e-06):
	'''

	:param func: univariate function
	:param initial: starting point(scalar)
	:param max_iter: max iteration
	:param epsilon: change in function value < epsilon (stopping condition)
	:return: if root is found, return the root. Otherwise None

	def root_finding(a):
    	return a**2 + 2*a + 1
    root = uni_Newton(root_finding, 50)
    root_finding(root) #gives something close to 0
	'''

	# Check Input formats
	sig = signature(func)  # function should take only one scalar input
	if len(sig.parameters) != 1:
		raise ValueError('The function should be uni-variate')

	# check the initial point is a scalar
	try:
		int(initial)
	except ValueError:
		print('The input must be a scalar')

	current_x = int(initial)
	for i in range(max_iter):
		func_val, func_der = evaluate(func, current_x)

		if abs(func_val) <= epsilon:
			print('Root Approximation Found!', ' root = ', current_x)
			return current_x

		if i == max_iter - 1:
			print(
				'Max iteration reached, failed to find the root. The function may not have a root or try increase iteration numbers')
			return None

		# check if it's a bad derivative(0)
		if abs(func_der[0]) <= 10 ** (-15):
			print('Bad Starting Point: Derivative of the function = 0 at some point')
			return None
			break

		current_x = current_x - func_val / func_der[0]

