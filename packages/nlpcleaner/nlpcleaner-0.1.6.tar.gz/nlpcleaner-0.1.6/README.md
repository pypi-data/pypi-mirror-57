# Nlpcleaner
Clean and prepare text for modeling with machine learning.
- lower all
- strip all
- remove numbers
- remove symbols
- remove stopwords by detected language
- lemming or stemming

## Usage

```
from nlpcleaner import Text
Text(txt).clean()
```

## Tests

```
pip install .
python setup.py test
```

## Push on PyPi

```
python setup.py sdist
pip install twine
twine upload dist/*
```
