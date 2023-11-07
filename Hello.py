
import streamlit as st
import pandas as pd


def main():
    # Title of the app
    st.title("Streamlit App with Pandas")

    # Display dependencies with exact versions
    st.subheader("Dependencies")
    st.write("- pandas==1.4.0")
    st.write("- streamlit==0.105.0")

    # Upload file
    st.subheader("Upload File")
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)

        # Display the DataFrame
        st.subheader("DataFrame")
        st.write(df)

        # Operations
        st.subheader("Popular Operations on DataFrame")
        
        # Get number of rows and columns
        st.write("- Shape of the DataFrame: ", df.shape)
        
        # Get column names
        st.write("- Column Names: ", df.columns.tolist())
        
        # Check for missing values
        st.write("- Missing Values: ", df.isnull().sum().to_frame(name="Count"))
        
        # Get statistical summary
        st.write("- Statistical Summary: ", df.describe())
        
        # Filter rows based on condition
        st.write("- Filtered Rows (Age > 30): ")
        filtered_df = df[df["Age"] > 30]
        st.write(filtered_df)
        
        # Group by and aggregation
        st.write("- Aggregated Data (Average Age by Gender): ")
        agg_df = df.groupby("Gender")["Age"].mean().to_frame(name="Average Age")
        st.write(agg_df)


if __name__ == "__main__":
    main()
