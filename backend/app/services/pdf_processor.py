import pymupdf

def process_pdf(contents: bytes) -> str:
    """
    Extract text from a PDF file.

    Args:
        contents (bytes): The binary contents of the PDF file.

    Returns:
        str: The extracted text from the PDF file.
    """
    # Open the PDF file from the provided binary contents
    pdf = pymupdf.open(stream=contents, filetype="pdf")

    # Initialize an empty string to store the extracted text
    text = ""

    # Iterate over each page in the PDF
    for page in pdf:
        # Extract the text from the current page and append it to the text variable
        text += page.get_text()

    # Return the extracted text
    return text