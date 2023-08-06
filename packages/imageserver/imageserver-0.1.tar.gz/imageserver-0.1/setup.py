import setuptools

setuptools.setup(name='imageserver',
      version='0.1',
      description='Host thumbnails of images on a remote machine',
      author='Nidhi',
      url='',
      author_email='chandranidhi45@gmail.com',
      license='MIT',
      zip_safe=False,
      packages=setuptools.find_packages(),
    install_requires=[
        'docopt',
        'flask',
        'pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'imageserver = imageserver.server:main',
        ],
        })
