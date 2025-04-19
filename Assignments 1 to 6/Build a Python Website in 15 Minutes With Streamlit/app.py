import streamlit as st
import pandas as pd
import datetime

st.title("🌈 Daily Mood Tracker App")

st.write("Track your mood every day and see your weekly trend!")

# Mood selection
mood = st.radio(
    "How are you feeling today?",
    ("😊 Happy", "😐 Neutral", "😔 Sad")
)

# Add comment box
note = st.text_area("Want to write something about today?", "")

# Save mood button (in real scenario, you’d store it in a DB)
if st.button("Save Today's Mood"):
    st.success(f"Mood saved: {mood} - {note}")

# Display mood trend chart (sample random data)
st.subheader("Weekly Mood Trend")
data = pd.DataFrame({
    "Date": pd.date_range(end=datetime.datetime.today(), periods=7),
    "Mood Level": [3, 2, 4, 5, 3, 2, 4]  # 1=sad, 3=neutral, 5=happy
})
st.line_chart(data.set_index("Date"))

st.write("💡 Come back daily to track your emotions!")

