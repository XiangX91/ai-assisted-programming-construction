# Tutorial 1: Uncovering Safety Hotspots
## Objective: 
This tutorial puts the principles of this chapter into practice. We will walk through the "AI-Powered Data Storytelling" workflow to transform a raw dataset into a compelling narrative that drives decision-making. This exercise is designed for construction professionals and students, demonstrating how to partner with an AI assistant to solve a real-world problem without needing a deep background in coding.

## Tool Used: 
Any conversational AI assistant capable of data analysis (e.g., ChatGPT, Gemini, Julius AI).

## Dataset: 
*nyc_construction_incidents.csv* (Available in the /data directory of this repository), from https://catalog.data.gov/dataset/construction-related-incidents

This dataset includes construction-related incidents recorded through the US Department of Buildings (DOB) Incident Database. Updated on August 11, 2025.

## The Human-AI-Code Triad in Action: 
Before we begin, let's revisit a key concept: the Human-AI-Code Triad. This tutorial is a perfect example of this collaborative partnership:
* **Human (You):** As the domain expert (a construction safety manager), you define the problem, provide the necessary context, and critically evaluate the results. Your role is strategic.   

* **AI (Your Assistant):** The AI acts as your "pair programmer" or data analyst. It handles the technical tasks of data processing, visualisation, and code generation based on your natural language instructions.   

* **Code (The Medium):** The Python script we generate is the tangible output that executes our analysis, turning our strategic goals into a functional reality.

This process allows you to focus on high-level problem decomposition and "context engineering", the art of giving the AI clear instructions rather than getting lost in the syntax, directly addressing the "code fear" many professionals experience.

## Scenario and Context:
You are the Health and Safety Manager for a large construction firm overseeing multiple high-rise projects in New York City. Leadership has tasked you with preparing a report on a recent increase in safety incidents. Instead of a static spreadsheet, your goal is to create a compelling data story that identifies safety hotspots and provides a clear, data-driven recommendation for action.

We will follow the Construction Data Analysis Workflow and the "And, But, Therefore" narrative framework to structure our story.   

#### Step 1: Data Exploration

First, we need to understand our data. We will provide the dataset to our AI assistant and ask it to perform an initial exploration. This step establishes the "Setup" of our story by defining the scope of our data.

**Prompt 1: Data Integration and Exploration (The Setup)**
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

#### Step 2: Pattern Recognition and Visualisation (The Conflict)

With the context established, we now search for the "Conflict" in our story—the key insight or problem that needs attention. We'll ask our AI assistant to generate visuals to expose patterns in the data.

**Prompt 2: Identify Geographical Hotspots**

This prompt asks the AI to create the first key visual for our story.

```markdown
CONTEXT & OBJECTIVE
Based on the nyc_construction_incidents.csv data we've already loaded, I need to identify if some geographical regions have more incidents than others. This will be the first key visual for my report.

INSTRUCTIONS & STEPS
1. Calculate the total number of incidents for each borough.
2. Generate a bar chart that displays the total number of incidents per borough.
3. Ensure the bar chart is clearly labelled, with a title like "Total Construction Incidents by NYC Borough".
4. Sort the bars in descending order to identify the borough with the most incidents easily.
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

#### Step 3: Narrative Development (The Resolution)
With our AI-generated visuals, we can now construct a compelling story that leads to a clear resolution or call to action.

*   **And:** "We diligently monitor safety incidents across all our projects in New York City, **and** our data encompasses a wide range of incident types across all five boroughs."
    *   *(This is supported by the output of Prompt 1)*

*   **But:** "**But**, our analysis clearly shows that Manhattan accounts for over 350 reported incidents. A further breakdown reveals that the majority of these are specifically related to 'Worker Fell'."
    *   *(This is the key insight from the visuals generated by Prompts 2 and 3)*

*   **Therefore:** "**Therefore**, I recommend we immediately initiate a comprehensive review of fall protection systems and working-at-heights protocols on our Manhattan sites. We should also schedule mandatory refresher safety training for all personnel, focusing on fall prevention and the proper use of personal fall arrest systems."
    *   *(This is the actionable recommendation derived from the story)*

This narrative, supported by the AI-generated visuals, transforms a simple data analysis into a powerful tool for driving strategic decisions in construction safety management.

#### Step 4: From Conversation to Code

Now, let's create a reusable artefact from our analysis. We can ask our AI assistant to generate a complete Python script to perform this analysis automatically in the future.

**Prompt 4: Python Code Generation**
```markdown
PERSONA / ROLE
You are an expert Python data scientist specialising in data visualisation using the pandas, matplotlib, and seaborn libraries. Your code must be clean, well-commented, and easy for a non-expert to understand.

CONTEXT & OBJECTIVE
Using the `nyc_construction_incidents.csv` dataset, I need a Python script that generates two key visualisations for my safety report: one showing incident hotspots by borough, and another breaking down the incident types within those hotspots.

INSTRUCTIONS & STEPS
1.  **Load Data:** Import necessary libraries and load `nyc_construction_incidents.csv`. Include error handling for a `FileNotFoundError`.
2.  **First Visualisation (Borough Hotspots):**
      *   Generate a bar chart showing the total number of incidents per borough, sorted in descending order.
      *   Include a clear title, axis labels, and numerical counts on top of each bar.
3.  **Second Visualisation (Incident Type Breakdown):**
      *   Identify the top 5 most frequent 'Incident\_Type' values from the entire dataset.
      *   Generate a stacked bar chart where each bar represents a borough, segmented by the count of these top 5 incident types.
      *   Include a clear title, axis labels, and a legend.
4.  **Display Plots:** Ensure the plots are displayed separately and are well-formatted using `plt.tight_layout()`.

OUTPUT FORMAT
Please provide the final output as a single, complete Python code block with comments explaining each major step. 
```
The generated script is available in the /scripts directory of this repository.

#### Step 5: Adopting a "Trust but Verify" Mindset
As emphasised throughout this chapter, the most significant risk in AI-assisted programming is not code that fails, but code that runs perfectly while producing a logically incorrect result. All AI-generated code must be treated as an unverified draft.   

Before using this script in a real report, apply a simple validation framework:
1. **Manual Code Review:** Read through the script. Does it make sense? Is it selecting the correct columns (Borough, Incident_Type)? This first-pass review can catch obvious errors.
2. **Cross-Verification:** Manually filter the *nyc_construction_incidents.csv* file in a spreadsheet program. Does the total count for Manhattan match the number on the AI-generated chart? Verifying one or two key data points provides confidence in the overall logic.
3. **Incremental Execution:** Run the code in a Jupyter Notebook (available in the /notebooks directory) cell by cell. After the data is loaded, display the first few rows to ensure it's correct. After the counts are calculated, print the results to check them before plotting. This helps isolate where a potential error might occur.

By adopting this mindset, you leverage the speed of AI while maintaining the critical oversight and professional responsibility required in the construction industry.   
