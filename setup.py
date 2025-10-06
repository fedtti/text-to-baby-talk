from setuptools import setup, find_packages

setup(
    name = "text_to_baby_talk_fedtti",
    version = "0.1.0",
    description = "",
    author = "Federico Moretti",
    author_email = "hello@federicomoretti.it",
    classifiers = [
      "Development Status :: 3 - Alpha",
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python :: 3.9",
    ],
    package_dir = { "": "src" },
    packages = find_packages(where = "src"),
    entry_points = {
        "console_scripts": [
            "text-to-baby-talk = text_to_baby_talk_fedtti.__main__:main"
        ]
    }
)
