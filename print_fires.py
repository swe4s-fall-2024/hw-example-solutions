from pathlib import Path

from utils import get_rows_by_column_value

country = "United States of America"
country_column_index = 0
file_path = Path("./Agrofood_co2_emission.csv")
savanna_emissions_colm = 2

usa_rows = get_rows_by_column_value(
    file_path=file_path, column_value=country, column_index=country_column_index
)

savanna_emissions = [float(row[savanna_emissions_colm]) for row in usa_rows]
# To SWE4S folks:
#   The above line uses "list comprehension" which is
#   is a concise way to create a new list by applying an expression to each element of an
#   existing iterable, optionally including a conditional filter
#   the expression.
#   You could alternatively have used a more conventional for loop but the above is more concise
#   and, once you get used to the syntax, just as clear

print(
    f"In the {file_path.stem} dataset, the total emissions from savanna fires in {country} is {sum(savanna_emissions)}."
)
