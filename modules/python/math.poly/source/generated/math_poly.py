# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.5
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_math_poly', [dirname(__file__)])
        except ImportError:
            import _math_poly
            return _math_poly
        if fp is not None:
            try:
                _mod = imp.load_module('_math_poly', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _math_poly = swig_import_helper()
    del swig_import_helper
else:
    import _math_poly
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


import coda.math_linear
import coda.coda_except

def new_doubleArray(nelements):
    """new_doubleArray(size_t nelements) -> double *"""
    return _math_poly.new_doubleArray(nelements)

def delete_doubleArray(ary):
    """delete_doubleArray(double * ary)"""
    return _math_poly.delete_doubleArray(ary)

def doubleArray_getitem(ary, index):
    """doubleArray_getitem(double * ary, size_t index) -> double"""
    return _math_poly.doubleArray_getitem(ary, index)

def doubleArray_setitem(ary, index, value):
    """doubleArray_setitem(double * ary, size_t index, double value)"""
    return _math_poly.doubleArray_setitem(ary, index, value)
class Poly1D(_object):
    """Proxy of C++ math::poly::OneD<(double)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Poly1D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Poly1D, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(math::poly::OneD<(double)> self) -> Poly1D
        __init__(math::poly::OneD<(double)> self, std_vector_double coef) -> Poly1D
        __init__(math::poly::OneD<(double)> self, size_t order) -> Poly1D
        __init__(math::poly::OneD<(double)> self, size_t order, double const * coef) -> Poly1D
        """
        this = _math_poly.new_Poly1D(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def order(self):
        """order(Poly1D self) -> size_t"""
        return _math_poly.Poly1D_order(self)


    def size(self):
        """size(Poly1D self) -> size_t"""
        return _math_poly.Poly1D_size(self)


    def empty(self):
        """empty(Poly1D self) -> bool"""
        return _math_poly.Poly1D_empty(self)


    def scaleVariable(self, scale):
        """scaleVariable(Poly1D self, double scale) -> Poly1D"""
        return _math_poly.Poly1D_scaleVariable(self, scale)


    def truncateTo(self, order):
        """truncateTo(Poly1D self, size_t order) -> Poly1D"""
        return _math_poly.Poly1D_truncateTo(self, order)


    def truncateToNonZeros(self, zeroEpsilon=0.0):
        """
        truncateToNonZeros(Poly1D self, double zeroEpsilon=0.0) -> Poly1D
        truncateToNonZeros(Poly1D self) -> Poly1D
        """
        return _math_poly.Poly1D_truncateToNonZeros(self, zeroEpsilon)


    def transformInput(self, gx, zeroEpsilon=0.0):
        """
        transformInput(Poly1D self, Poly1D gx, double zeroEpsilon=0.0) -> Poly1D
        transformInput(Poly1D self, Poly1D gx) -> Poly1D
        """
        return _math_poly.Poly1D_transformInput(self, gx, zeroEpsilon)


    def copyFrom(self, p):
        """copyFrom(Poly1D self, Poly1D p)"""
        return _math_poly.Poly1D_copyFrom(self, p)


    def __call__(self, at):
        """__call__(Poly1D self, double at) -> double"""
        return _math_poly.Poly1D___call__(self, at)


    def integrate(self, start, end):
        """integrate(Poly1D self, double start, double end) -> double"""
        return _math_poly.Poly1D_integrate(self, start, end)


    def derivative(self):
        """derivative(Poly1D self) -> Poly1D"""
        return _math_poly.Poly1D_derivative(self)


    def velocity(self, x):
        """velocity(Poly1D self, double x) -> double"""
        return _math_poly.Poly1D_velocity(self, x)


    def acceleration(self, x):
        """acceleration(Poly1D self, double x) -> double"""
        return _math_poly.Poly1D_acceleration(self, x)


    def __imul__(self, *args):
        """
        __imul__(Poly1D self, double cv) -> Poly1D
        __imul__(Poly1D self, Poly1D p) -> Poly1D
        """
        return _math_poly.Poly1D___imul__(self, *args)


    def __mul__(self, *args):
        """
        __mul__(Poly1D self, double cv) -> Poly1D
        __mul__(Poly1D self, Poly1D p) -> Poly1D
        """
        return _math_poly.Poly1D___mul__(self, *args)


    def __iadd__(self, p):
        """__iadd__(Poly1D self, Poly1D p) -> Poly1D"""
        return _math_poly.Poly1D___iadd__(self, p)


    def __add__(self, p):
        """__add__(Poly1D self, Poly1D p) -> Poly1D"""
        return _math_poly.Poly1D___add__(self, p)


    def __isub__(self, p):
        """__isub__(Poly1D self, Poly1D p) -> Poly1D"""
        return _math_poly.Poly1D___isub__(self, p)


    def __sub__(self, p):
        """__sub__(Poly1D self, Poly1D p) -> Poly1D"""
        return _math_poly.Poly1D___sub__(self, p)


    def __idiv__(self, cv):
        """__idiv__(Poly1D self, double cv) -> Poly1D"""
        return _math_poly.Poly1D___idiv__(self, cv)


    def __div__(self, cv):
        """__div__(Poly1D self, double cv) -> Poly1D"""
        return _math_poly.Poly1D___div__(self, cv)


    def power(self, toThe):
        """power(Poly1D self, size_t toThe) -> Poly1D"""
        return _math_poly.Poly1D_power(self, toThe)


    def __getitem__(self, i):
        """__getitem__(Poly1D self, long i) -> double"""
        return _math_poly.Poly1D___getitem__(self, i)


    def __setitem__(self, i, val):
        """__setitem__(Poly1D self, long i, double val)"""
        return _math_poly.Poly1D___setitem__(self, i, val)


    def __str__(self):
        """__str__(Poly1D self) -> std::string"""
        return _math_poly.Poly1D___str__(self)


    def __deepcopy__(self, memo):
        """__deepcopy__(Poly1D self, PyObject * memo) -> Poly1D"""
        return _math_poly.Poly1D___deepcopy__(self, memo)

    __swig_destroy__ = _math_poly.delete_Poly1D
    __del__ = lambda self: None
Poly1D_swigregister = _math_poly.Poly1D_swigregister
Poly1D_swigregister(Poly1D)

class Poly2D(_object):
    """Proxy of C++ math::poly::TwoD<(double)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Poly2D, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Poly2D, name)
    __repr__ = _swig_repr

    def coeffs(self):
        """coeffs(Poly2D self) -> std::vector< math::poly::OneD< double >,std::allocator< math::poly::OneD< double > > > &"""
        return _math_poly.Poly2D_coeffs(self)


    def __init__(self, *args):
        """
        __init__(math::poly::TwoD<(double)> self) -> Poly2D
        __init__(math::poly::TwoD<(double)> self, size_t orderX, size_t orderY) -> Poly2D
        __init__(math::poly::TwoD<(double)> self, std::vector< math::poly::OneD< double >,std::allocator< math::poly::OneD< double > > > const & v) -> Poly2D
        """
        this = _math_poly.new_Poly2D(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def empty(self):
        """empty(Poly2D self) -> bool"""
        return _math_poly.Poly2D_empty(self)


    def orderX(self):
        """orderX(Poly2D self) -> size_t"""
        return _math_poly.Poly2D_orderX(self)


    def orderY(self):
        """orderY(Poly2D self) -> size_t"""
        return _math_poly.Poly2D_orderY(self)


    def __call__(self, atX, atY):
        """__call__(Poly2D self, double atX, double atY) -> double"""
        return _math_poly.Poly2D___call__(self, atX, atY)


    def integrate(self, xStart, xEnd, yStart, yEnd):
        """integrate(Poly2D self, double xStart, double xEnd, double yStart, double yEnd) -> double"""
        return _math_poly.Poly2D_integrate(self, xStart, xEnd, yStart, yEnd)


    def set(self, i, p):
        """set(Poly2D self, size_t i, Poly1D p)"""
        return _math_poly.Poly2D_set(self, i, p)


    def flipXY(self):
        """flipXY(Poly2D self) -> Poly2D"""
        return _math_poly.Poly2D_flipXY(self)


    def derivativeY(self):
        """derivativeY(Poly2D self) -> Poly2D"""
        return _math_poly.Poly2D_derivativeY(self)


    def derivativeX(self):
        """derivativeX(Poly2D self) -> Poly2D"""
        return _math_poly.Poly2D_derivativeX(self)


    def derivativeXY(self):
        """derivativeXY(Poly2D self) -> Poly2D"""
        return _math_poly.Poly2D_derivativeXY(self)


    def scaleVariable(self, *args):
        """
        scaleVariable(Poly2D self, double scaleX, double scaleY) -> Poly2D
        scaleVariable(Poly2D self, double scale) -> Poly2D
        """
        return _math_poly.Poly2D_scaleVariable(self, *args)


    def truncateTo(self, orderX, orderY):
        """truncateTo(Poly2D self, size_t orderX, size_t orderY) -> Poly2D"""
        return _math_poly.Poly2D_truncateTo(self, orderX, orderY)


    def truncateToNonZeros(self, zeroEpsilon=0.0):
        """
        truncateToNonZeros(Poly2D self, double zeroEpsilon=0.0) -> Poly2D
        truncateToNonZeros(Poly2D self) -> Poly2D
        """
        return _math_poly.Poly2D_truncateToNonZeros(self, zeroEpsilon)


    def transformInput(self, *args):
        """
        transformInput(Poly2D self, Poly2D gx, Poly2D gy, double zeroEpsilon=0.0) -> Poly2D
        transformInput(Poly2D self, Poly2D gx, Poly2D gy) -> Poly2D
        transformInput(Poly2D self, Poly2D gx, double zeroEpsilon=0.0) -> Poly2D
        transformInput(Poly2D self, Poly2D gx) -> Poly2D
        """
        return _math_poly.Poly2D_transformInput(self, *args)


    def atY(self, y):
        """atY(Poly2D self, double y) -> Poly1D"""
        return _math_poly.Poly2D_atY(self, y)


    def __imul__(self, *args):
        """
        __imul__(Poly2D self, double cv) -> Poly2D
        __imul__(Poly2D self, Poly2D p) -> Poly2D
        """
        return _math_poly.Poly2D___imul__(self, *args)


    def __mul__(self, *args):
        """
        __mul__(Poly2D self, double cv) -> Poly2D
        __mul__(Poly2D self, Poly2D p) -> Poly2D
        """
        return _math_poly.Poly2D___mul__(self, *args)


    def __iadd__(self, p):
        """__iadd__(Poly2D self, Poly2D p) -> Poly2D"""
        return _math_poly.Poly2D___iadd__(self, p)


    def __add__(self, p):
        """__add__(Poly2D self, Poly2D p) -> Poly2D"""
        return _math_poly.Poly2D___add__(self, p)


    def __isub__(self, p):
        """__isub__(Poly2D self, Poly2D p) -> Poly2D"""
        return _math_poly.Poly2D___isub__(self, p)


    def __sub__(self, p):
        """__sub__(Poly2D self, Poly2D p) -> Poly2D"""
        return _math_poly.Poly2D___sub__(self, p)


    def __idiv__(self, cv):
        """__idiv__(Poly2D self, double cv) -> Poly2D"""
        return _math_poly.Poly2D___idiv__(self, cv)


    def __div__(self, cv):
        """__div__(Poly2D self, double cv) -> Poly2D"""
        return _math_poly.Poly2D___div__(self, cv)


    def __eq__(self, p):
        """__eq__(Poly2D self, Poly2D p) -> bool"""
        return _math_poly.Poly2D___eq__(self, p)


    def __ne__(self, p):
        """__ne__(Poly2D self, Poly2D p) -> bool"""
        return _math_poly.Poly2D___ne__(self, p)


    def power(self, toThe):
        """power(Poly2D self, size_t toThe) -> Poly2D"""
        return _math_poly.Poly2D_power(self, toThe)


    def __getitem__(self, inObj):
        """__getitem__(Poly2D self, PyObject * inObj) -> double"""
        return _math_poly.Poly2D___getitem__(self, inObj)


    def __setitem__(self, inObj, val):
        """__setitem__(Poly2D self, PyObject * inObj, double val)"""
        return _math_poly.Poly2D___setitem__(self, inObj, val)


    def __str__(self):
        """__str__(Poly2D self) -> std::string"""
        return _math_poly.Poly2D___str__(self)


    def __deepcopy__(self, memo):
        """__deepcopy__(Poly2D self, PyObject * memo) -> Poly2D"""
        return _math_poly.Poly2D___deepcopy__(self, memo)

    __swig_destroy__ = _math_poly.delete_Poly2D
    __del__ = lambda self: None
Poly2D_swigregister = _math_poly.Poly2D_swigregister
Poly2D_swigregister(Poly2D)


def fit(*args):
    """
    fit(size_t numObs, double const * x, double const * y, size_t numCoeffs) -> Poly1D
    fit(MatrixDouble x, MatrixDouble y, MatrixDouble z, size_t nx, size_t ny) -> Poly2D
    fit(size_t numRows, size_t numCols, double const * x, double const * y, double const * z, size_t nx, size_t ny) -> Poly2D
    fit(VectorDouble xObs, VectorDouble yObs0, VectorDouble yObs1, VectorDouble yObs2, size_t numCoeffs) -> PolyVector3
    fit(VectorDouble xObsVector, MatrixDouble yObsMatrix, size_t numCoeffs) -> PolyVector3
    fit(std_vector_double xObs, std_vector_double yObs0, std_vector_double yObs1, std_vector_double yObs2, size_t numCoeffs) -> PolyVector3
    """
    return _math_poly.fit(*args)

def FitVectorDouble(x, y, numCoeffs):
    """FitVectorDouble(VectorDouble x, VectorDouble y, size_t numCoeffs) -> Poly1D"""
    return _math_poly.FitVectorDouble(x, y, numCoeffs)
class PolyVector3(_object):
    """Proxy of C++ math::poly::OneD<(Vector3)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolyVector3, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PolyVector3, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        """
        __init__(math::poly::OneD<(Vector3)> self) -> PolyVector3
        __init__(math::poly::OneD<(Vector3)> self, std::vector< math::linear::VectorN< 3,double >,std::allocator< math::linear::VectorN< 3,double > > > const & coef) -> PolyVector3
        __init__(math::poly::OneD<(Vector3)> self, size_t order) -> PolyVector3
        __init__(math::poly::OneD<(Vector3)> self, size_t order, Vector3 coef) -> PolyVector3
        """
        this = _math_poly.new_PolyVector3(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def order(self):
        """order(PolyVector3 self) -> size_t"""
        return _math_poly.PolyVector3_order(self)


    def size(self):
        """size(PolyVector3 self) -> size_t"""
        return _math_poly.PolyVector3_size(self)


    def empty(self):
        """empty(PolyVector3 self) -> bool"""
        return _math_poly.PolyVector3_empty(self)


    def scaleVariable(self, scale):
        """scaleVariable(PolyVector3 self, double scale) -> PolyVector3"""
        return _math_poly.PolyVector3_scaleVariable(self, scale)


    def truncateTo(self, order):
        """truncateTo(PolyVector3 self, size_t order) -> PolyVector3"""
        return _math_poly.PolyVector3_truncateTo(self, order)


    def copyFrom(self, p):
        """copyFrom(PolyVector3 self, PolyVector3 p)"""
        return _math_poly.PolyVector3_copyFrom(self, p)


    def __call__(self, at):
        """__call__(PolyVector3 self, double at) -> Vector3"""
        return _math_poly.PolyVector3___call__(self, at)


    def derivative(self):
        """derivative(PolyVector3 self) -> PolyVector3"""
        return _math_poly.PolyVector3_derivative(self)


    def velocity(self, x):
        """velocity(PolyVector3 self, double x) -> Vector3"""
        return _math_poly.PolyVector3_velocity(self, x)


    def acceleration(self, x):
        """acceleration(PolyVector3 self, double x) -> Vector3"""
        return _math_poly.PolyVector3_acceleration(self, x)


    def __imul__(self, *args):
        """
        __imul__(PolyVector3 self, double cv) -> PolyVector3
        __imul__(PolyVector3 self, PolyVector3 p) -> PolyVector3
        """
        return _math_poly.PolyVector3___imul__(self, *args)


    def __mul__(self, *args):
        """
        __mul__(PolyVector3 self, double cv) -> PolyVector3
        __mul__(PolyVector3 self, PolyVector3 p) -> PolyVector3
        """
        return _math_poly.PolyVector3___mul__(self, *args)


    def __iadd__(self, p):
        """__iadd__(PolyVector3 self, PolyVector3 p) -> PolyVector3"""
        return _math_poly.PolyVector3___iadd__(self, p)


    def __add__(self, p):
        """__add__(PolyVector3 self, PolyVector3 p) -> PolyVector3"""
        return _math_poly.PolyVector3___add__(self, p)


    def __isub__(self, p):
        """__isub__(PolyVector3 self, PolyVector3 p) -> PolyVector3"""
        return _math_poly.PolyVector3___isub__(self, p)


    def __sub__(self, p):
        """__sub__(PolyVector3 self, PolyVector3 p) -> PolyVector3"""
        return _math_poly.PolyVector3___sub__(self, p)


    def __idiv__(self, cv):
        """__idiv__(PolyVector3 self, double cv) -> PolyVector3"""
        return _math_poly.PolyVector3___idiv__(self, cv)


    def __div__(self, cv):
        """__div__(PolyVector3 self, double cv) -> PolyVector3"""
        return _math_poly.PolyVector3___div__(self, cv)


    def __getitem__(self, i):
        """__getitem__(PolyVector3 self, long i) -> Vector3"""
        return _math_poly.PolyVector3___getitem__(self, i)


    def __setitem__(self, i, val):
        """__setitem__(PolyVector3 self, long i, Vector3 val)"""
        return _math_poly.PolyVector3___setitem__(self, i, val)


    def __str__(self):
        """__str__(PolyVector3 self) -> std::string"""
        return _math_poly.PolyVector3___str__(self)


    def __deepcopy__(self, memo):
        """__deepcopy__(PolyVector3 self, PyObject * memo) -> PolyVector3"""
        return _math_poly.PolyVector3___deepcopy__(self, memo)

    __swig_destroy__ = _math_poly.delete_PolyVector3
    __del__ = lambda self: None
PolyVector3_swigregister = _math_poly.PolyVector3_swigregister
PolyVector3_swigregister(PolyVector3)

class StdVectorDouble(_object):
    """Proxy of C++ std::vector<(double)> class"""
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, StdVectorDouble, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, StdVectorDouble, name)
    __repr__ = _swig_repr

    def iterator(self):
        """iterator(StdVectorDouble self) -> SwigPyIterator"""
        return _math_poly.StdVectorDouble_iterator(self)

    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        """__nonzero__(StdVectorDouble self) -> bool"""
        return _math_poly.StdVectorDouble___nonzero__(self)


    def __bool__(self):
        """__bool__(StdVectorDouble self) -> bool"""
        return _math_poly.StdVectorDouble___bool__(self)


    def __len__(self):
        """__len__(StdVectorDouble self) -> std::vector< double >::size_type"""
        return _math_poly.StdVectorDouble___len__(self)


    def pop(self):
        """pop(StdVectorDouble self) -> std::vector< double >::value_type"""
        return _math_poly.StdVectorDouble_pop(self)


    def __getslice__(self, i, j):
        """__getslice__(StdVectorDouble self, std::vector< double >::difference_type i, std::vector< double >::difference_type j) -> std_vector_double"""
        return _math_poly.StdVectorDouble___getslice__(self, i, j)


    def __setslice__(self, *args):
        """
        __setslice__(StdVectorDouble self, std::vector< double >::difference_type i, std::vector< double >::difference_type j, std_vector_double v)
        __setslice__(StdVectorDouble self, std::vector< double >::difference_type i, std::vector< double >::difference_type j)
        """
        return _math_poly.StdVectorDouble___setslice__(self, *args)


    def __delslice__(self, i, j):
        """__delslice__(StdVectorDouble self, std::vector< double >::difference_type i, std::vector< double >::difference_type j)"""
        return _math_poly.StdVectorDouble___delslice__(self, i, j)


    def __delitem__(self, *args):
        """
        __delitem__(StdVectorDouble self, std::vector< double >::difference_type i)
        __delitem__(StdVectorDouble self, PySliceObject * slice)
        """
        return _math_poly.StdVectorDouble___delitem__(self, *args)


    def append(self, x):
        """append(StdVectorDouble self, std::vector< double >::value_type const & x)"""
        return _math_poly.StdVectorDouble_append(self, x)


    def empty(self):
        """empty(StdVectorDouble self) -> bool"""
        return _math_poly.StdVectorDouble_empty(self)


    def size(self):
        """size(StdVectorDouble self) -> std::vector< double >::size_type"""
        return _math_poly.StdVectorDouble_size(self)


    def clear(self):
        """clear(StdVectorDouble self)"""
        return _math_poly.StdVectorDouble_clear(self)


    def swap(self, v):
        """swap(StdVectorDouble self, std_vector_double v)"""
        return _math_poly.StdVectorDouble_swap(self, v)


    def get_allocator(self):
        """get_allocator(StdVectorDouble self) -> std::vector< double >::allocator_type"""
        return _math_poly.StdVectorDouble_get_allocator(self)


    def begin(self):
        """begin(StdVectorDouble self) -> std::vector< double >::iterator"""
        return _math_poly.StdVectorDouble_begin(self)


    def end(self):
        """end(StdVectorDouble self) -> std::vector< double >::iterator"""
        return _math_poly.StdVectorDouble_end(self)


    def rbegin(self):
        """rbegin(StdVectorDouble self) -> std::vector< double >::reverse_iterator"""
        return _math_poly.StdVectorDouble_rbegin(self)


    def rend(self):
        """rend(StdVectorDouble self) -> std::vector< double >::reverse_iterator"""
        return _math_poly.StdVectorDouble_rend(self)


    def pop_back(self):
        """pop_back(StdVectorDouble self)"""
        return _math_poly.StdVectorDouble_pop_back(self)


    def erase(self, *args):
        """
        erase(StdVectorDouble self, std::vector< double >::iterator pos) -> std::vector< double >::iterator
        erase(StdVectorDouble self, std::vector< double >::iterator first, std::vector< double >::iterator last) -> std::vector< double >::iterator
        """
        return _math_poly.StdVectorDouble_erase(self, *args)


    def __init__(self, *args):
        """
        __init__(std::vector<(double)> self) -> StdVectorDouble
        __init__(std::vector<(double)> self, std_vector_double arg2) -> StdVectorDouble
        __init__(std::vector<(double)> self, std::vector< double >::size_type size) -> StdVectorDouble
        __init__(std::vector<(double)> self, std::vector< double >::size_type size, std::vector< double >::value_type const & value) -> StdVectorDouble
        """
        this = _math_poly.new_StdVectorDouble(*args)
        try:
            self.this.append(this)
        except:
            self.this = this

    def push_back(self, x):
        """push_back(StdVectorDouble self, std::vector< double >::value_type const & x)"""
        return _math_poly.StdVectorDouble_push_back(self, x)


    def front(self):
        """front(StdVectorDouble self) -> std::vector< double >::value_type const &"""
        return _math_poly.StdVectorDouble_front(self)


    def back(self):
        """back(StdVectorDouble self) -> std::vector< double >::value_type const &"""
        return _math_poly.StdVectorDouble_back(self)


    def assign(self, n, x):
        """assign(StdVectorDouble self, std::vector< double >::size_type n, std::vector< double >::value_type const & x)"""
        return _math_poly.StdVectorDouble_assign(self, n, x)


    def resize(self, *args):
        """
        resize(StdVectorDouble self, std::vector< double >::size_type new_size)
        resize(StdVectorDouble self, std::vector< double >::size_type new_size, std::vector< double >::value_type const & x)
        """
        return _math_poly.StdVectorDouble_resize(self, *args)


    def insert(self, *args):
        """
        insert(StdVectorDouble self, std::vector< double >::iterator pos, std::vector< double >::value_type const & x) -> std::vector< double >::iterator
        insert(StdVectorDouble self, std::vector< double >::iterator pos, std::vector< double >::size_type n, std::vector< double >::value_type const & x)
        """
        return _math_poly.StdVectorDouble_insert(self, *args)


    def reserve(self, n):
        """reserve(StdVectorDouble self, std::vector< double >::size_type n)"""
        return _math_poly.StdVectorDouble_reserve(self, n)


    def capacity(self):
        """capacity(StdVectorDouble self) -> std::vector< double >::size_type"""
        return _math_poly.StdVectorDouble_capacity(self)


    def __getitem__(self, *args):
        """
        __getitem__(StdVectorDouble self, PySliceObject * slice) -> std_vector_double
        __getitem__(StdVectorDouble self, std::vector< double >::difference_type i) -> std::vector< double >::value_type const
        __getitem__(StdVectorDouble self, long i) -> double
        """
        return _math_poly.StdVectorDouble___getitem__(self, *args)


    def __setitem__(self, *args):
        """
        __setitem__(StdVectorDouble self, PySliceObject * slice, std_vector_double v)
        __setitem__(StdVectorDouble self, PySliceObject * slice)
        __setitem__(StdVectorDouble self, std::vector< double >::difference_type i, std::vector< double >::value_type const & x)
        __setitem__(StdVectorDouble self, long i, double val)
        """
        return _math_poly.StdVectorDouble___setitem__(self, *args)


    def __str__(self):
        """__str__(StdVectorDouble self) -> std::string"""
        return _math_poly.StdVectorDouble___str__(self)

    __swig_destroy__ = _math_poly.delete_StdVectorDouble
    __del__ = lambda self: None
StdVectorDouble_swigregister = _math_poly.StdVectorDouble_swigregister
StdVectorDouble_swigregister(StdVectorDouble)

# This file is compatible with both classic and new-style classes.


