# 🏅 A-I — AI & Deep Learning Journey

> A personal learning repository covering AI, Deep Learning, and Data Analysis projects built with Python, Streamlit, and Jupyter Notebooks.

---

## 📁 Repository Structure

```
A-I/
└── DeepLearning/
    ├── Models/
    │   ├── Potato_Disease_Model/     # CNN model to detect potato plant diseases
    │   └── Word_Generator/           # Deep learning word generation model
    └── Projects/
        └── Olympic_Data_Analysis/    # Streamlit app for Olympics data analysis
            ├── app.py
            ├── helper.py
            ├── preprocess.py
            ├── Olympics_Analysis.ipynb
            └── data/
                ├── athlete_events.csv
                └── noc_regions.csv
```

---

## 🏆 Project 1 — Olympic Data Analysis (Streamlit App)

An interactive web application built with **Streamlit** that lets you explore 120+ years of Olympic Games data.

### Features

| Analysis Mode | Description |
|---|---|
| **Medal Tally** | View gold, silver, bronze, and total medal counts filtered by year and country |
| **Overall Analysis** | Stats on cities, years, events, sports, nations, and athletes over time |
| **Country-wise Analysis** | Year-by-year medal trend line chart + sport-wise heatmap for any country |
| **Athlete-wise Analysis** | Top 10 athletes per sport + age distribution curves by medal type |

### Tech Stack

- **Streamlit** — interactive web UI
- **Pandas** — data manipulation
- **Plotly Express & Figure Factory** — interactive charts and distribution plots
- **Seaborn & Matplotlib** — heatmaps and static visualizations

### Data

- `athlete_events.csv` — historical Olympic athlete records
- `noc_regions.csv` — NOC country code to region mapping

### How to Run

```bash
# Clone the repo
git clone https://github.com/yaseenddar/A-I.git
cd A-I/DeepLearning/Projects/Olympic_Data_Analysis

# Install dependencies
pip install streamlit pandas plotly seaborn matplotlib

# Run the app
streamlit run app.py
```

### App Walkthrough

**Sidebar Filters:**
- Select Analysis Type (Medal Tally / Overall / Country-wise / Athlete-wise)
- Filter by Year (Overall or specific Olympic year)
- Filter by Country

**Preprocessing (`preprocess.py`):**
- Filters for Summer Olympics only
- Merges region data on NOC code
- Removes duplicate team-event medals
- Creates medal dummy columns

**Helper Functions (`helper.py`):**
- `medal_tally()` — aggregates medals by region and year
- `filter_data()` — applies year and country filters
- `event_based_data()` — tracks countries/sports growth over years
- `country_based_data()` — year-wise medal count for a country
- `country_wise_data()` — sport-wise medal pivot for heatmap
- `top_10_data()` — returns top 10 athletes by medal count for a sport
- `generate_title()` — generates dynamic page titles

---

## 🤖 Model 1 — Potato Disease Model

A Convolutional Neural Network (CNN) trained to classify potato plant leaf images into:
- Healthy
- Early Blight
- Late Blight

---

## 📝 Model 2 — Word Generator

A deep learning model that generates text/words using sequential learning techniques.

---

## 🛠️ Languages & Tools

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=flat&logo=jupyter&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)

---

## 👨‍💻 Author

**Mohammad Yaseen** — [@yaseenddar](https://github.com/yaseenddar)

> "This is the starting of the wonderful learning about AI and deep learning."
