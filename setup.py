from setuptools import setup, find_packages

setup(
    name = "text_to_baby_talk_fedtti",
    version = "0.1.0",
    description = "",
    packages = find_packages(where="src"),
    package_dir={"": "src"},
    entry_points = {
        "console_scripts": [
            "text-to-baby-talk = text_to_baby_talk_fedtti.__main__:main"
        ]
    }
)
