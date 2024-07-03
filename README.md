## Generate LateX documents with python

Python module for generating simple LaTeX documents in your Python scripts.


## External dependencies

This package requires a working installation of pdflatex with the graphicx, subcaption, booktabs, geometry, placeins, pdflscape packages.

## Code Formatting

The code in this repository follows the formatting guidelines set by the Black code formatter (https://github.com/psf/black). Pull requests are required to comply with these formatting guidelines.

## Testing

The unit tests just check if the correct text has been added to the .tex file. Currently there is no testing of the compiled output.


## Installation

Clone this github repo ```git clone https://github.com/tomcarron/LatexDoc.git``` \
Navigate to the directory LatexDoc. \
```pip install --upgrade pip``` \
```pip install .```

## Usage
import to python:

from LatexDoc import LaTeXDocument

see example.py for further details on usage.

