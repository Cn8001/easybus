from setuptools import setup

setup(setup_requires=["pbr"],pbr=True, #Enable pbr for autoconf of git and documentation
      packages=['easybus'],
      entry_points={
          'console_scripts' : [
              'easybus =  easybus.main:main'
            ]
        },
      install_requires=['uvicorn','fastapi','selenium','bs4','python-dateutil','get_gecko_driver']
)