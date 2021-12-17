# in progress
from setuptools import setup
from Cython.Build import cythonize
from Cython.Distutils import build_ext

setup(
    name='autosign',
    # Include additional files into the package using MANIFEST.in
    include_package_data=True,
    app=['main.py'],
    data_files=[],
    cmdclass={'build_ext': build_ext},
    ext_modules=cythonize(["main.py",], language_level=3),

    setup_requires=['py2app'],
    options={
        'cython': {"language_level": "3"}
    },
    install_requires=[
        "Cython"
    ],
    entry_points={
        "console_scripts": [
            "testLoad = __main__:main"
        ]
    },
)
