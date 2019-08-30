try:
    from Cython.Build import cythonize,build_ext
except:
    raise ImportError("You must have cython installed in order to use mkp!") 

import os
import numpy as np
from distutils.core import setup, Extension


ext_modules = []
ext_modules += cythonize(Extension(
    "mkp._algorithms_cy.mtm_cy", 
    sources=["cpp/mtm_c.cpp","python/mkp/_algorithms_cy/mtm_cy.pyx"], 
    include_dirs=['cpp/'],
    language='c++',
    extra_compile_args=["-std=c++1y"]))

extentions_info = [
    {
        "cython_sourcefile": "python/mkp/_algorithms_cy/mthm.pyx"
    }
]

include_path = [np.get_include(), 'cpp']

for extention_info in extentions_info:
    sourcefiles = extention_info.get("cpp_sourcefiles", [])
    cython_sourcefile = extention_info.get("cython_sourcefile")
    sourcefiles += [cython_sourcefile]
    
    # NOTE: extension name must match .pyx file name
    extension_name = cython_sourcefile.replace('.pyx', '').replace(os.sep, '.')
    ext_modules += cythonize(Extension(
                                extension_name,
                                sources=sourcefiles,
                                include_dirs=include_path,
                                language='c++',
                                extra_compile_args=["-std=c++1y"]))


setup(name='mkp',
      version='1.0',
      description='Algorithms for Multiple Knapsack Problem (MKP)',
      author='Jesse Myrberg',
      author_email='jesse.myrberg@gmail.com',
      url='https://github.com/jmyrberg/mkp',
      license='MIT',
      packages=['mkp','mkp._algorithms_cy'],
      package_dir={
          'mkp': 'python/mkp',
      },
      ext_modules=ext_modules,
      install_requires=['numpy'],
      include_dirs=[np.get_include(), 'cpp'])

