from setuptools import setup

setup(name='chinese_name_similarity',
      version='0.1',
      description='Calculate similarity between chinese names',
      url='http://github.com/jasminehung/chinese_name_similarity', 
      download_url = 'https://github.com/jasminehung/chinese_name_similarity/archive/v0.1-beta.tar.gz',  
      author='Jasmine Hung',
      author_email='jasmine_sg27@yahoo.com.tw',
      license='MIT',
      packages=['chinese_name_similarity'],
      keywords = ['CHINESE', 'NAME', 'SIMILARITY'],   
      install_requires=['python-Levenshtein','opencc-python-reimplemented'],
      zip_safe=False)
