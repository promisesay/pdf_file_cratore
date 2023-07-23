from fpdf import FPDF
import pandas as pn
topics = pn.read_csv("topics.csv")

pdf = FPDF(orientation="L", format="Letter", unit="mm")
for index, row in topics.iterrows():
    pdf.add_page()
    pdf.set_font(style="B", family="Times", size=22)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(txt=row["Topic"], align="L", w=0, h=10, ln=1)
    pdf.line(10, 21, 265, 21)


pdf.output("output.pdf")
