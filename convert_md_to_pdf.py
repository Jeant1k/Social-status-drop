import os
from fpdf import FPDF
import markdown
import re

# Config
input_file = 'Project_Full.md'
output_file = 'Project_Full.pdf'
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
font_bold_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'

# Custom class to handle fonts and basic setup
class PDF(FPDF):
    def header(self):
        pass # No header for now
    
    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', '', 8)
        self.cell(0, 10, f'Page {self.page_no()}', align='C')

def convert():
    # Read MD
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pre-processing for better fpdf2 compatibility
    # Replace the page break div with a unique marker we can split on
    sections = text.split('<div style="page-break-after: always;"></div>')
    
    # Initialize PDF
    pdf = PDF()
    
    # Add Font
    if os.path.exists(font_path):
        # Add a Unicode font
        pdf.add_font('DejaVu', '', font_path)
        if os.path.exists(font_bold_path):
            pdf.add_font('DejaVu', 'B', font_bold_path)
        else:
            pdf.add_font('DejaVu', 'B', font_path) # Fallback
            
        # Fallback for Italic (map to Regular if oblique not found)
        # Using Regular for Italic prevents crash, though text won't be italic.
        pdf.add_font('DejaVu', 'I', font_path)
        pdf.add_font('DejaVu', 'BI', font_bold_path if os.path.exists(font_bold_path) else font_path)
        
        pdf.set_font('DejaVu', size=11)
    else:
        print("Warning: DejaVu font not found. Cyrillic support might be missing.")
        pdf.set_font("Arial", size=11)

    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Process each section
    for i, section in enumerate(sections):
        pdf.add_page()
        
        # Convert to HTML
        html = markdown.markdown(section, extensions=['extra', 'tables', 'nl2br'])
        
        try:
            pdf.write_html(html)
        except Exception as e:
            print(f"Error rendering section {i}: {e}")
            # Fallback: write as plain text (stripped of HTML tags ideally)
            clean_text = re.sub('<[^<]+?>', '', html) 
            pdf.multi_cell(0, 10, clean_text)

    try:
        pdf.output(output_file)
        print(f"Successfully generated {output_file}")
    except Exception as e:
        print(f"Error saving PDF: {e}")

if __name__ == "__main__":
    convert()
