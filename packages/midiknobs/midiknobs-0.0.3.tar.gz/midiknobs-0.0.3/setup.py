from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="midiknobs",
    description="A small pyqt5 gui to use midi knobs for change linux master audio",
    version="0.0.3",
    python_requires='>=3.5',
    long_description=long_description,
    install_requires=["python-rtmidi", "mido", "vext.pyqt5", "PyQt5"],
    packages=find_packages(),
    entry_points={
        'console_scripts': ['midiknobs_gui=midiknobs.__main__:main'],
    },
    project_urls={
        'Source': 'https://github.com/nicolalandro/midi_kbobs',
    },
)
