# shex_to_shexj

[![Pyversions](https://img.shields.io/pypi/pyversions/shex_to_shexj.svg)](https://pypi.python.org/pypi/shex_to_shexj)

[![PyPi](https://img.shields.io/pypi/v/shex_to_shexj.svg)](https://pypi.python.org/pypi/shex_to_shexj)


ShExC to ShExJ conversion utility.  Convert the ShEx compact syntax (ShExC) to the ShEx JSON syntax (ShExJ). This
conversion is useful for:
* Tools that do processing directly on the ShEx AST
* Large ShEx files that may take a while to compile (although another solution would be to enhance the compiler 
itself...)

## Installation
`pipenv install shex_to_shexj`

## Usage
`pipenv run shex_to_shexj`

```
usage: shex_to_shexj [-h] [-i [INFILE [INFILE ...]]] [-id INDIR]
                              [-o [OUTFILE [OUTFILE ...]]] [-od OUTDIR] [-f]
                              [-s]

ShEx to ShExJ converter

optional arguments:
  -h, --help            show this help message and exit
  -i [INFILE [INFILE ...]], --infile [INFILE [INFILE ...]]
                        Input file(s)
  -id INDIR, --indir INDIR
                        Input directory
  -o [OUTFILE [OUTFILE ...]], --outfile [OUTFILE [OUTFILE ...]]
                        Output file(s)
  -od OUTDIR, --outdir OUTDIR
                        Output directory
  -f, --flatten         Flatten output directory
  -s, --stoponerror     Stop on processing error

```

