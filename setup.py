
from setuptools import setup, find_packages

setup(
    name='iot_env_monitoring',
    version='1.0.0',
    description='IoT and Satellite Enabled Environmental Monitoring System',
    author='rfc391',
    author_email='robshubert96@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'flask',
        'requests',
        'protobuf',
        'python-dotenv',
        'pyserial',
        'pytest',
        'gunicorn'
    ],
    entry_points={
        'console_scripts': [
            'iot-monitor=cli:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
