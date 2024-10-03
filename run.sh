#!/bin/bash

pwd

# Function to display the help message
show_help() {
    echo "Given the the Agrofood_co2_emission.csv, a country, and an emissions column," \
    "this script prints the total emissions in the country."
    echo
    echo "Usage: ./run.sh [-c|i|e|f]"
    echo
    echo "Options:"
    echo "  -c  Name of the country"
    echo "  -i  Index of country column"
    echo "  -e  Index of emissions column"
    echo "  -f  Path to Agrofood_co2_emission.csv"
    echo "  -h  Display this help message"
}

# Parse command line arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -c) COUNTRY="$2"; shift ;;
        -i) COUNTRY_COLM="$2"; shift ;;
        -e) EMISSION_COLM="$2"; shift ;;
        -f) FILE_PATH="$2"; shift ;;
        -h) show_help ;;   # Display help and exit
        *) echo "Unknown parameter passed: $1"; show_help ;;
    esac
    shift
done

# Check if required arguments are set
if [[ -z "$COUNTRY" || -z "$COUNTRY_COLM" || -z "$EMISSION_COLM" || -z "$FILE_PATH" ]]; then
    echo "Error: -c, -i, -e, and -f arguments are required"
    echo "Help message:"
    show_help
fi

python print_fires.py --country "$COUNTRY" --country_column $COUNTRY_COLM --emissions_column $EMISSION_COLM --file_path "$FILE_PATH"