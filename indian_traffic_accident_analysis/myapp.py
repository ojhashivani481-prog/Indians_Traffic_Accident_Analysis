#step-6:STEAMLIT dASHBOARD Dashboard with KPI Cards

import streamlit as st
import pandas as pd

# Configure the dashboard page
st.set_page_config(
    page_title="Indian Traffic Accident Analysis",
    page_icon="🚗",
    layout="wide"
)

# Load the cleaned dataset
df = pd.read_csv("data/cleaned_accident_data.csv")

# Display the dashboard title
st.title("Indian Traffic Accident Analysis")
st.write("Explore accident records through statistics and charts.")

# Create three columns for KPI cards
col1, col2, col3 = st.columns(3)

# Display total accident records
col1.metric("Total Accident Records", len(df))

# Display total casualties
col2.metric(
    "Total Casualties",
    f"{df['Number of Casualties'].sum():,}"
)

# Display total fatalities
col3.metric(
    "Total Fatalities",
    f"{df['Number of Fatalities'].sum():,}"
)


# Part 6 - Streamlit: Add Dashboard Filters

# Create a year filter
years = sorted(df["Year"].unique())

selected_year = st.selectbox(
    "Select Year",
    ["All Years"] + years
)

# Create an accident severity filter
severities = sorted(df["Accident Severity"].unique())

selected_severity = st.selectbox(
    "Select Accident Severity",
    ["All Severities"] + severities
)

# Start with all records
filtered_df = df.copy()

# Filter records by year
if selected_year != "All Years":
    filtered_df = filtered_df[
        filtered_df["Year"] == selected_year
    ]

# Filter records by severity
if selected_severity != "All Severities":
    filtered_df = filtered_df[
        filtered_df["Accident Severity"] == selected_severity
    ]

# Display the number of filtered records
st.subheader("Filtered Accident Records")
st.write("Records found:", len(filtered_df))

# Display filtered data
st.dataframe(filtered_df)
