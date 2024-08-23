from PyPDF2 import PdfReader, PdfWriter
import os

def remove_pages_from_pdf(file_path: str, start_pages: int = None, end_pages: int = None, specific_pages: list = None):
    """
    Removes pages from the start, end, and/or specific pages of a PDF, and saves the modified PDF to a new directory.
    """
    reader = PdfReader(file_path)
    writer = PdfWriter()
    
    # Calculate pages to keep
    num_pages = len(reader.pages)
    start_index = start_pages if start_pages is not None else 0
    end_index = num_pages - end_pages if end_pages is not None else num_pages
    pages_to_keep = set(range(start_index, end_index))

    if specific_pages is not None:
        pages_to_keep.difference_update([p - 1 for p in specific_pages])

    # Adding the pages to keep to the writer object
    for i in sorted(pages_to_keep):
        writer.add_page(reader.pages[i])
    
    # Output directory and modified file path
    output_directory = "new_data"
    os.makedirs(output_directory, exist_ok=True)
    base_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_directory, f"modified_{base_name}")

    # Writing out the modified PDF
    with open(output_file_path, "wb") as f:
        writer.write(f)

    print(f"Modified PDF created at {output_file_path} with selected pages removed.")

# This function allows for the removal of pages from a PDF in several ways:
# 1. To remove pages from the beginning of the PDF, use the start_pages parameter:
#    - Example: start_pages=3 will remove the first 3 pages.
# 2. To remove pages from the end of the PDF, use the end_pages parameter:
#    - Example: end_pages=4 will remove the last 4 pages.
# 3. To remove specific pages anywhere in the PDF, use the specific_pages parameter:
#    - Example: specific_pages=[5, 15, 25] will remove pages 5, 15, and 25.
# 4. You can combine any of the above methods to suit your needs. Adjust the parameters accordingly.
# Below is an example of combining all three methods:

# To remove the first 2 pages, the last 2 pages, and specific pages: 10 and 20


remove_pages_from_pdf("your path to your PDF", end_pages=1)
