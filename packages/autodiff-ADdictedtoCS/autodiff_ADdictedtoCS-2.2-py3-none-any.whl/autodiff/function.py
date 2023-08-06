import numpy as np
import autodiff
from autodiff.variable import Variable, ReverseVariable
from autodiff.utils import get_right_shape, close
import warnings
"""
Function class is the base class that implements the chain rule and other basic methods.
A Function object takes a Variable object, and returns a new Variable with the transformed value and gradient
The elementary functions that are currently implemented are exp, sin, cos, and tan.

Multiplication, addition, power are implemented in the class Variable. 
It can stay that way or we can consider subclasses such as add(Function), mul(Function)

The Different classes are instantiated so that we can easily import.
Example: import function as F
x=Variable, y = F.exp(x)
"""

#Now, we have the autodiff.config object
#mode = 'reverse'
#operations = []

class Function:
    """
   The get_grad and get_val methods are not implemented for this base class 
   but get_grad implements calculation of derivative, and get_val implements calculation of value
   for the elementary functions which are subclasses of function   
    """

    def get_grad(self, x):
        raise NotImplementedError

    def get_val(self, x):
        raise NotImplementedError

    def __repr__(self):
        """    
        RETURNS
        ========
        string: contains a printable representation of an Function object
    
        """
        return '{}'.format(type(self))

    def __call__(self, x):
        """Implements the chain rule.
        INPUTS
        =======
        x: autodiff.Variable holding a val and grad
    
        RETURNS
        ========
        autodiff.Variable: updated Variable after chain rule was applied 
        """
        # if autodiff.config.mode == 'forward':
        if isinstance(x, Variable):
            out_val = self.get_val(x.val)
            out_grad = np.dot(self.get_grad(x.val), x.grad)
            # out_grad = np.dot(self.get_grad(x.val), x.grad)
            return Variable(val=out_val, grad=out_grad)
        elif isinstance(x, ReverseVariable):
            out_val = self.get_val(x.val)
            res = ReverseVariable(out_val)
            x.children.append(res)
            res.left = x
            res.leftgrad = self.get_grad(x.val)
            return res
        else:
            raise ValueError("Not a variable!")
           
    
class Exponent(Function):
    """Implements calculation of value and derivative of Exponential function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")   
        return np.exp(x)
    
    def get_grad(self, x):
        return np.exp(x)
    
class Sinus(Function):
    """Implements calculation of value and derivative of Sine function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.sin(x)

    def get_grad(self, x):
        return np.cos(x)

class Cosinus(Function):
    """Implements calculation of value and derivative of Cosine function
        Overloads get_val and get_grad from the Function class
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.cos(x)

    def get_grad(self, x):
        return - np.sin(x)

class Tangent(Function):
    """Implements calculation of value and derivative of Tangent function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        tmp = (x - np.pi / 2) / np.pi
        if close(tmp, round(tmp)):
            raise ValueError("Value not in the domain!")
        return np.tan(x)

    def get_grad(self, x):
        # tmp = (x - np.pi / 2) / np.pi
        return 1./np.cos(x)**2

class Arcsin(Function):
    """Implements calculation of value and derivative of Arcsin function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.arcsin(x)

    def get_grad(self, x):
        return 1.0 / np.sqrt(1.0 - x ** 2)

class Arccos(Function):
    """Implements calculation of value and derivative of Arccos function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.arccos(x)

    def get_grad(self, x):
        return -1.0 / np.sqrt(1.0 - x ** 2)

class Arctan(Function):
    """Implements calculation of value and derivative of Arctan function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.arctan(x)

    def get_grad(self, x):
        return 1.0 / (1.0 + x ** 2)

class Sinh(Function):
    """Implements calculation of value and derivative of Sinh function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.sinh(x)

    def get_grad(self, x):
        return np.cosh(x)

class Cosh(Function):
    """Implements calculation of value and derivative of Cosh function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.cosh(x)

    def get_grad(self, x):
        return np.sinh(x)

class Tanh(Function):
    """Implements calculation of value and derivative of Tanh function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.tanh(x)

    def get_grad(self, x):
        return (np.cosh(x) ** 2 - np.sinh(x) ** 2) / (np.cosh(x) ** 2)

class Log(Function):
    """Implements calculation of value and derivative of Log function
        Overloads get_val and get_grad from the Function class
        
    """   

    def __init__(self, base=None):
        if base != None:
            self.base = get_right_shape(base)
            if not isinstance(self.base, float):
                raise ValueError("Not a valid base!")
            if self.base <= 0:
                raise ValueError("Not a valid base!")
        else:
            self.base = None
            

    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!") 
        if self.base == None: 
            return np.log(x)
        else:
            return np.log(x) / np.log(self.base)

    def get_grad(self, x):
        if self.base == None: 
            return 1.0 / x
        else:
            return 1.0 / (x * np.log(self.base))

class Logistic(Function):
    """Implements calculation of value and derivative of Logistic function
        Overloads get_val and get_grad from the Function class  
    #TODO-Write documentation about that.
    """   

    def __init__(self, L=1.0, k=1.0, x0=0):
        self.L = get_right_shape(L)
        self.k = get_right_shape(k)
        self.x0 = get_right_shape(x0)
        if not isinstance(self.L, float) or not isinstance(self.k, float) or not isinstance(self.x0, float):
            raise ValueError("Error input for logistic function!")

    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!") 
        return self.L / (1.0 + np.exp(-self.k * (x - self.x0)))

    def get_grad(self, x):
        return self.get_val(x) * (1.0 - self.get_val(x))

class Sqrt(Function):
    """Implements calculation of value and derivative of Sqrt function
        Overloads get_val and get_grad from the Function class
        
    """   
    def get_val(self, x):
        if not isinstance(x, float):
            raise ValueError("Cannot be a vector!")  
        return np.sqrt(x)

    def get_grad(self, x):
        return 0.5 / np.sqrt(x)

class Dot(Function):
    """
    assumes e is a (N,p) array.
    Elements of e should not require gradient computations.
    Assumes x is a Variable.
    """
    def __init__(self, e):
        self.e = e

    def get_val(self, x):
        #return np.dot((self.e).T, x.val) #p,N x N, = p,
        # return np.dot((self.e).T, x) #p,N x N, = p,
        return np.dot(self.e, x)

    def get_grad(self, x):
        #return (self.e).T #p,N
        return self.e

# class Dot_Var(Function):
#     """
#     #TODO-Could/should be a <class Variable> method.
#     Dot product between variables. 
#     We rewrite the __call__ signature. 
    

"""
    def __init__(self):
        return None

    def __call__(self, X, Y):
        assert X.val.shape == Y.val.shape, "Variables of different sizes. dot product undefined."
        assert X.grad.shape == Y.grad.shape, "Gradients of different sizes provided."
        unroll_X, unroll_Y = unroll(X), unroll(Y)
        dot_product = 0.
        for x, y in zip(unroll_X, unroll_Y):
            dot_product += x*y
        return dot_product

class Dot_(Function):
    '''
    User friendly usage of dot. No Need to instantiate the dot. 
    Works on right and left multiplication by a matrix for instance.
    Also enable
    '''
    def __init__(self):
        return None

    def __call__(self, e, x):
        if isinstance(e, Variable) and isinstance(x, Variable):
            return Dot_Var()(e,x)
        else:
            try: #We have e which is supposed to be a matrix then   
                return Dot(e)(x) 
            except Exception:
                message = "Need to provide a Variable and right shapesTypes and shapes are: {}, {}| {}, {}".format(type(e), 
                type(x), e.shape, (x.val.shape, x.grad.shape))
                assert isinstance(e, Variable), message
                val = Dot(x.T)(e)
                warnings.warn('Matrix multiplication on the right')
                return val
"""

def concat(var_list:list):
    """
    If x, y variables, it should let the user define conc_x,y = F.concat([x,y]) which is now a multivariate stuff. 
    Assume we have two variables in R^2 and R^3 respectively.
    There are supposed to have the same input space, for instance X^10 so that the gradients are 10,2 and 10,3 dimensions.
    var_list has to be a list of var. 
    """
    assert len(var_list)>0, 'Can not concatenate an empty list'
    input_dim = var_list[0].grad.shape[1] #grad shape of the first variable in the list
    concat_val, concat_grad = [], []
    for var in var_list:
        assert var.grad.shape[1] == input_dim, 'trying to concatenate variables from a different input space'
        if isinstance(var.val, float):
            concat_val.append(np.array(var.val).reshape(-1,1))
        else: #We already have an array
            concat_val.append(var.val)
        concat_grad.append(var.grad)
        #print(var.grad.shape)
        #print(len(concat_val))
    out_val = np.concatenate(concat_val)# We have list that must be changed
    out_grad = np.concatenate(concat_grad, axis=0)
    return Variable(val=out_val, grad=out_grad)
    
def generate_base(N):
    """Function to generate the canonical basis of R^{N}
    Helper function.
    Input: Dimesion of the space we want the base
    Output: 
    Dictionary with keys e_1,...,e_N and values are the associated 
    basis vectors.

    Further DOC-> Finish the doc. Say that it is equivalent to slicing actually. 
    """
    Id = np.eye(N)
    basis = {'e{}'.format(i): Id[i].reshape(-1,1) for i in range(N)}
    return basis

#=======================
# Elementary-Wise function.
#=====================

class ew_Exponent(Function):
    """
    Implements calculation of value and derivative of Exponential function element-wise
        Overloads get_val and get_grad from the Function class
    """
    warnings.warn(
        "Using the element-wise composition. Beta version. Not entirely tested.")

    def get_val(self, x):
        return np.exp(x)

    def get_grad(self, x):
        return np.diagflat(np.exp(x))

class ew_Sinus(Function):
    """Implements calculation of value and derivative of Sine function element-wise
        Overloads get_val and get_grad from the Function class
    """
    warnings.warn(
        "Using the element-wise composition. Beta version. Not entirely tested.")

    def get_val(self, x):
        return np.sin(x)

    def get_grad(self, x):
        return np.diagflat(np.cos(x))

class ew_Cosinus(Function):
    """Implements calculation of value and derivative of Cosine function element-wise
        Overloads get_val and get_grad from the Function class
    """
    warnings.warn(
        "Using the element-wise composition. Beta version. Not entirely tested.")

    def get_val(self, x):
        return np.cos(x)

    def get_grad(self, x):
        return - np.diagflat(np.sin(x))

class ew_Tangent(Function):
    """Implements calculation of value and derivative of Tangent function element-wise
        Overloads get_val and get_grad from the Function class 
    """
    warnings.warn(
        "Using the element-wise composition. Beta version. Not entirely tested.")

    def get_val(self, x):
        for t in x.flatten():
            tmp = (t - np.pi / 2) / np.pi
            if close(tmp, round(tmp)):
                raise ValueError("Value not in the domain!")
        return np.tan(x)

    def get_grad(self, x):
        # tmp = (x - np.pi / 2) / np.pi
        return np.diagflat(1./np.cos(x)**2)

#========================
#User aliases
#========================
exp = Exponent()
sin = Sinus()
cos = Cosinus()
tan = Tangent()
sqrt = Sqrt()
log = Log()
logi = Logistic()
arcsin = Arcsin()
arccos = Arccos()
arctan = Arctan()
sinh = Sinh()
cosh = Cosh()
tanh = Tanh()
ew_cos = ew_Cosinus()
ew_tan = ew_Tangent()
ew_exp = ew_Exponent()
ew_sin = ew_Sinus()

if __name__ == "__main__":
    #=====================
    #DEMO
    #===================
    from autodiff.variable import Variable, ReverseVariable
    import autodiff.function as F
    X = Variable(np.array([1,5,10]))
    #x = Variable(2.)
    Y = Variable(np.array([3,7,12]))
    #print(x)
    print(X.val)
    Z = X + Y
    x, y, z = X.unroll()
    print(x.val, x.grad.shape)
    xyz = (x+y)*z
    xy = x+y
    print(xyz.val, xy.grad.shape)
    print(xy.val, xy.grad.shape)
    f = concat([xyz, xy])
    print(f.val, f.val.shape, f.grad, f.grad.shape)
    
    #=============
    #Dirty old demos
    #==============
    """
    def first_demos(X):
        x,y,z = unroll(X)
        print(x,y,z)
        out = exp(x) + cos(y)
        out += x
        #=============
        #Check whether it matches what we hoped ?
        #===========
        print('Expected value', np.exp(X.val[0])+np.sin(X.val[1]))
        print('Expected gradients', np.exp(X.val[0])+1, -np.sin(X.val[1]), 0)

        #====================
        # DEMO with a Linear matrix mulitplication ? 
        #====================
        #X does not change.
        print('Second part')
        e0, e1, e2 = generate_base(X.val.shape[0]).values()
        print(e1)
        out = dot_(e0,X)
        print('Out', out)
        ut_2 = dot_(e1, X)
        print('Out_2', out_2)

        matrix = np.array([[4,6,0], [1,0,2]]).T
        matrix_mul = dot_(matrix, X) #2,3 x #3, -> 2,
        print('matrix_mul', matrix_mul)
        #What if we want to expand to a bigger dimension ? 
        new_mm = dot_(matrix.T, matrix_mul) #3,2->2,
        print('New mm', new_mm)

        #print(type(X), 'class autodiff.variable.Variable')
        #print(getattr(X,'type'))
        print(isinstance(X,Variable))
    
        out_x = dot_(X, matrix.T) #3, x 3,2
        print('out_x', out_x)

        new_X = concat([x,y])
        print(X)
        print(new_X)

        full_X = concat([new_X,z])
        print('full_X', full_X)
        #print('EQ?', full_X == X)
        print((X.grad==full_X.grad).all())
    def second_demos(X):
        U = Variable(np.array([1, 5, 10]))
        u1,u2,u3 = unroll(U)
        #We should not do U.dot(X)
        out = Dot_Var()(X,U)
        print('1', out)
        out = dot_(X,U)
        print('2', out)
        out = dot_(U,X)
        print('3', out)
        matrix = np.array([[4, 6, 0], [1, 0, 2]]).T
        out = dot_(matrix, X)
        print('4', out)
        out = dot_(X, matrix.T)
        print('5', out)
    def third_demos(x):
        x = Variable(np.array([10]))
        x1 = exp(x)
        #Naive way=create a new var with the default gradient.
        x1_= Variable(x1.val)
        print(x1)
        print(x1_)
        x2 = sin(x1)
        print(x2)
        x2_ = sin(x1_)
        print(x2_)
        print(x2_.grad * x1.grad)

        #Let's assume we want to compute the backward pass of sin(exp(cos))
        x = Variable(np.array([np.log(2)]))
        _var = []
        x1 = exp(x)
        _var.append(x1)
        x1_ = Variable(x1.val)
        x2 = sin(x1_)
        _var.append(x2)

        grad = 1.
        for var in _var:
            grad = grad * var.grad
            print(grad)
        print('Done')
    def my_func(x):
        return sin(exp(x))
    def my_func_backward(x):
        print('1-here', autodiff.config.reverse_graph)
        y = exp.call_reverse(x)
        print('2-here', autodiff.config.reverse_graph)
        z = sin.call_reverse(y)
        print('3-here', autodiff.config.reverse_graph)
        out_grad = z.do_backward()
        return out_grad
    def demos_old_rev_mode():
        x = Variable(np.array([np.log(2.)]))
        print('FWD', my_func(x))
        #TODO-Make a setter to change that
        autodiff.config.mode='reverse'
        autodiff.config.reverse_graph = []
        print('Backward gradient', my_func_backward(x))
    """
