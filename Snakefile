# Define input data and output files
data_file = "Agrofood_co2_emission.csv"
countries = ["China", "Canada", "Australia"]

# Define the output for heatmap and scatter plots
heatmap_output = "plot_outputs/urban_proportions_heatmap.png"
scatter_plots = expand("plot_outputs/{country}_fires_vs_urban.png", country=countries)

# Rule to run the plot.py script and produce all figures
rule generate_all_figures:
    input:
        data_file = data_file
    output:
        heatmap_output,
        scatter_plots
    params:
        country_list = " ".join([f'"{c}"' for c in countries])
    shell:
        """
        python3 plots.py -l {params.country_list} -n 0 -y 1 -r 25 -u 26 -t 3 -f {input.data_file}
        """

# Rule to ensure all figures are produced
rule all:
    input:
        heatmap_output,
        scatter_plots
