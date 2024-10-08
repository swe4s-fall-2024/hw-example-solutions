#!/bin/bash

# Help message
function display_help {
    echo
    echo "Usage: ./run.sh [-c|i|e|f|o]"
    echo
    echo "Options:"
    echo "  -c  Name of the country"
    echo "  -i  Index of country column"
    echo "  -e  Index of emissions column"
    echo "  -f  Path to Agrofood_co2_emission.csv"
    echo "  -o  Operation to perform. Options: sum, mean, median,"
    echo "  -h  Display this help message"
    echo
    exit 1
}

# Parse command line arguments
OPERATION="sum" # default value
while getopts "c:i:e:f:o:h" opt; do
    case ${opt} in
        c) COUNTRY=$OPTARG ;;
        i) COUNTRY_COLUMN=$OPTARG ;;
        e) EMISSIONS_COLUMN=$OPTARG ;;
        f) FILE_PATH=$OPTARG ;;
        o) OPERATION=$OPTARG ;;
        h) display_help ;;
        *) echo "Unknown parameter passed: $0"; display_help ;;
    esac
done

# Make sure required arguments have been set
if [[ -z "$COUNTRY" || -z "$COUNTRY_COLUMN" || -z "$EMISSIONS_COLUMN" || -z "$FILE_PATH" ]]; then
        echo "Error: -c, -i, -e, and -f, arguments are required"
        echo "Help message:"
        display_help
fi

python print_fires.py --file_path "$FILE_PATH" --country "$COUNTRY" --country_column "$COUNTRY_COLUMN" --emissions_column "$EMISSIONS_COLUMN" --operation "$OPERATION"
