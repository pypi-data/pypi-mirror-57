from setuptools import find_packages, setup

requirements = ['aiohttp',
                'aiohttp_debugtoolbar',
                'aiohttp_jinja2',
                'psutil',
                'pytest',
                'pytest-xdist',
                'pytest-asyncio',
                'python-dateutil',
                'gevent',
                'parse',
                'simplejson',
                'tinydb',
                'matplotlib',
                'pandas']

with open('VERSION') as version_file:
    version = version_file.read()

with open('README.md') as readme_file:
    long_description = readme_file.read()

setup(name='arps',
      python_requires='>3.7.0',
      version=version,
      description=('Multi-Agent System (MAS) Framework for managing resource;'
                   'It also providers a discrete event simulator component to evaluate agents before deploying them'),
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://gitlab.com/arps/arps',
      license='MIT',
      author='Thiago Coelho Prado',
      author_email='coelhudo@gmail.com',
      packages=find_packages(exclude=['*tests*']),
      install_requires=requirements,
      platforms='any',
      entry_points='''
      [console_scripts]
      agents_directory=arps.apps.agents_directory:main
      agent_manager_runner=arps.apps.agent_manager_runner:main
      agent_runner=arps.apps.agent_runner:main
      pmt_service=arps.apps.policy.main:main
      sim_result_to_image=arps.apps.event_log_parser:main
      agent_client=arps.apps.client:main
      ''',
      include_package_data=True,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.7'
      ]
      )
