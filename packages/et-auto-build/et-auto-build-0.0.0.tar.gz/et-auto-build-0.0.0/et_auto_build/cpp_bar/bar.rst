This file documents a python module built from C++ code with pybind11.
You should document the Python interfaces, *NOT* the C++ interfaces.

Module et_auto_build.bar
*********************************************************************

Module :py:mod:`bar` built from C++ code in :file:`cpp_bar/bar.cpp`.

.. function:: add(x,y,z)
   :module: et_auto_build.bar
   
   Compute the sum of *x* and *y* and store the result in *z* (overwrite).

   :param x: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param y: 1D Numpy array with ``dtype=numpy.float64`` (input)
   :param z: 1D Numpy array with ``dtype=numpy.float64`` (output)
   