import streamlit as st
import pandas as pd
import random

# Load the CSV file into a DataFrame
df = pd.read_csv('star_dataset.csv')

# Function to return star descriptions
def get_star_description(star_type):
    descriptions = {
        0: "Brown Dwarfs are faint stars with relatively low temperatures.",
        1: "Red Dwarfs are the most common stars, small and cooler than the sun.",
        2: "White Dwarfs are remnants of stars that have exhausted their fuel.",
        3: "Main Sequence stars are like the Sun, in a stable phase of burning hydrogen.",
        4: "Supergiants are massive, luminous stars near the end of their lives.",
        5: "Hypergiants are the largest known stars, very hot and extremely bright."
    }
    return descriptions.get(star_type, "Unknown star type")

# Streamlit app layout
st.title("Star Dataset Analyzer")

# Dropdown to select star type
star_type = st.selectbox(
    "Select Star Type:",
    ["--Select Star Type--", "Brown Dwarf", "Red Dwarf", "White Dwarf", "Main Sequence", "Supergiant", "Hypergiant"],
    index=0
)

# Dictionary to map star types to values
star_type_mapping = {
    "Brown Dwarf": 0,
    "Red Dwarf": 1,
    "White Dwarf": 2,
    "Main Sequence": 3,
    "Supergiant": 4,
    "Hypergiant": 5
}

if star_type != "--Select Star Type--":
    # Filter dataset based on selected star type
    selected_type_value = star_type_mapping[star_type]
    filtered_df = df[df['Star type'] == selected_type_value]

    if not filtered_df.empty:
        # Get a random sample from the filtered dataframe
        star_info = filtered_df.sample(1).iloc[0]

        # Display star details
        st.write("### Star Details")
        st.write(f"**Temperature (K):** {int(star_info['Temperature (K)'])}")
        st.write(f"**Luminosity (L/Lo):** {float(star_info['Luminosity(L/Lo)'])}")
        st.write(f"**Radius (R/Ro):** {float(star_info['Radius(R/Ro)'])}")
        st.write(f"**Star Color:** {str(star_info['Star color'])}")
        st.write(f"**Spectral Class:** {str(star_info['Spectral Class'])}")
        st.write(f"**Description:** {get_star_description(int(star_info['Star type']))}")
    else:
        st.error("No star data found for this type.")
else:
    st.warning("Please select a star type.")
