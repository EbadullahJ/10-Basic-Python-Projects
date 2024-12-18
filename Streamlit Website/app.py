import streamlit as st
import pandas as pd
import matplotlib as ply

st.title("Simple Data Dashboard")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.subheader("Data Preview")
    st.write(df.head())

    st.subheader("Data Summary")
    st.write(df.describe())

    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    if df[selected_column].dtype == 'object':
        unique_values = df[selected_column].unique()
        selected_value = st.selectbox(f"Select Value for {selected_column}", unique_values)
        filtered_df = df[df[selected_column] == selected_value]
    else:
        min_value, max_value = float(df[selected_column].min()), float(df[selected_column].max())
        selected_range = st.slider(
            f"Select range for {selected_column}",
            min_value=min_value,
            max_value=max_value,
            value=(min_value, max_value)
        )
        filtered_df = df[
            (df[selected_column] >= selected_range[0]) & (df[selected_column] <= selected_range[1])
        ]

    st.write(filtered_df)
    st.subheader("Plot Data")
    x_column = st.selectbox("Select X-axis column", columns)
    y_column = st.selectbox("Select Y-axis column", columns)

    if st.button("Generate Plot"):
        try:
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        except Exception as e:
            st.error(f"Error generating plot: {e}")

else:
    st.write("Waiting for file to upload...")
