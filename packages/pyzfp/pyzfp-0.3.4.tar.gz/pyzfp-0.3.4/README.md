# pyzfp
Python wrapper over the [zfp compression library](https://computation.llnl.gov/projects/floating-point-compression). This is the second version, rewritten using Cython because the earlier version using ctypes was slow. [Click here](https://github.com/navjotk/pyzfp/blob/ctypes_vs_cython/ctypes_vs_cython_compression.png) for performance comparison. Currently wraps zfp version 0.5.5. 

# Installation
```
pip install pyzfp
```
This should download zfp version 0.5.5, compile it and install the python (Cython) wrappers in the default install location. The use of a virtual environment is recommended.

Should you face any issues, please report them using Github issues. 

# Usage

A sample program that demonstrates the use of the library: (also contents of test.py):
```
from pyzfp import compress, decompress


a = np.linspace(0, 100, num=1000000).reshape((100, 100, 100))



tolerance = 0.0000001
parallel = True
compressed = compress(a, tolerance=tolerance, parallel=parallel)

recovered = decompress(compressed, a.shape, a.dtype, tolerance=tolerance)
print(len(a.tostring()))
print(len(compressed))
print(np.linalg.norm(recovered-a))
```

