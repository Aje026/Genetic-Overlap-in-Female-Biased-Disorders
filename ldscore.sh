#!/bin/bash

# Full path to ldsc.py script
LDSC_SCRIPT="./ldsc.py"

# Get a list of files in the 'munged' folder
files=(munged/*.sumstats.gz)

# Loop through each file in 'munged' while there are more than two files left
while [ ${#files[@]} -gt 1 ]; do
    # Construct --rg argument by joining files with commas
    rg_argument=$(IFS=,; echo "${files[*]}")

    # Define the output name
    output_name=${#files[@]}

    # Run ldsc.py with the full path
    $LDSC_SCRIPT --rg $rg_argument --ref-ld-chr LDscore/ --w-ld-chr LDscore/ --out $output_name

    # Move the first file to the 'moved_files' folder after the LDSC call
    mv "${files[0]}" munged/moved_files/

    # Remove the first file from the list
    files=("${files[@]:1}")