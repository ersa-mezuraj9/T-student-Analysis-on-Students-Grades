# T-student Analysis on Students' Grades

This repository provides a comprehensive analysis of students' grades using T-Student statistical methods. The goal is to explore, visualize, and statistically analyze the performance of students across various courses or groups, providing actionable insights for educators and stakeholders.

## Project Overview

The project focuses on:
- Applying T-Student tests to compare student performance between groups.
- Visualizing grade distributions.
- Extracting statistical significance and insights from students' academic results.

## Features

- Data preprocessing and cleaning
- Exploratory data analysis (EDA)
- T-Student test implementation for comparing groups
- Statistical visualization (histograms, box plots, etc.)
- Summary of findings and implications

## Installation

**Clone the repository:**
   ```bash
   git clone https://github.com/ersa-mezuraj9/T-student-Analysis-on-Students-Grades.git
   cd T-student-Analysis-on-Students-Grades
   ```

## Usage

1. Place your dataset in the `data/` directory (see [Data](#data) for requirements).
2. Run the main analysis script:
   ```bash
   python main.py
   ```
3. View outputs in the `results/` directory.

## Data

- The dataset should be a CSV file containing students' grades and relevant group information (e.g., gender, class, school, etc.).
- Example columns: `StudentID, Group, Grade`
- Place your data file in the `data/` directory.

## Analysis Methods

- **Exploratory Data Analysis (EDA):** Descriptive statistics and visualizations.
- **T-Student Test:** Compare means between two groups to determine statistical significance.
- **Visualization:** Histograms, box plots, and group comparisons.

## Results

- Summary statistics and test results will be saved in the `results/` folder.
- Visualizations will be available as PNG files for presentations or reports.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
