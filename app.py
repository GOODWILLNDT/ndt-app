import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="GOODWILL NDT - NDT MASTER", layout="wide")
st.title("GOODWILL NDT - NDT MASTER")
st.subheader("UTT - Ultrasonic Thickness Test Report")

ALL_DATA = {
    '806-PSV-0151': [
        [1, "PIPE", "", 7.6, 7.6, 8.1, 8.2, 8.1, "", ""],
        [2, "ELBOW", "", "", "", 7.6, 7.6, "", 6.2],
        [3, "PIPE", "", "", "", 7.6, 7.6, 7.3, 7.3],
        [4, "PIPE", "", 9.2, 9.2, 9.3, 8.5, 8.7, "", ""],
        [5, "PIPE", "", 7.6, 7.6, 7.6, 7.2, 6.2, "", ""],
    ],
    '806-PSV-0150': [
        [1, "PIPE", "", 10.2, 9.2, 9.2, 8.1, "", "", ""],
        [2, "PIPE", "", 7.2, 7.6, 6.7, 7.2, "", "", ""],
    ],
    'TO FLARE HEADER 8" x 6"': [
        [1, "PIPE", '8"', 7.2, 7.6, 7.2, 7.3, "", "", ""],
        [2, "ELBOW", '8"', 6.3, 6.7, 6.3, "", "", "", ""],
        [3, "ELBOW", "", 10.6, 10.6, 10.6, 11.6, "", "", ""],
        [4, "PIPE", '6"', 7.2, 7.2, 8.1, 7.6, "", "", ""],
        [5, "ELBOW", '6"', 8.7, 9.2, 8.2, "", "", "", ""],
        [6, "PIPE", '6"', 8.2, 8.7, 8.5, 8.8, "", "", ""],
    ],
}

c1, c2, c3 = st.columns(3)
client = c1.text_input("Client", "KJO")
job_no = c2.text_input("Project / Job No.", "HQ628ES19")
location = c3.text_input("Location / Site", "Y2B")
c4, c5 = st.columns(2)
report_no = c4.text_input("Report No.", "QCS/Y2B/UTT/01")
date = c5.text_input("Date", "25/10/2026")

line_no = st.selectbox("LINE NO. - Select Pannu, Table Thanaave Maarum", list(ALL_DATA.keys()))
cols = ["S.No", "COMPONENT", "Size", "NORTH", "SOUTH", "EAST", "WEST", "TOP", "BOT", "O.D."]
df = pd.DataFrame(ALL_DATA[line_no], columns=cols)
st.subheader(f"UTT Table - {line_no}")
edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True, key=f"editor_{line_no}")

st.subheader("Report Details")
c6, c7, c8 = st.columns(3)
instrument = c6.text_input("Instrument", "OLYMPUS 38DL PLUS")
probe = c7.text_input("Probe / Transducer", "5 MHz Dual")
cal_block = c8.text_input("Cal. Block", "Step Block 5-20mm")
c9, c10, c11 = st.columns(3)
procedure = c9.text_input("Procedure No.", "QCS/UTT/P-01")
acceptance = c10.text_input("Acceptance", "ASME B31.3")
technician = c11.text_input("Technician", "PETER")
result = st.selectbox("Result", ["ACCEPTED", "REJECTED", "HOLD"])

def make_pdf(data_df):
    pdf = FPDF(orientation='L', unit='mm', format='A4')
    pdf.add_page()
    pdf.set_font("Arial", "B", 14)
    pdf.cell(0, 8, "GOODWILL NDT - NDT MASTER", ln=True, align="C")
    pdf.set_font("Arial", "", 10)
    pdf.cell(0, 6, f"Client: {client} | Job: {job_no} | Location: {location}", ln=True, align="C")
    pdf.cell(0, 6, f"Report: {report_no} | Date: {date} | Line: {line_no}", ln=True, align="C")
    pdf.cell(0, 6, f"Instrument: {instrument} | Probe: {probe} | Cal Block: {cal_block}", ln=True, align="C")
    pdf.cell(0, 6, f"Procedure: {procedure} | Acceptance: {acceptance} | Tech: {technician} | Result: {result}", ln=True, align="C")
    pdf.ln(3)
    pdf.set_font("Arial", "B", 7)
    headers = ["S.No", "COMPONENT", "Size", "NORTH", "SOUTH", "EAST", "WEST", "TOP", "BOT", "O.D."]
    widths = [12, 35, 15, 22, 22, 22, 22, 22, 22, 22]
    for i, h in enumerate(headers):
        pdf.cell(widths[i], 7, h, border=1, align="C")
    pdf.ln()
    pdf.set_font("Arial", "", 7)
    for _, row in data_df.iterrows():
        for i, h in enumerate(headers):
            v = "" if pd.isna(row[h]) else str(row[h])
            pdf.cell(widths[i], 7, v, border=1, align="C")
        pdf.ln()
    pdf.ln(4)
    pdf.set_font("Arial", "B", 10)
    pdf.cell(0, 7, f"RESULT: {result}  |  Technician: {technician}  |  Signature: ______________", ln=True)
    return pdf.output(dest="S").encode("latin-1")
pdf_bytes = make_pdf(edited_df)
st.download_button("DOWNLOAD PDF", data=pdf_bytes, file_name="report.pdf", mime="application/pdf")