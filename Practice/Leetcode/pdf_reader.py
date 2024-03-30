import pdfkit as pdf
import numpy as np
import pandas as pd
# from wkhtmltopdf import WKhtmlToPdf
from fpdf import FPDF

data = [{"a": 1, "b": 2, "c": 3, "d": 4}, {"a": 5, "b": 6, "c": 7, "d": 8}]

def write_table_using_fpdf():

    pdf = FPDF(orientation="landscape", format="a3")
    pdf.add_page()
    pdf.set_font("Times", size=12)

    # set the line height and column width
    line_height = pdf.font_size * 17.5
    col_width = 10

    for row in data:
        for k, v in row.items():
            print(v)
            pdf.multi_cell(col_width, line_height, str(v), border=1)
        pdf.ln(line_height)
    pdf.output(name="pdf_using_fpdf.pdf")

write_table_using_fpdf()


# data = [{"a": 1, "b": 2, "c":[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,],
#                 "d": [4,4,4,4,4,4,4,4,4,]},
#         {"a": 5, "b": [6,6,6,6,6,6,6,6,6,6], "c":
#           [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7], "d": 8}]

# def pdf_gen_weasyprint():

#         # extract headers from input data
#         table_headers = [headers.title() for headers in data[0]]

#         # extract table data from input data
#         table_values = [str(v) for d in data for k, v in d.items()]

#         # convert input data to HTML
#         a = np.array(table_values)
#         df = pd.DataFrame(a.reshape(-1, len(table_headers)), columns=table_headers)
#         html_string = df.to_html(index=False)

#         # write html to pdf
#         html_doc = HTML(string=html_string)

#         html_doc.write_pdf(f"your_report.pdf", stylesheets=None)

# pdf_gen_weasyprint()



data = [{"a": 1, "b": 2, "c": [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,],
         "d": [4,4,4,4,4,4,4,4,4,]},
        {"a": 5, "b": [6,6,6,6,6,6,6,6,6,6], "c":
          [7,7,7,7,7,7,7,7,7,7,7,7,7,7,7], "d": 8}]

# def pdf_gen_pdfkit():

#         table_headers = [headers.title() for headers in data[0]]

#         # extract table data from input data
#         table_values = [str(v) for d in data for k, v in d.items()]

#         # convert input data to HTML
#         a = np.array(table_values)
#         # this is required to match your column numbers
#         df = pd.DataFrame(a.reshape(-1, len(table_headers)), columns=table_headers)
#         # removing the index while writing to html
#         html_string = df.to_html(index=False)
#         # print(html_string)
#         path_wkthmltopdf = 'D:\python projects\Practice\Leetcode\pdfkit_sample.pdf'
#         config = pdf.configuration(wkhtmltopdf=path_wkthmltopdf)
        
#         # pdf.from_string(html_string, "pdfkit_sample.pdf")

#         # sample code to write with css
#         #pdf.from_string(html_string, "pdfkit_sample.pdf", css="my_pdf_style.css")

# pdf_gen_pdfkit()