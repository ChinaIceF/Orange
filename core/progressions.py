import numpy


## CHANGE LOGS ##
## 2023.7.29 created processions.py
## 2023.7.30 added 5 classes (progression, orange, OFunc, arith, geo)


# Define class Progression 
class progression(numpy.ndarray):

    def __new__(cls, func, xarray):
        xarray = numpy.array(xarray)

        # check if xrange is in the shape of (2,)
        if len(xarray.shape) != 1:
            raise SyntaxError(xarray)
            
        # change self.func into OFunc if it is not a OFunc
        if str(type(func)) != "<class 'orange.core.progressions.OFunc'>":
            try:
                func = OFunc(func)
            except:
                raise TypeError(func)
        
        return func.generate_array(xarray)


class orange(numpy.ndarray):
    
    def __new__(cls, *atuple):
        input_range = numpy.array(atuple)

        if len(input_range.shape) != 1:
            raise ValueError(input_range)

        if input_range.shape[0] > 3 or input_range.shape[0] < 2:
            raise ValueError(input_range)

        if input_range.shape[0] == 2:
            arange = numpy.arange(input_range[0], input_range[1])

        if input_range.shape[0] == 3:
            arange = numpy.arange(input_range[0], input_range[1], input_range[2])

        return arange


# OFunc returns a new object
# Define class OFunc, which contains a function to generate progression
class OFunc(object):
    
    def __init__(self, func, name = None):
        self.func = func
        self.name = name
    
    def generate_array(self, xarray):
        try:
            array = self.func(xarray)
            
        except:
            array = numpy.zeros(len(xarray))
            for i, x in enumerate(array):
                array[i] = self.func(x)
        
        return array
    
    def info(self):
        print('')
        print(' >> Orange.Ofunc object')
        print('    Name:\t{}'.format(self.name))
        print('    Object:\t{}'.format(self))
        print('      Function:\t{}'.format(self.func))
        print('')


# Arithmetic progression
class arith(OFunc):
    
    def __new__(cls, k, b, name = None):
        return OFunc(lambda x: k*x+b, name = name)


# Geometric progression
class geo(OFunc):
    
    def __new__(cls, a, name = None):
        return OFunc(lambda x: a ** x)