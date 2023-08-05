Cython for All with GitHub Actions
==================================


Is Python interpreted or compiled?
----------------------------------


c2f.py
------

.. code-block:: python

   # cython: language_level=3
   "Celsius to Fahrenheit Library"

   def convert(celsius: float) -> float:
       "Convert Celsius to Fahrenheit"
       fahrenheit = celsius * 1.8 + 32
       return fahrenheit


setup.py
--------

  $ python setup.py sdist

.. code-block:: python

   from setuptools import setup
   from Cython.Build import cythonize

   setup(
       name='c2f',
       version='0.0.0',
       py_modules=['c2f'],
       ext_modules=cythonize('c2f.py'),
   )


c2f.cpython-38.pyc
------------------

.. code-block:: pycon

   >>> dis.dis(c2f.convert)
     6           0 LOAD_FAST                0 (celsius)
                 2 LOAD_CONST               1 (1.8)
                 4 BINARY_MULTIPLY
                 6 LOAD_CONST               2 (32)
                 8 BINARY_ADD
                10 STORE_FAST               1 (fahrenheit)
     7          12 LOAD_FAST                1 (fahrenheit)
                14 RETURN_VALUE


github.com/python/cpython/blob/master/Python/ceval.c
----------------------------------------------------

.. code-block:: c

   case TARGET(BINARY_MULTIPLY): {
       PyObject *right = POP();
       PyObject *left = TOP();
       PyObject *res = PyNumber_Multiply(left, right);
       Py_DECREF(left);
       Py_DECREF(right);
       SET_TOP(res);
       if (res == NULL)
           goto error;
       DISPATCH();
   }


c2f.c
-----

  $ cython c2f.py

.. code-block:: c

   static PyObject * __pyx_pf_3c2f_convert(double __pyx_v_celsius) {
     double __pyx_v_fahrenheit;
     PyObject *__pyx_r = NULL;
     __pyx_v_fahrenheit = ((__pyx_v_celsius * 1.8) + 32.0);
     __pyx_r = PyFloat_FromDouble(__pyx_v_fahrenheit);
     return __pyx_r;
   }


c2f.so
------

  $ pip install wheel
  $ python setup.py bdist_wheel

  $ gcc -g -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I/Library/Frameworks/Python.framework/Versions/3.8/include/python3.8 -L/Library/Frameworks/Python.framework/Versions/3.8/lib -o c2f.so c2f.c -lpython3.8
  $ objdump -S -df=___pyx_pw_3c2f_1convert c2f.so

.. code-block:: nasm

   ___pyx_pw_3c2f_1convert:
   push	  rbp
   mov	  rbp, rsp
   sub	  rsp, 16
   movsd  xmm0, qword ptr [rbp - 8]
   mulsd  xmm0, qword ptr [rip + 1379]
   addsd  xmm0, qword ptr [rip + 1379]
   call	  502 <PyFloat_FromDouble ...>
   add	  rsp, 16
   pop	  rbp
   ret


GitHub Workflow
---------------


Future
------

Check out https://github.com/grantjenks/python-runstats for a more complete example.
