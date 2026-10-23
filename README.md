# Indian Traffic Accident Analysis

## 📌 Project Overview

**Indian Traffic Accident Analysis** is a data analysis project developed using Python to explore traffic accident records in India. The project focuses on understanding accident patterns, severity, road and weather conditions, yearly trends, and other factors that may be associated with traffic accidents.

Using data cleaning, exploratory data analysis (EDA), and data visualization, this project transforms raw accident data into meaningful insights.

## 🎯 Project Objectives

- Analyze traffic accidents based on accident severity.
- Explore the impact of weather and road conditions on accident records.
- Identify year-wise accident trends.
- Analyze accident records by day of the week and time of day.
- Examine driver age, speed limits, casualties, and fatalities.
- Use heatmaps to visualize accident patterns and numerical correlations.
- Generate visualizations to support data-driven understanding of road safety.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and programming |
| Pandas | Data loading, cleaning, and manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization and heatmaps |
| Jupyter Notebook | Interactive analysis and documentation |

## 📂 Project Structure

```text
INDIAN-TRAFFIC-ANALYSIS/
│
├── accident_analysis.ipynb
├── data/
│   └── cleaned_accident_data.csv
├── charts/
│   ├── accident_severity.png
│   ├── weather_condition.png
│   ├── road_condition.png
│   ├── year_wise_accidents.png
│   ├── severity_casualties.png
│   ├── day_wise_accidents.png
│   ├── corr_heatmap.png
│   ├── without_corr_heatmap.png
│   ├── SpeedLimit_kdeplot.png
│   └── Pair_plot.png
└── README.md
```

*Note: The `data/` and `charts/` folders should be created and populated when running the notebook. The chart filenames above reflect the intended outputs; make sure they match the files you actually save.*

## 📊 Project Workflow

### 1. Data Loading

- Import the required Python libraries.
- Load the traffic accident dataset using Pandas.
- Display the dataset for initial inspection.

### 2. Data Understanding

- Check the number of rows and columns.
- Inspect column names and data types.
- Display the first five records.
- Identify missing values.
- Generate descriptive statistics.
- Explore accident severity, weather conditions, and road conditions.

### 3. Data Cleaning

- Investigate records where fatalities exceed casualties.
- Check zero-casualty and zero-fatality records.
- Handle missing values in traffic control presence and driver license status.
- Inspect unknown city names.
- Check for remaining missing values.
- Save the cleaned dataset as a CSV file.

### 4. Exploratory Data Analysis (EDA)

Perform exploratory analysis to understand accident patterns and distributions.

The analysis includes:
- Accident severity distribution.
- Accident records by weather condition.
- Accident records by road condition.
- Year-wise accident trends.
- Average casualties by accident severity.
- Day-wise accident distribution.
- Total casualties and fatalities.
- Average casualties per accident record.

### 5. Data Visualization

The project uses Matplotlib and Seaborn to create charts that make the findings easier to interpret.

| Visualization | Purpose |
|---|---|
| Bar Chart | Compare accident categories |
| Line Chart | Observe year-wise trends |
| Seaborn Bar Plot | Compare average casualties and day-wise records |
| Correlation Heatmap | Explore correlations between numerical variables |
| Day-Time Heatmap | Compare accident record counts across days and times |
| KDE Plot | Examine the distribution of speed limits |
| Pair Plot | Explore relationships among selected variables |

### 6. Time Data Processing

- Convert the `Time of Day` column into Python time values.
- Verify the converted values and resulting data type.

## 📈 Key Analysis Areas

This project explores the following questions:

1. Which accident severity categories occur most frequently?
2. Which weather and road conditions have the highest accident record counts?
3. How do accident records vary across years?
4. How do average casualties differ across accident severity categories?
5. Which days of the week have the most accident records?
6. How are accident records distributed across days and times?
7. What correlations exist between numerical variables?
8. How are speed limits distributed in the dataset?

*Actual findings should be added after running the notebook and reviewing its outputs. Accident record counts alone do not establish the cause of accidents.*

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/INDIAN-TRAFFIC-ANALYSIS.git
```

### Step 2: Navigate to the Project Folder

```bash
cd INDIAN-TRAFFIC-ANALYSIS
```

### Step 3: Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn jupyter
```

### Step 4: Prepare the Dataset

Place the source CSV file in your project directory, preferably inside the `data/` folder.

Update the CSV file path in the notebook to match your local file location. Also, ensure the output folders exist before saving cleaned data and charts.

### Step 5: Run the Notebook

```bash
jupyter notebook accident_analysis.ipynb
```

Open the notebook in your browser and run the cells in order.

## 📁 Dataset Information

The notebook uses a CSV dataset named `accident_prediction_india.csv`.

The analysis references fields such as:

- Accident Severity
- Weather Conditions
- Road Condition
- Driver Age
- Number of Casualties
- Number of Fatalities
- Traffic Control Presence
- Driver License Status
- City Name
- Year
- Day of Week
- Time of Day
- Speed Limit (km/h)
- Lighting Conditions

**Dataset source:** Add the original dataset source or download link here if available.

## 💡 Skills Demonstrated

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Data manipulation using Pandas
- Numerical analysis using NumPy
- Data visualization using Matplotlib and Seaborn
- Correlation analysis
- Heatmap creation
- Working with time-based data
- Extracting insights from structured datasets
- Organizing a data analytics project for GitHub

## 🚀 Future Improvements

- Develop an interactive dashboard using Streamlit.
- Add more detailed analysis of accident locations and time periods.
- Explore relationships between lighting, weather, and accident severity.
- Add filters for year, city, and accident severity.
- Include additional charts and data-driven findings.
- Investigate suitable methods for predicting accident severity, if supported by the dataset.

## 👩‍💻 Author

**Shivani Ojha**

Aspiring Data Analyst | Python | SQL | Excel | Power BI | Data Visualization

🔗 GitHub: https://github.com/ojhashivani481-prog

---

⭐ If you find this project useful, consider giving the repository a star!

