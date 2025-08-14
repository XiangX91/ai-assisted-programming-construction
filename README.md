# An Introduction to AI-Assisted Programming

## Getting Started: Setup and Installation
To run the analysis and visualisations on your local machine, you will need to have Conda installed. Follow these steps to set up the project environment.

* Clone the Repository
```bash
git clone https://github.com/XiangX91/ai-assisted-programming-construction.git
```

* Create and Activate the Conda Environment

This repository includes an `environment.yml` file that contains all the necessary dependencies. Create the Conda environment from this file:

```bash
conda env create -f environment.yml
```
This command will create a new Conda environment named construction-viz and install all the required packages.

Once the environment is created, activate it:

```bash
conda activate construction-viz
```
You will now be in the project's dedicated Python environment, and your terminal prompt should change to show (construction-viz).

* Run the Python Scripts

With the environment activated, you can now run the Python scripts from the /scripts directory to conduct the analysis and generate the visualisations.

To run the main analysis script:

```bash
python scripts/Tutorial_1/safety_hotspot_analysis.py #Please change the .py you would like to run
```

* Deactivate the Conda Environment

```bash
conda deactivate construction-viz
```
