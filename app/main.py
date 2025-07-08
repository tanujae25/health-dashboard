import streamlit as st

st.set_page_config(page_title="Health Insight Dashboard", layout="wide")

st.title("🧠 AI-Powered Personal Health Dashboard")

st.subheader("📝 Daily Health Log")

# Input fields
mood = st.selectbox("How do you feel today?", ["Happy", "Tired", "Anxious", "Sad", "Energetic"])
sleep = st.slider("Hours of Sleep", 0, 12, 6)
water = st.slider("Water Intake (in litres)", 0.0, 5.0, 2.0)
steps = st.number_input("Steps Walked Today", min_value=0, step=100)

if st.button("Submit Entry"):
    st.success(f"✔️ Entry submitted!\n\nMood: {mood}, Sleep: {sleep}h, Water: {water}L, Steps: {steps}")
