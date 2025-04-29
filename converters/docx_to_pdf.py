import os
from docx2pdf import convert

def convert_docx_to_pdf(docx_path: str) -> str:
    output_dir = os.path.dirname(docx_path)
    convert(docx_path, output_dir)
    
    pdf_filename = os.path.splitext(os.path.basename(docx_path))[0] + ".pdf"
    pdf_path = os.path.join(output_dir, pdf_filename)
    
    if not os.path.exists(pdf_path):
        raise Exception("PDF was not generated.")
    
    return pdf_path