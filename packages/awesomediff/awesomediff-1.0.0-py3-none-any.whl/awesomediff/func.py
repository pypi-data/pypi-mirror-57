import math
import numpy as np

from awesomediff.core import variable

def sin(x):
    """
        Helper function that calculates the sin of a variable or number.

        INPUTS:
            x : awesomediff.variable object or a number.

        OUTPUT:
            awesomediff.variable
    """
    
    try:
        # Assume object is a variable:
        val = x.val
        der = x.der
    except:
        # If not, treat it as a constant.
        try:
            float(x)
        except:
            raise ValueError("{} is not a number.".format(x))
        val = x
        der = 0  # Derivative of a constant is zero.
    # Calculate new value an derivative:
    new_val = np.sin(val)
    new_der = np.cos(val)*der
    # Return variable with new value an derivative:
    return variable(val=new_val,der=new_der)

def cos(x):
    """
        Helper function that calculates the sin of a variable or number.

        INPUTS:
            x : awesomediff.variable object or a number.

        OUTPUT:
            awesomediff.variable
    """
    
    try:
        # Assume object is a variable:
        val = x.val
        der = x.der
    except:
        # If not, treat it as a constant.
        try:
            float(x)
        except:
            raise ValueError("{} is not a number.".format(x))
        val = x
        der = 0  # Derivative of a constant is zero.
    # Calculate new value an derivative:
    new_val = np.cos(val)
    new_der = -np.sin(val)*der
    # Return variable with new value an derivative:
    return variable(val=new_val,der=new_der)

def tan(x):
    """
        Helper function that calculates the sin of a variable or number.

        INPUTS:
            x : awesomediff.variable object or a number.

        OUTPUT:
            awesomediff.variable
    """
    
    try:
        # Assume object is a variable:
        val = x.val
        der = x.der
    except:
        # If not, treat it as a constant.
        try:
            float(x)
        except:
            raise ValueError("{} is not a number.".format(x))
        val = x
        der = 0  # Derivative of a constant is zero.
    # Calculate new value an derivative:
    new_val = np.tan(val)
    new_der = ((1/np.cos(val))**2)*der
    # Return variable with new value an derivative:
    return variable(val=new_val,der=new_der)

def log(x):
    """
        Helper function that calculates the natural log of a variable or number.

        INPUTS:
            x : AutoDiff.variable object or a number.

        OUTPUT:
            AutoDiff.variable
    """
    try:
        # x.val = np.log(x.val)
        # x.der = (1/x.val)*x.der
        new_val = np.log(x.val)
        new_der = (1/x.val)*x.der
        # return x
        return variable(val=new_val,der=new_der)
    except:
        new_val = np.log(x)
        new_der = 0
        return variable(val=new_val,der=new_der)

def sqrt(x):
    """
        Helper function that calculates the square root of a variable or number.

        INPUTS:
            x : AutoDiff.variable object or a number.

        OUTPUT:
            AutoDiff.variable
    """
    try:
        new_val = np.sqrt(x.val)
        new_der = (0.5/np.sqrt(x.val))*x.der
        return variable(val=new_val,der=new_der)
    except:
        new_val = np.sqrt(x)
        new_der = 0
        return variable(val=new_val,der=new_der)

def exp(x):
    """
        Helper function that calculates the exponential of a variable or number.

        INPUTS:
            x : AutoDiff.variable object or a number.

        OUTPUT:
            AutoDiff.variable
    """
    try:
        new_val = np.exp(x.val)
        new_der = np.exp(x.val)*x.der
        return variable(val=new_val,der=new_der)
    except:
        new_val = np.exp(x)
        new_der = 0
        return variable(val=new_val,der=new_der)
