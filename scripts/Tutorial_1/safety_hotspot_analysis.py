import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def analyze_construction_incidents(filepath):
    """
    Loads construction incident data and generates two key visualizations for a safety report.

    1. A bar chart showing the total number of incidents by NYC borough.
    2. A stacked bar chart breaking down the top 5 incident types by borough.

    Args:
        filepath (str): The path to the CSV file.
    """
    # --- 1. Load Data ---
    # Try to load the dataset. A FileNotFoundError will be raised if the file path is incorrect.
    try:
        df = pd.read_csv(filepath)
        # The prompt uses 'Incident_Type', but based on the data preview,
        # 'Check2 Description' is the most appropriate column for specific incident categories.
        # We will rename it for clarity and consistency with the prompt's instructions.
        df.rename(columns={'Check2 Description': 'Incident_Type'}, inplace=True)
        print("Dataset loaded successfully.")
    except FileNotFoundError:
        print(f"Error: The file at '{filepath}' was not found. Please ensure the file exists in that location.")
        return

    # --- 2. First Visualisation (Borough Hotspots) ---
    print("Generating the first visualization: Total Incidents by Borough...")
    
    # Set a professional and clean style for the plots.
    sns.set_style("whitegrid")
    
    # Calculate the number of incidents per borough and sort them in descending order.
    borough_counts = df['Borough'].value_counts().sort_values(ascending=False)
    
    # Create the figure and axes for the plot.
    plt.figure(figsize=(12, 7))
    # CORRECTED: Removed the 'hue' parameter as it was redundant and caused the error.
    ax1 = sns.barplot(x=borough_counts.index, y=borough_counts.values, palette='viridis')
    
    # Set a clear title and labels for the axes.
    ax1.set_title('Total Construction Incidents by NYC Borough', fontsize=16, fontweight='bold')
    ax1.set_xlabel('Borough', fontsize=12)
    ax1.set_ylabel('Total Number of Incidents', fontsize=12)
    
    # Add numerical counts on top of each bar for better readability.
    for p in ax1.patches:
        ax1.annotate(f'{int(p.get_height())}', 
                     (p.get_x() + p.get_width() / 2., p.get_height()), 
                     ha='center', va='center', 
                     xytext=(0, 9), 
                     textcoords='offset points',
                     fontsize=11)
    
    # Rotate the x-axis labels to prevent them from overlapping.
    plt.xticks(rotation=45, ha='right')
    # Ensure all plot elements fit nicely within the figure.
    plt.tight_layout()
    # Display the first plot.
    plt.show()

    # --- 3. Second Visualisation (Incident Type Breakdown) ---
    print("\nGenerating the second visualization: Breakdown of Top 5 Incident Types by Borough...")
    
    # Identify the top 5 most frequent incident types from the entire dataset.
    top_5_incident_types = df['Incident_Type'].value_counts().nlargest(5).index
    
    # Filter the DataFrame to include only incidents of these top 5 types.
    df_top5 = df[df['Incident_Type'].isin(top_5_incident_types)]
    
    # Group data by borough and incident type, then count the occurrences.
    # The unstack() method pivots the incident types into columns, and fill_value=0 handles missing combinations.
    incident_breakdown = df_top5.groupby(['Borough', 'Incident_Type']).size().unstack(fill_value=0)
    
    # Reorder the incident types to match the overall frequency for a more intuitive legend.
    incident_breakdown = incident_breakdown[top_5_incident_types]
    
    # Sort the boroughs based on the total incidents from the first chart for consistency.
    incident_breakdown = incident_breakdown.reindex(borough_counts.index)

    # Generate the stacked bar chart using a color-blind friendly palette.
    ax2 = incident_breakdown.plot(kind='bar', stacked=True, figsize=(14, 8), cmap='tab20b')
    
    # Set title, labels, and legend.
    ax2.set_title('Top 5 Incident Types Breakdown by Borough', fontsize=16, fontweight='bold')
    ax2.set_xlabel('Borough', fontsize=12)
    ax2.set_ylabel('Count of Incidents', fontsize=12)
    # Place the legend outside the plot for better clarity.
    ax2.legend(title='Incident Type', bbox_to_anchor=(1.02, 1), loc='upper left')
    
    # Rotate the x-axis labels.
    plt.xticks(rotation=45, ha='right')
    # Ensure all plot elements fit nicely.
    plt.tight_layout()
    # Display the second plot.
    plt.show()

# --- Main execution block ---
# This ensures the code runs only when the script is executed directly.
if __name__ == '__main__':
    # Define the file path for the dataset, assuming it's in a 'data' subdirectory.
    # The os.path.join function creates a platform-independent file path.
    file_path = os.path.join('data', 'Construction-Related_Incidents.csv')
    analyze_construction_incidents(file_path)
