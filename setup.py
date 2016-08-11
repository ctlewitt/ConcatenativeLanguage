from setuptools import setup

config = {
    'description': "Concatenative Language Interpreter for Don't Answer",
    'author': 'Charley Lewittes',
    'url': 'https://github.com/ctlewitt/ConcatenativeLanguage',
    'download_url': 'https://github.com/ctlewitt/ConcatenativeLanguage',
    'author_email': 'ctlewitt@gmail.com',
    'version': '0.1',
    'packages': ['concatenative_language', 'concatenative_language.functions', 'concatenative_language.functions.native'],
    'name': "dontanswer",
    'entry_points': {'console_scripts': ['dont-answer=concatenative_language.runner:main']}
}

setup(**config)