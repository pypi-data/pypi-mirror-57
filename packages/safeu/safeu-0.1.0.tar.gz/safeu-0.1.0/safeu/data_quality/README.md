#   data_quality

### Self-generated slp_tools dependency package

We use cython to write some code. For Windows and Linux platforms,we give both 3.6 and 3.7 python versions of the dependency package.

At the same time, you can generate a package that depends on the current python in the current directory via **python setup.py build_ext --inplace**.

-   At this point you need to modify the dependency path in slp.py to ensure the correctness of the call.
-	Of course, this depends on the vs compiler that has been installed under the Windows platform; the gnu environment needs to be provided under the Linux platform.
-	Compiling also requires a cython environment, so if you install anaconda, it will be much smoother.