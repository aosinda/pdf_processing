from PyPDF2 import PdfReader, PdfWriter
import os

def extract_pages_from_pdf(file_path: str, output_directory: str, start_pages: int = None, end_pages: int = None, specific_pages: list = None):
    """
    Extracts pages from specified sections (start, end, specific) of a PDF, and saves them as a new PDF.

    Args:
    file_path (str): The path to the PDF file.
    output_directory (str): The directory to save the extracted PDF.
    start_pages (int, optional): Number of pages to extract from the start of the PDF. Defaults to None.
    end_pages (int, optional): Number of pages to extract from the end of the PDF. Defaults to None.
    specific_pages (list, optional): Specific page numbers to extract. Defaults to None.
    """
    reader = PdfReader(file_path)
    writer = PdfWriter()

    # Total number of pages in the PDF
    num_pages = len(reader.pages)

    # Determine pages to extract
    pages_to_extract = set()
    if start_pages is not None:
        pages_to_extract.update(range(start_pages))
    if end_pages is not None:
        pages_to_extract.update(range(num_pages - end_pages, num_pages))
    if specific_pages is not None:
        pages_to_extract.update([p - 1 for p in specific_pages])  # Convert to zero-indexed

    # Add the pages to extract to the writer object
    for i in sorted(pages_to_extract):
        writer.add_page(reader.pages[i])

    # Ensure the output directory exists
    os.makedirs(output_directory, exist_ok=True)
    base_name = os.path.basename(file_path)
    output_file_path = os.path.join(output_directory, f"extracted_{base_name}")

    # Write out the extracted pages to the new PDF
    with open(output_file_path, "wb") as f:
        writer.write(f)

    print(f"Extracted PDF created at {output_file_path} with pages {sorted(list(pages_to_extract))}.")

# This function allows for the extraction of pages from a PDF in several ways:
# 1. To extract pages from the beginning of the PDF, use the start_pages parameter:
#    - Example: start_pages=3 will extract the first 3 pages.
# 2. To extract pages from the end of the PDF, use the end_pages parameter:
#    - Example: end_pages=4 will extract the last 4 pages.
# 3. To extract specific pages anywhere in the PDF, use the specific_pages parameter:
#    - Example: specific_pages=[5, 15, 25] will extract pages 5, 15, and 25.
# 4. You can combine any of the above methods to suit your needs. Adjust the parameters accordingly.

extract_pages_from_pdf(
    "your path to your PDF", 
    "folder to save extracted PDF", 
    start_pages=10,
)
