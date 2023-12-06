from setuptools import find_packages, setup

setup(
  name = 'pypicalculator',
  packages = find_packages(),
  include_package_data=True,
  version = '0.1',
  license='MIT',
  description = 'Simple Arithmetic Calculator',
  author = 'Yash Dhakade',
  author_email = 'yinsights8@gmail.com',
 # url = 'https://github.com/yinsights8/SimpleCalculator',
 # download_url = 'https://github.com/sourangshupal/pyarithcalc/releases/download/0.5/pyarithcalc-0.5.tar.gz',
  keywords = ['calculator'],
  install_requires=[
          'flask',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish
    'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  entry_points={
        "console_scripts": [
            "calc = pypicalculator.app:start_app",
        ]},
)
