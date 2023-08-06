estnltk-1.4-light
=================

Estnltk-1.4-light is a heavily stripped-down version of [estnltk 1.4](https://github.com/estnltk/estnltk/tree/eef59a766005fd082d486816d3f221b4c4f3d632) which only includes core instruments for text tokenization and morphological analysis including lemmatization.


## Installation

Estnltk-1.4-light was tested on Ubuntu 18.04 with Python 2.7 and 3.6, but is very likely to work with other OS/python types as well.


Installing from PyPi:

    pip install estnltk-1.4-light

Installing from source:

    rm -rf ./build ./dist ./estnltk/vabamorf/vabamorf.py ./estnltk/vabamorf/vabamorf_wrap.cpp
    pip install -r requirements.txt
    python setup.py build 
    python setup.py install

Post-installation check:

    python -m estnltk.run_tests
    python -c "from estnltk import Text; print(Text('Täna on hea päev').get.lemmas.postags.as_zip)"
    

## License

GNU General Public License, version 2
