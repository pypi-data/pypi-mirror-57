from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setup(name='ExploriPy',
      version='1.1.2',
      description='Pre-Modelling Analysis of the data by doing various exploratory data analysis and Statistical Test',
      url='https://github.com/exploripy/exploripy',
      author="Sajan Kumar Bhagat, Kunjithapatham Sivakumar, Shashank Shekhar",
	  author_email='bhagat.sajan0073@gmail.com, s.vibish@gmail.com, quintshekhar@gmail.com',
	  maintainer="Sajan Kumar Bhagat, Kunjithapatham Sivakumar, Shashank Shekhar",
	  maintainer_email='bhagat.sajan0073@gmail.com, s.vibish@gmail.com, quintshekhar@gmail.com',
	  long_description=long_description,
      long_description_content_type="text/markdown",
      license='MIT',
      packages=['ExploriPy'],
      install_requires=[
          'pandas',
          'numpy',
          'Jinja2',
          'scipy',
          'seaborn',
          'matplotlib',
          'statsmodels',
          'sklearn',
		  'tqdm'
      ],
      include_package_data=True,
      zip_safe=False)
