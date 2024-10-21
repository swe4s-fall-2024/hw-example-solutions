# Agri-food C02 emissions analysis

- [Agri-food C02 emissions analysis](#agri-food-c02-emissions-analysis)
  - [Introduction](#introduction)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Example](#example)
  - [Changelog](#changelog)
    - [v2.1.0](#v210)
    - [v2.0.0](#v200)
    - [v1.0.0](#v100)
  - [Some notes for SWE4S students](#some-notes-for-swe4s-students)
    - [README.md](#readmemd)
    - [utils.py](#utilspy)

## Introduction 

This repo contains a Python script and a bash script to assist in analyses of the [Agri-food CO2 emission Kaggle dataset](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml).

Given a country and emissions column, both the Python and bash script will compute the user-chosen sum, mean, median, or mode of the Agri-food data corresponding to the chosen country and emissions column.
Using these scripts, users can explore things like how the emissions of differenty types compare across countries.

## Installation

This project depends on the dependencies listed in `environment.yaml`. 
To create an suitable environment using `conda`, run `conda env create -f environment.yaml` and activate the created environment.

## Usage

There are two scripts that do the same thing.
If you are more comfortable with Python, use the Python script `print_fires.py`
If you are more comfortable with Bash, use the Bash script `run.sh`

For usage information, run `python print_fires.py -h` or `./run.sh -h`, respectively. 
If you choose to use `run.sh`, make sure that both `run.sh` and `print_fires.py` are in your current working directory.  

### Example 

Both

```bash
./run.sh -c "United States of America" \
  -i 0 -e 2 -f ./Agrofood_co2_emission.csv -o "sum"
```

and 

```bash
python print_fires.py --file_path ./Agrofood_co2_emission.csv \
	--country "United States of America" \
    --country_column 0 \
    --emissions_column 2 \
    --operation "sum"
```

should print the the total (i.e., "sum" of) emissions from savanna fires in the USA. 

## Changelog

### v2.1.0

The version went from v2.0.0 to v2.1.0 because I added functionality in a backward compatible manner.

- Both `print_fires.py` and `run.sh` now allow users to choose the operation they want to perform: sum, mean, median, or standard deviation

### v2.0.0

- `print_fires.py` 
    - Added command line argument parsing
    - Rather than having the country, country column, emissions column, and file path hardcoded, its behavior is now more customizable. For more information, see the [usage](#usage) section
- Added bash script `run.sh`

### v1.0.0

- Added `print_fires.py`


## Some notes for SWE4S students

### README.md 

- Each sentence should be on a new line so that PR review feedback can be sentence-by-sentence specific
- README is for information that's relevant to a user of your software.
Hence it's probably nice to tell the user:    
  1. what your software does, 
  2. what the dependency and installation details for your software are
  3. how to use your software with examples
  4. a changelog to describe what changed between versions 
  5. anything else you think a user needs to know


### utils.py

- There are several functions without docstrings. 
IMO because the functions with no docstrings are simple enough and their function signatures are clear enough, that no further documentation is needed.
- The `compute_*` functions don't just call a functions (like `numpy.median` for the median) that will compute what we want because this is homework and I want you to practice writing code. 
If you wanted to compute a sum or mean or standard deviation, in a non-homework codebase than you should just use a already existing functions that do what you want (e.g., `numpy.median`) and not write a new function.
