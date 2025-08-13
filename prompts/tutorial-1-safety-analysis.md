# Tutorial 1: Uncovering Safety Hotspots
## Objective: 
This tutorial will walk you through the process of using an AI assistant to analyse a real-world construction safety dataset. You will learn how to move from raw data to a compelling, actionable narrative that can be presented to stakeholders.

## Tool Used: 
Any conversational AI assistant capable of data analysis (e.g., ChatGPT, Gemini, Julius AI).

## Dataset: 
*nyc_construction_incidents.csv* (Available in the /data directory of this repository), from https://catalog.data.gov/dataset/construction-related-incidents

## Scenario and Context:
Imagine you are the Health and Safety Manager for a large construction firm with multiple high-rise projects across New York City. Leadership has noticed a recent uptick in safety incidents and has tasked you with preparing a report for the quarterly review.

Instead of presenting a dense spreadsheet, your goal is to create a compelling data story. This story should not only show what is happening but also reveal where the problems are concentrated and why they might be occurring, leading to a clear, data-driven recommendation for action.

We will use the "And, But, Therefore" narrative framework to structure our story.

### Understand the Data and Design the Narrative

#### Step 1: Data Exploration

First, we need to understand our data. We will provide the dataset to our AI assistant and ask it to perform an initial exploration. This step establishes the "Setup" of our story by defining the scope of our data.

**Prompt 1: Initial Data Analysis**
Copy and paste the following prompt into your AI assistant. Make sure to upload the *nyc_construction_incidents.csv* file when prompted.

```markdown
PERSONA / ROLE
You are an expert data analyst with a specialisation in construction management and workplace safety. Your task is to help me analyse a dataset of construction safety incidents to uncover key insights.

CONTEXT & OBJECTIVE
I am analysing a dataset named nyc_construction_incidents.csv, which contains records of construction-related safety incidents in New York City. My objective is to understand the overall landscape of these incidents.

INSTRUCTIONS & STEPS
1. Load the nyc_construction_incidents.csv dataset.
2. Provide a high-level summary of the data, including the total number of records and the names of the columns.
3. Check for any missing or null values in the dataset and report your findings.
4. List all the unique values for the 'Borough' column to show the geographical scope.
5. List all the unique values for the 'Incident_Type' column to show the different categories of incidents.

OUTPUT FORMAT
Provide the response in a clear, sectioned format. Use bullet points for lists.
```

#### Step 2: Generating Visual Insights

Now that we understand our data, we need to find the "Conflict" in our story. Where is the problem? We will ask our AI assistant to create visualizations to expose patterns and identify hotspots. This is an iterative process.

**Prompt 2: Identify Geographical Hotspots**

This prompt asks the AI to create the first key visual for our story.

```markdown
CONTEXT & OBJECTIVE
Based on the nyc_construction_incidents.csv data we've already loaded, I need to identify if certain geographical areas have more incidents than others. This will be the first key visual for my report.

INSTRUCTIONS & STEPS
1. Calculate the total number of incidents for each borough.
2. Generate a bar chart that displays the total number of incidents per borough.
3. Ensure the bar chart is clearly labelled, with a title like "Total Construction Incidents by NYC Borough".
4. Sort the bars in descending order to easily identify the borough with the most incidents.
```
**Prompt 3: Drill Down into the Problem Area**

The first chart will likely show that one borough has significantly more incidents. Now, we drill down to understand what kind of incidents are happening there. This follow-up prompt builds on the previous result.

```markdown
CONTEXT & OBJECTIVE
The previous bar chart showed that [Manually enter the name of the borough with the most incidents here, e.g., Manhattan] has the highest number of incidents. Now, I need to understand the types of incidents that are most common in that specific borough.

INSTRUCTIONS & STEPS
1. Filter the dataset to include only the incidents that occurred in [Manually enter the same borough name again].
2. From this filtered data, calculate the frequency of each 'Incident_Type'.
3. Generate a pie chart to show the distribution of incident types for that borough.

Make sure the pie chart includes percentage labels for each slice and has a clear title, such as "Distribution of Incident Types in".
```

#### Step 3: Building the Narrative
With our AI-generated visuals, we can now construct a compelling story that leads to a clear resolution or call to action.

*   **And:** "We diligently monitor safety incidents across all our projects in New York City, **and** our data encompasses a wide range of incident types across all five boroughs."
    *   *(This is supported by the output of Prompt 1)*

*   **But:** "**But**, our analysis clearly shows that Manhattan accounts for over 350 reported incidents. A further breakdown reveals that the majority of these are specifically related to 'Worker Fell'."
    *   *(This is the key insight from the visuals generated by Prompts 2 and 3)*

*   **Therefore:** "**Therefore**, I recommend we immediately initiate a comprehensive review of fall protection systems and working-at-heights protocols on our Manhattan sites. We should also schedule mandatory refresher safety training for all personnel, focusing on fall prevention and the proper use of personal fall arrest systems."
    *   *(This is the actionable recommendation derived from the story)*

This narrative, supported by the AI-generated visuals, transforms a simple data analysis into a powerful tool for driving strategic decisions in construction safety management.

#### Step 4: Visualise according to the refined narrative

To bring your tutorial to life, you'll need a Python script that can perform the analysis and create the visualisations we've discussed. Below is a complete, well-documented Python script designed to be run in an environment like a Jupyter Notebook. 

**Prompt 4: Python generation**
Here is a well-structured prompt you can use to ask an AI assistant to generate the script above. This demonstrates the "context engineering" we discussed, providing the AI with a clear role, objective, and detailed instructions to get a high-quality result.


```markdown
PERSONA / ROLE
You are an expert Python data scientist specialising in data visualisation using the pandas, matplotlib, and seaborn libraries. Your code should be clean, well-commented, and easy for a non-expert to understand.

CONTEXT & OBJECTIVE
I am working with a dataset named nyc_construction_incidents.csv. This dataset contains information about construction safety incidents in New York City, including columns for 'Borough' and 'Incident_Type'. My objective is to create a Python script that generates two visualisations to identify and analyse safety hotspots.

INSTRUCTIONS & STEPS
Please generate a complete Python script that performs the following actions in sequence:
1. Load Data: Import the necessary libraries (pandas, matplotlib.pyplot, seaborn) and load the nyc_construction_incidents.csv file into a pandas DataFrame. Include basic error handling for a FileNotFoundError.
2. Create First Visualisation (Borough Hotspots):
* Calculate the total number of incidents for each of the five boroughs.
* Generate a bar chart showing these totals.
* The chart should have a clear title: "Total Construction Incidents by NYC Borough".
* Label the X and Y axes appropriately.
* Add the numerical count on top of each bar for clarity.
* Use a professional colour palette (e.g., "viridis").
3. Create Second Visualisation (Incident Type Breakdown):
* First, identify the top 5 most frequent 'Incident_Type' values from the entire dataset.
* Create a new DataFrame that is filtered only to include rows with these top 5 incident types.
* Generate a stacked bar chart where each bar represents a borough.
* Each bar should be segmented by the count of the top 5 incident types.
* The chart should have a clear title: "Breakdown of Top 5 Incident Types by NYC Borough".
* Ensure the legend is clear and placed appropriately.
4. Please make sure to call plt.show() after each plot is generated so they display separately. Use plt.tight_layout() to ensure labels do not overlap.

OUTPUT FORMAT
Provide the final output as a single, complete Python code block. Add comments within the code to explain each major step.
```
The generated script is available in the /scripts directory of this repository
