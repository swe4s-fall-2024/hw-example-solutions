def get_rows_by_column_value(file_path, column_value, column_index=0):
    # In CSV, get all the rows where row[column_index] == column_value
    with open(file_path, "r") as file:
        matching_rows = []
        for line in file:
            row = line.split(",")
            if row[column_index] == column_value:
                matching_rows.append(row)

        return matching_rows
