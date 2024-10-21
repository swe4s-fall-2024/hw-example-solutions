# Data Visualization Using matplotlib

## Introduction

This report covers how you can use matplotlib to visualize data using plot maps. This repository uses `plots.py` to process emissions data from three different countries, in this case China, Canada, and Australia. The script generates both a heatmaps of urban population proportions over time and scatter plots for each country comparing urban population proportions with forest fire occurrences. These plots can be seen below. Using these plots, you can visualize the relationship between the urban population proportions and forest fires across time for specified countries.

## Methods

1. **Script Design**:
   The `plots.py` script was developed to process emissions data and generate visualizations. It uses the `argparse` library to handle user-specified command-line arguments for input CSV file path, country selection, and column indices for key data such as population and forest fire occurrences.

   *Credit to Maddy Pernat for supplying the base for this example solution!*

2. **Data Extraction**:
   For each specified country, the script reads the CSV file, extracts the relevant rows and columns (urban population, rural population, and forest fire data), and processes the data using pandas. The urban population proportion is calculated as the urban population divided by the total population (urban + rural).

3. **Visualization**:
   The script generates two types of visualizations:
   - A **heatmap** of urban population proportions over time, showing trends for each country. This visualization was created using `seaborn` and saved as a PNG file.
   - **Scatter plots** comparing urban population proportions and forest fires for each country. These visualizations were created using `matplotlib` and saved as PNG files.

4. **Execution**:
   The script was run with command-line arguments specifying the countries (United States, China, Canada, and Australia), CSV file path, and relevant columns for data extraction and plotting. The output figures were saved in the `plot_outputs/` directory.

## Results

Using `plots.py`, I generated visualizations for four countries: the United States, Canada, Australia, and China. The following figures demonstrate key findings from the analysis:

- **Figure 1** shows a heatmap of urban population proportions over the years 1990–2020 for the selected countries. The heatmap reveals trends in urbanization, with increasing urbanization over time in all countries, but most significantly in China.
  
- **Figures 2-4** are scatter plots for each country comparing urban population proportions against forest fires. There does not appear to be a trend between these two things.

**Figure 1**: Urban Population Proportions (Heatmap)  
![Urban Population Proportions Heatmap](plot_outputs\urban_proportions_heatmap.png)

**Figure 2**: Forest Fires vs Urban Proportions (China)  
![Forest Fires vs Urban Proportions USA](plot_outputs\China_fires_vs_urban.png)

**Figure 3**: Forest Fires vs Urban Proportions (Australia)  
![Forest Fires vs Urban Proportions USA](plot_outputs\Australia_fires_vs_urban.png)

**Figure 4**: Forest Fires vs Urban Proportions (Canada)  
![Forest Fires vs Urban Proportions USA](plot_outputs\Canada_fires_vs_urban.png)

