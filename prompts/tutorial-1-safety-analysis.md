# Tutorial 1: Uncovering Safety Hotspots
## Objective: 
This tutorial will walk you through the process of using an AI assistant to analyse a real-world construction safety dataset. You will learn how to move from raw data to a compelling, actionable narrative that can be presented to stakeholders.

## Tool Used: 
Any conversational AI assistant capable of data analysis (e.g., ChatGPT, Gemini, Julius AI).

## Dataset: 
*nyc_construction_incidents.csv* (Available in the /data directory of this repository).

## Scenario and Context:
Imagine you are the Health and Safety Manager for a large construction firm with multiple high-rise projects across New York City. Leadership has noticed a recent uptick in safety incidents and has tasked you with preparing a report for the quarterly review.

Instead of presenting a dense spreadsheet, your goal is to create a compelling data story. This story should not only show what is happening but also reveal where the problems are concentrated and why they might be occurring, leading to a clear, data-driven recommendation for action.

We will use the "And, But, Therefore" narrative framework to structure our story.

### Understand the data

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
