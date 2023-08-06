from setuptools import setup, find_packages
 
setup(name='arimafd',
      version='0.2',
      url='https://github.com/waico/arimafd',
      license='MIT',
      packages=find_packages(),
      author='Vyacheslav Kozitsin, Yuri Katser',
      author_email='waico@waico.ru',
      description='Build librarry',
      #packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      long_description_content_type='text/x-rst',
      zip_safe=False)