## PDF Processing Repository
This repository contains scripts and notebooks designed to process PDF files, extracting tables, text, and performing various manipulations on the data. The repository is structured into directories that separate original data, extracted/manipulated data, and the source code.

### recommendation of additional folders
data/: This directory should contain the original data in its raw form (e.g., PDFs or CSV files) that are yet to be processed.

new_data/: This directory will contain extracted, manipulated, or processed data files, such as cleaned-up tables, transposed data, or formatted Excel outputs.

### Files
'extract_pages.py': A Python script to extract specific pages from PDFs based on certain criteria. could be to remove x amount pages from start, end or specific pages.

test_one_page.ipynb: A Jupyter Notebook for testing PDF extraction processes on a single page, used to verify extraction logic before scaling to multiple pages.

extract_text_tables_multiple_pages.ipynb: A Jupyter Notebook designed to extract both text and tables from PDFs that have multiple pages, and processes each page accordingly.

remove_pages.py: A Python script to remove certain pages from PDFs, based on criteria such as keywords or page numbers.

test_excel_to_excel.py: A script to convert extracted data into Excel format, ensuring proper formatting and organization across different sheets.

turn_values_excel_copy.py: A script that transposes or turns extracted values into a desired format, and saves the results into an Excel file.