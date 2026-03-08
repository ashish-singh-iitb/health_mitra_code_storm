import streamlit as st
import pandas as pd

st.title("💊 Medication Tracker")

with st.form("medication_form"):
    medicine_name = st.text_input("Medicine Name")
    dosage = st.text_input("Dosage", placeholder="Example: 1 tablet")
    frequency = st.text_input("Frequency", placeholder="Example: Twice daily")
    duration_days = st.number_input("Duration (days)", min_value=1, max_value=365, value=5)
    food_instruction = st.selectbox("Food Instruction", ["After food", "Before food", "Any time"])
    submit = st.form_submit_button("Add Medication")

if "medications" not in st.session_state:
    st.session_state.medications = []

if submit:
    if not medicine_name.strip():
        st.error("Medicine name is required.")
    else:
        st.session_state.medications.append({
            "Medicine Name": medicine_name,
            "Dosage": dosage,
            "Frequency": frequency,
            "Duration Days": duration_days,
            "Food Instruction": food_instruction
        })
        st.success("Medication added.")

if st.session_state.medications:
    st.subheader("Current Medication Plan")
    df = pd.DataFrame(st.session_state.medications)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No medications added yet.")