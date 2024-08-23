import pandas as pd

# Load the Excel file
df = pd.read_excel("new_data/extracted_tables_new.xlsx")

# Transpose the DataFrame without the word 'resultater'
df_transposed = df.set_index('your column').T
df_transposed.index.name = None

# Save the transposed DataFrame to a new Excel file
df_transposed.to_excel("new_data/transposed_results_no_resultater.xlsx", index=False)

# Print a success message
print("The new Excel file 'transposed_results_no_resultater.xlsx' has been created successfully.")

