import streamlit as st
import json

# Load the exam data
with open('General_Class_License_Exam_Questions.json', 'r') as f:
    data = json.load(f)

st.title("GAYLE: Socratic Engine")

# Get the first inquiry
current_item = data[0]
st.write(f"### Inquiry: {current_item['question']}")

# Socratic input area
user_derivation = st.text_area("Your Derivation (Explain the principle):")

if st.button("Submit"):
    st.write("Processing derivation...")
    # Logic to evaluate the derivation against the 'correct_answer'
    st.write(f"Verification Key: {current_item['correct_answer']}")
