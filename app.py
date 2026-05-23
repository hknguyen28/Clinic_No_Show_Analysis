import streamlit as st
import pandas as pd

# 1. Setup the page
st.set_page_config(page_title="Clinic Dashboard", layout="wide")
st.title("🏥 Clinic Operations Dashboard")
st.markdown("Live view of patient scheduling and no-show metrics.")

# 2. Load the dataset
df = pd.read_csv('appointments.csv')

# 3. Calculate metrics
total_appts = len(df)
no_shows = len(df[df['no_show'] == 'Yes'])
no_show_rate = round((no_shows / total_appts) * 100, 1)

# 4. Build the UI layout (3 columns for numbers)
col1, col2, col3 = st.columns(3)
col1.metric("Total Appointments", total_appts)
col2.metric("Missed Appointments", no_shows)
col3.metric("No-Show Rate (%)", f"{no_show_rate}%")

# 5. Display the data table
st.subheader("Raw Patient Data")
st.dataframe(df, use_container_width=True)