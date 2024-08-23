import pandas as pd

def transform_excel_data(input_excel_path, output_excel_path):
    # Load the Excel file, assuming data is in the first sheet
    # If multiple sheets contain relevant data, you might need to adjust this
    df = pd.read_excel(input_excel_path, sheet_name=0)
    
    # Check if the DataFrame has the expected columns
    if 'Parameter' in df.columns and 'Resultat' in df.columns:
        # Pivot the DataFrame so that each parameter becomes a column
        transformed_df = df.pivot_table(index=[df.index], columns='Parameter', values='Resultat', aggfunc='first')
        
        # Reset the index to clean up the DataFrame
        transformed_df.reset_index(drop=True, inplace=True)
        
        # Save the transformed DataFrame to a new Excel file
        transformed_df.to_excel(output_excel_path, index=False)
        print(f"Transformed data saved to Excel at {output_excel_path}")
    else:
        print("The required columns 'Parameter' and 'Resultat' are not present in the DataFrame.")

# Example usage
input_excel_path = 'new_data/extracted_tables_new.xlsx'  # Adjust this to the correct path of your uploaded Excel file
output_excel_path = 'new_data/NOW_extracted_tables_new.xlsx'
transform_excel_data(input_excel_path, output_excel_path)
