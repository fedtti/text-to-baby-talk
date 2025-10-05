from setuptools import setup

setup(
    name = 'text_to_baby_talk_fedtti',
    version = '0.0.1',
    packages = ['text_to_baby_talk_fedtti'],
    entry_points = {
        'console_scripts': [
            'text_to_baby_talk_fedtti = text_to_baby_talk_fedtti.__main__:main'
        ]
    }
)
