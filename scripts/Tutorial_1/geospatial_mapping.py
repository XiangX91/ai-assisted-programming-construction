import pandas as pd
import folium
import os

def create_manhattan_incident_map(filepath):
    """
    Loads construction incident data, filters for 'Worker Fell' incidents
    in Manhattan, and creates an interactive map of their locations.

    Args:
        filepath (str): The path to the CSV file.
    """
    # --- 1. Load and Prepare Data ---
    # Try to load the dataset. A FileNotFoundError will be raised if the file path is incorrect.
    try:
        df = pd.read_csv(filepath)
        # Rename 'Check2 Description' to 'Incident_Type' for clarity and consistency.
        df.rename(columns={'Check2 Description': 'Incident_Type'}, inplace=True)
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' was not found. Please check the file path.")
        return

    # Filter the DataFrame for 'Worker Fell' incidents that occurred in Manhattan.
    manhattan_falls_df = df[(df['Borough'] == 'Manhattan') & (df['Incident_Type'] == 'Worker Fell')].copy()
    print(f"Found {len(manhattan_falls_df)} 'Worker Fell' incidents in Manhattan.")

    # --- 2. Clean Geospatial Data ---
    # Convert 'Latitude' and 'Longitude' columns to numeric types.
    # 'coerce' will turn any values that cannot be converted into NaN (Not a Number).
    manhattan_falls_df['Latitude'] = pd.to_numeric(manhattan_falls_df['Latitude'], errors='coerce')
    manhattan_falls_df['Longitude'] = pd.to_numeric(manhattan_falls_df['Longitude'], errors='coerce')

    # Drop rows where Latitude or Longitude are missing to ensure we can plot them.
    initial_count = len(manhattan_falls_df)
    manhattan_falls_df.dropna(subset=['Latitude', 'Longitude'], inplace=True)
    cleaned_count = len(manhattan_falls_df)
    if initial_count > cleaned_count:
        print(f"Removed {initial_count - cleaned_count} rows with missing location data.")

    # --- 3. Create the Map Visualisation ---
    # Initialize a folium map centered on Manhattan.
    # The location is [latitude, longitude] and zoom_start controls the initial zoom level.
    manhattan_map = folium.Map(location=[40.7831, -73.9712], zoom_start=12)

    # Iterate through each incident in our cleaned, filtered DataFrame.
    for index, row in manhattan_falls_df.iterrows():
        # For each incident, add a circle marker to the map.
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=5,  # Defines the size of the circle marker.
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.7,
            # Create a popup that displays the incident date when a marker is clicked.
            popup=f"Incident Date: {row['Incident Date']}"
        ).add_to(manhattan_map)

    # --- 4. Save the Output ---
    # Save the generated map to an HTML file.
    output_filename = 'manhattan_worker_fall_map.html'
    manhattan_map.save(output_filename)
    print(f"\nMap has been successfully generated and saved as '{output_filename}'.")

# --- Main execution block ---
# This ensures the code runs only when the script is executed directly.
if __name__ == '__main__':
    # Define the file path for the dataset, assuming it's in a 'data' subdirectory.
    # The os.path.join function creates a platform-independent file path.
    file_path = os.path.join('data', 'Construction-Related_Incidents.csv')
    create_manhattan_incident_map(file_path)
