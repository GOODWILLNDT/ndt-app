import streamlit as st
from datetime import date

st.set_page_config(page_title="GOODWILLNDT - NDT MASTER", layout="wide")
st.title("GOODWILLNDT - NDT MASTER")
st.subheader("Non-Destructive Testing Report Generator | Dammam, Saudi Arabia")

# --- TOP DETAILS ---
c1, c2 = st.columns(2)
with c1:
    client = st.text_input("Client Name", "Example: ARAMCO / SABIC")
    project = st.text_input("Project / Location", "Dammam")
    job_no = st.text_input("Job / Report No", "GW-2026-001")
    report_date = st.date_input("Date", date.today())
with c2:
    methods = ["UT - Ultrasonic Testing","MT - Magnetic Particle","PT - Penetrant Testing","RT - Radiographic Testing","VT - Visual Testing","ET - Eddy Current","PAUT - Phased Array UT","TOFD - Time of Flight Diffraction","MFL - Magnetic Flux Leakage","PMI - Positive Material Identification","Hardness Test","Ferrite Test","Leak Test - Bubble","Leak Test - Helium","Leak Test - Halogen","Hydro Test","Pneumatic Test","Coating / DFT Test","PWHT - Post Weld Heat Treatment"]
    method = st.selectbox("NDT Method", methods)
    tech = st.text_input("Technician Name", "")
    level = st.selectbox("Technician Level", ["Level I","Level II","Level III"])
    result = st.selectbox("Overall Result", ["ACCEPTED","REJECTED","REPAIR / RE-TEST"])

st.divider()
st.subheader("Job Details")

c3, c4, c5 = st.columns(3)
with c3:
    joint = st.text_input("Joint / Item No", "J-01")
    material = st.text_input("Material / Grade", "Carbon Steel A106 Gr B")
    thickness = st.text_input("Thickness / Size", "12.7 mm")
with c4:
    procedure = st.text_input("Procedure No", "GW-NDT-P-01")
    acceptance = st.text_input("Acceptance Standard", "ASME Sec V / Aramco Std")
    drawing = st.text_input("Drawing No", "DWG-001")
with c5:
    equipment = st.text_input("Equipment Used", "")
    consumable = st.text_input("Consumable / Film / Couplant", "")
    calibration = st.text_input("Calibration Block / Cal Due Date", "")

# --- METHOD SPECIFIC FIELDS ---
st.divider()
st.subheader(f"Method Specific Details - {method}")

m1, m2, m3 = st.columns(3)
if "UT" in method or "PAUT" in method or "TOFD" in method:
    with m1: freq = st.text_input("Probe / Frequency", "4 MHz, 45 Deg")
    with m2: gain = st.text_input("Gain / DAC / TCG", "45 dB")
    with m3: scan = st.text_input("Scan Coverage / Calibration", "100% - IIW V1 Block")
elif "MT" in method:
    with m1: yoke = st.text_input("Yoke / Prod - Current", "AC Yoke - 230V")
    with m2: powder = st.text_input("Powder / Contrast Paint", "Black Powder / White Paint")
    with m3: field = st.text_input("Field Direction", "Longitudinal + Transverse")
elif "PT" in method:
    with m1: pen = st.text_input("Penetrant Type", "Visible / Fluorescent - Type II")
    with m2: dwell = st.text_input("Dwell / Developer Time", "10 min / 10 min")
    with m3: clean = st.text_input("Cleaner / Temp", "Solvent Removable")
elif "RT" in method:
    with m1: source = st.text_input("Source / kV / Ci", "Ir-192 / 25 Ci")
    with m2: film = st.text_input("Film / SFD / IQI", "D7 / 600mm / 1-2T")
    with m3: exposure = st.text_input("Exposure Time / Density", "2.5 min / 2.0-4.0")
elif "VT" in method:
    with m1: visual = st.text_input("Visual Aid", "10X Magnifier / Borescope")
    with m2: light = st.text_input("Light Intensity", "1000 Lux")
    with m3: surface = st.text_input("Surface Condition", "Clean / Ground Flush")
elif "ET" in method:
    with m1: et_freq = st.text_input("Frequency / Probe", "200 kHz / Absolute")
    with m2: et_std = st.text_input("Calibration Standard", "ASME Tube Block")
    with m3: et_gain = st.text_input("Gain / Phase", "60 dB / 0 Deg")
elif "MFL" in method:
    with m1: mfl_tool = st.text_input("Tool / Scanner", "MFL Scanner - 12 inch")
    with m2: mfl_speed = st.text_input("Scan Speed", "0.5 m/s")
    with m3: mfl_cal = st.text_input("Cal Plate / Sensitivity", "20% Wall Loss")
elif "PMI" in method:
    with m1: pmi_gun = st.text_input("XRF Gun Model / Serial", "Olympus Vanta")
    with m2: pmi_time = st.text_input("Test Time", "30 Sec")
    with m3: pmi_grade = st.text_input("Identified Grade", "SS 316L")
elif "Hardness" in method:
    with m1: hard_type = st.text_input("Method", "Rockwell / Brinell / Leeb")
    with m2: hard_load = st.text_input("Load / Scale", "150 kgf / HRC")
    with m3: hard_val = st.text_input("Avg Value", "185 HB")
elif "Ferrite" in method:
    with m1: fer_meter = st.text_input("Ferrite Meter", "Fischer FMP30")
    with m2: fer_cal = st.text_input("Calibration Standard", "10 FN Block")
    with m3: fer_val = st.text_input("Avg FN", "5.2 FN")
elif "Leak" in method:
    with m1: leak_med = st.text_input("Test Medium / Pressure", "Air / 2 Bar")
    with m2: leak_sol = st.text_input("Solution / Detector", "Soap Solution / He Detector")
    with m3: leak_hold = st.text_input("Hold Time", "10 Min")
elif "Hydro" in method:
    with m1: hydro_press = st.text_input("Test Pressure", "150 Bar")
    with m2: hydro_hold = st.text_input("Hold Time", "30 Min")
    with m3: hydro_med = st.text_input("Medium / Temp", "Water / 25 C")
elif "Pneumatic" in method:
    with m1: pneu_press = st.text_input("Test Pressure", "7 Bar")
    with m2: pneu_hold = st.text_input("Hold Time / Steps", "10 Min / 10% Steps")
    with m3: pneu_med = st.text_input("Medium", "Dry Air / Nitrogen")
elif "Coating" in method:
    with m1: coat_type = st.text_input("Coating Type", "Epoxy 3LPE")
    with m2: dft_val = st.text_input("Required DFT / Measured DFT", "250 micron / 268 micron")
    with m3: dft_gauge = st.text_input("DFT Gauge", "Elcometer 456")
elif "PWHT" in method:
    with m1: pwht_temp = st.text_input("Soak Temp / Time", "620 C / 2 Hrs")
    with m2: pwht_rate = st.text_input("Heating / Cooling Rate", "100 C/hr")
    with m3: pwht_chart = st.text_input("Chart No / Thermocouple", "CH-01 / 4 Nos")

st.divider()
st.subheader("Inspection Results Table")

# Results table - simple
n = st.number_input("No of Joints / Spots", 1, 20, 3)
remarks = st.text_area("Defects / Observations / Remarks", "No relevant indication observed. All joints found acceptable as per acceptance standard.")
if st.button("GENERATE REPORT", type="primary"):
    st.success(f"✅ REPORT GENERATED - {job_no} - {result}")
    st.markdown(f"""
    ### GOODWILLNDT - NDT REPORT
    **Client:** {client} | **Project:** {project}
    **Report No:** {job_no} | **Date:** {report_date}
    **Method:** {method} | **Technician:** {tech} ({level})
    **Joint:** {joint} | **Material:** {material} | **Thickness:** {thickness}
    **Procedure:** {procedure} | **Standard:** {acceptance}
    **Equipment:** {equipment} | **Consumable:** {consumable}
    **Calibration:** {calibration}
    **No of Joints:** {n}
    **Remarks:** {remarks}
    ### RESULT: {result}
    **Technician Sign:** ___________ **QC Sign:** ___________ **Client Sign:** ___________
    """)
    st.info("Print pannina: Browser la Ctrl+P adhichu PDF ah save pannunga. Report ready!")
    st.balloons()