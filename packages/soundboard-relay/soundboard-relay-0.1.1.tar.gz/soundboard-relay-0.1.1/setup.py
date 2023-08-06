from setuptools import setup

setup(
    name='soundboard-relay',
    version="0.1.1",
    packages=['soundboard_relay'],
    include_package_data=True,
    install_requires=[
        'paho-mqtt',
        'python-mpd2',
    ],
    entry_points={
        'console_scripts': [
            'soundboard-relay=soundboard_relay.__main__:main'
        ]
    }
)
