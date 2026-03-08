import streamlit as st

st.title("📈 Recovery Monitor")

with st.form("recovery_form"):
    condition_today = st.selectbox("How are you feeling today?", ["Better", "Same", "Worse"])
    pain_level = st.slider("Pain level", min_value=0, max_value=10, value=2)
    fever_status = st.text_input("Current fever status", placeholder="Example: No fever / 99 F")
    medication_taken = st.radio("Did you take your medication?", ["Yes", "No"], horizontal=True)
    new_symptoms = st.text_area("Any new symptoms?")
    submitted = st.form_submit_button("Submit Recovery Check-in")

if submitted:
    st.info("Analyzing recovery... currently using mock response")

    if condition_today == "Better":
        st.success("Recovery trend: Improving")
        st.write("Updated Severity: S4 - Mild")
        st.write("Guidance: Continue medication and monitoring.")
    elif condition_today == "Same":
        st.warning("Recovery trend: Stable")
        st.write("Updated Severity: S3 - Moderate")
        st.write("Guidance: Continue monitoring and consider clinic follow-up.")
    else:
        st.error("Recovery trend: Worsening")
        st.write("Updated Severity: S2 - Urgent")
        st.write("Guidance: Hospital visit within 24 hours recommended.")