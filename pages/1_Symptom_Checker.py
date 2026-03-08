import streamlit as st
from config import SEVERITY_INFO

st.title("🩺 Symptom Checker")

if "language" not in st.session_state:
    st.session_state.language = "English"

st.write(f"Current language: **{st.session_state.language}**")

with st.form("symptom_form"):
    symptom_text = st.text_area(
        "Describe your symptoms",
        placeholder="Example: I have fever, cough, and body pain for 2 days"
    )
    duration = st.text_input("Symptom duration", placeholder="Example: 2 days")
    temperature = st.text_input("Temperature (optional)", placeholder="Example: 101 F")
    prior_conditions = st.text_area("Prior conditions (optional)", placeholder="Example: diabetes, asthma")
    uploaded_file = st.file_uploader(
        "Upload prescription or symptom image (optional)",
        type=["jpg", "jpeg", "png", "pdf"]
    )

    submit_btn = st.form_submit_button("Analyze Symptoms")

if submit_btn:
    if not symptom_text.strip():
        st.error("Please enter symptoms.")
    else:
        st.info("Calling AI analysis... currently using mock response")

        mock_response = {
            "extracted_symptoms": ["fever", "cough", "body pain"],
            "severity_level": "S3",
            "severity_label": "Moderate",
            "reasoning": "Symptoms suggest a condition that should be clinically assessed.",
            "recommended_action": "Clinic visit recommended",
            "care_guidance": "Drink fluids, rest, monitor temperature, and consult a doctor."
        }

        severity_code = mock_response["severity_level"]
        severity_data = SEVERITY_INFO.get(severity_code, {})

        st.subheader("Analysis Result")
        st.write(f"**Extracted Symptoms:** {', '.join(mock_response['extracted_symptoms'])}")
        st.write(f"**Severity Level:** {severity_code} - {mock_response['severity_label']}")
        st.write(f"**Meaning:** {severity_data.get('message', '-')}")
        st.write(f"**Reasoning:** {mock_response['reasoning']}")
        st.write(f"**Recommended Action:** {mock_response['recommended_action']}")
        st.write(f"**Care Guidance:** {mock_response['care_guidance']}")

        if uploaded_file is not None:
            st.success(f"Uploaded file: {uploaded_file.name}")

        if severity_code == "S1":
            st.error("Emergency symptoms detected. Please seek immediate medical care.")
        elif severity_code == "S2":
            st.warning("Urgent symptoms detected. Please visit a hospital within 24 hours.")
        elif severity_code == "S3":
            st.warning("Moderate condition detected. Clinic visit recommended.")
        elif severity_code == "S4":
            st.success("Mild condition detected. Home care and monitoring suggested.")
        elif severity_code == "S5":
            st.info("Wellness guidance suggested.")