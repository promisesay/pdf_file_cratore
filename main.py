import fpdf
from fpdf import FPDF
import pandas as pn
df = pn.read_csv("topics.csv")
pdf = FPDF(orientation='P', format="A4", unit='mm')
pdf.set_auto_page_break(auto=False, margin=0)

for index, i in df.iterrows():
    pdf.add_page()

    #set the header
    pdf.set_font(style="B", size=29, family='Times')
    pdf.cell(w=0, h=12, txt=i["Topic"], ln=1, border=0, align='L')
    pdf.set_text_color(100, 100, 100)
    y = 28
    x1 = 10
    x2 = 195
    pdf.line(x1, y, x2, y)

    #set the footpage
    pdf.ln(260)
    pdf.set_font(style="I", size=8, family="Times")
    pdf.cell(w=0, h=12, txt=i["Topic"], ln=1, align='R')
    for l in range(28, 285, 10):
        pdf.line(10, l, 200, l)
    for P in range(i["Pages"] - 1):
        pdf.add_page()
        y = 28
        pdf.line(x1, y, x2, y)
        pdf.ln(270)
        pdf.set_font(style="I", size=8, family="Times")
        pdf.cell(w=0, h=12, txt=i['Topic'], align='R')
        for l in range(28, 285, 10):
            pdf.line(10, l, 200, l)

pdf.output("output.pdf")
