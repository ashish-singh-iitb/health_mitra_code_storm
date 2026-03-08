import streamlit as st
from config import APP_NAME, SUPPORTED_LANGUAGES

st.set_page_config(
    page_title=APP_NAME,
    page_icon="🏥",
    layout="wide"
)

if "language" not in st.session_state:
    st.session_state.language = "English"

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {
        "full_name": "",
        "age": "",
        "gender": "",
        "preferred_language": "English"
    }

st.title("🏥 HealthMitra")
st.subheader("AI-powered multilingual healthcare support")

st.markdown(
    """
    HealthMitra helps users across the care journey:

    **Symptom Input → Severity Classification → Care Guidance → Consultation Summary → Medication Tracking → Recovery Monitoring**
    """
)

st.warning(
    "HealthMitra is an AI-assisted hackathon demo and is not a substitute for professional medical advice, diagnosis, or emergency care."
)

st.divider()

st.header("1. Select Language")

selected_language = st.radio(
    "Choose your preferred language",
    options=list(SUPPORTED_LANGUAGES.keys()),
    index=list(SUPPORTED_LANGUAGES.keys()).index(st.session_state.language),
    horizontal=True
)

st.session_state.language = selected_language
st.session_state.user_profile["preferred_language"] = selected_language

st.success(f"Selected language: {selected_language}")

st.divider()

st.header("2. Patient Basic Details")

with st.form("patient_details_form"):
    full_name = st.text_input("Full Name", value=st.session_state.user_profile["full_name"])
    age = st.number_input("Age", min_value=0, max_value=120, value=25)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    submitted = st.form_submit_button("Save Details")

    if submitted:
        st.session_state.user_profile["full_name"] = full_name
        st.session_state.user_profile["age"] = age
        st.session_state.user_profile["gender"] = gender
        st.success("Patient details saved successfully.")

st.divider()

st.header("3. Go to Modules")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/1_Symptom_Checker.py", label="Go to Symptom Checker", icon="🩺")
    st.page_link("pages/2_Consultation_Summary.py", label="Go to Consultation Summary", icon="📋")

with col2:
    st.page_link("pages/3_Medication_Tracker.py", label="Go to Medication Tracker", icon="💊")
    st.page_link("pages/4_Recovery_Monitor.py", label="Go to Recovery Monitor", icon="📈")