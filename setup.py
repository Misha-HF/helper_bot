from setuptools import setup, find_namespace_packages

setup(name='helper_bot',
      version='1',
      description='Helper description',
      url= 'https://github.com/Misha-HF/helper_bot',
      author='Goit team',
      author_email='test@test.com ',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['helper_bot = helper_bot.main:main']},
      install_requires=['prompt_toolkit'])
