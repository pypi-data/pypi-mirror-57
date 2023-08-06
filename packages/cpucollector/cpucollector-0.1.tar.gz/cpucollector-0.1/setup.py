from setuptools import setup, find_packages

setup(name='cpucollector',
      version='0.1',
      description='CPU information system',
      keywords='cpu',
      url='https://github.com/dikopylov/cpu-collector',
      author="Dmitry Kopylov",
      author_email="dikopylov10@gmail.com",
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'flask',
          'flask-sqlalchemy',
          'flask-script',
          'flask-injector',
          'requests',
          'psutil',
          'schedule',
      ],
      include_package_data=True,
      zip_safe=False)
