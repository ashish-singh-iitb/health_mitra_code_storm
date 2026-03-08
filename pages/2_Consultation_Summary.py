import streamlit as st

st.title("📋 Consultation Summary")

with st.form("consultation_form"):
    consultation_notes = st.text_area(
        "Enter doctor consultation notes or visit details",
        placeholder="Example: Patient has viral fever. Advised rest and paracetamol for 3 days."
    )
    submitted = st.form_submit_button("Generate Summary")

if submitted:
    if not consultation_notes.strip():
        st.error("Please enter consultation notes.")
    else:
        st.info("Generating summary... currently using mock response")

        st.subheader("Generated Summary")
        st.write("**Reason for visit:** Fever and cough")
        st.write("**Findings:** Likely viral infection")
        st.write("**Advice:** Rest, hydration, temperature monitoring")
        st.write("**Follow-up:** Visit clinic if symptoms worsen")