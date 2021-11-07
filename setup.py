import whid
from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=whid.__title__,
    version=whid.__version__,
    description=whid.__description__,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=whid.__url__,
    author=whid.__author__,
    author_email=whid.__author_email__,
    license=whid.__license__,
    packages=['whid'],
    entry_points={
        'console_scripts': [
            'whid = whid.__main__:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities'
    ],
    keywords='whid what have i done',
    install_requires=[
        'pyautogui',
        'moviepy',
        'argparse',
        'plyer',
        'tqdm',
    ],
    python_requires='>=3.6'
)