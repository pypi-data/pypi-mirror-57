from setuptools import Extension, find_packages, setup

from Cython.Build import cythonize

extensions = [
    Extension(
        name="_jopus_cython",
        sources=["jopus/jopus.pyx"],
        libraries=["opusfile", "opus", "ogg", "opusurl"],
        library_dirs=["/usr/local/lib"],
        include_dirs=[
            "/usr/include/opus",
            "/usr/local/include/opus",
            "/usr/local/include",
        ],
        language="c++",
    )
]

setup(
    name="jopus",
    version="0.0.2",
    packages=find_packages(),
    description="Simple Python wrapper for libopusfile",
    ext_modules=cythonize(extensions, force=True),
    python_requires=">=3.6.0",
    author="Dmitry Yutkin",
    url='https://github.com/yutkin/jopus',
    license="MIT",
    zip_safe=True,
    install_requires=["numpy"],  # Any version of numpy is OK
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Programming Language :: C++",
    ],
)
