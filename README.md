# HW 3

## Usage

Given the [`Agri-food CO2 emission dataset`](https://www.kaggle.com/datasets/alessandrolobello/agri-food-co2-emission-dataset-forecasting-ml), this repo provides scripts to compute and print the total emissions from a given column for a given country.
There are two entrypoints:

- a Python script, `print_fires.py`, and
- a bash script, `run.sh`, that simply runs `print_fires.py`

For usage information, run `python print_fires.py -h` or `./run.sh -h`, respectively. 
If you choose to use `run.sh`, make sure that both `run.sh` and `print_fires.py` are in your current working directory.  

### Example usage

Both

```bash
./run.sh -c "United States of America" -i 0 -e 2 -f path/to/Agrofood_co2_emission.csv
```

and 

```bash
python print_fires.py --file_path path/to/Agrofood_co2_emission.csv \
	--country "United States of America" \
    --country_column 0 \
    --emissions_column 2
```

should print the the total emissions from savanna fires in the USA. 

## Changelog

### v2.0.0

- Changes to `print_fires.py`:
    - Added command line argument parsing
    - Rather than having the country, country column, emissions column, and file path hardcoded, its behavior is now more customizable. For more information, see the [usage](#usage) section
- Added bash script `run.sh`

### v1.0.0

- Added `print_fires.py`