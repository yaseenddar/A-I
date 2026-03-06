# Olympic Data Analysis

An interactive data analysis and visualization application for Olympic Games data built with Streamlit. This project provides comprehensive insights into Olympic medal tallies, athlete performances, and historical trends across different countries and sports.

## Features

The application offers four main analysis sections:

### 1. Medal Tally
- View medal counts (Gold, Silver, Bronze) by country and year
- Filter by specific Olympic years or view overall statistics
- Interactive data table showing detailed medal breakdowns

### 2. Overall Analysis

Provides high-level statistics including:
- Number of Cities, Years, Events, Sports, Nations, and Athletes
- Interactive visualizations showing:

#### Countries Participating Over Time
Line chart showing the growth in participating nations across Olympic history.

![Countries over Years](https://github.com/user-attachments/assets/)  <!-- Will be updated with actual screenshot -->

#### Sports Events Over Time  
Visualization of how the number of sports has evolved throughout Olympic history.

![Sports over Years](https://github.com/user-attachments/assets/)  <!-- Will be updated with actual screenshot -->

#### Age Distribution Analysis
Kernel Density Estimation (KDE) plots showing:
- Overall athlete age distribution
- Age distribution by medal type (Gold, Silver, Bronze)
- Weight-based analysis

![Age Distribution](https://github.com/user-attachments/assets/)  <!-- Will be updated with actual screenshot -->

### 3. Country-wise Analysis

Detailed analysis for individual countries:
- Year-by-year medal performance
- Line chart showing medal trends over time
- Heatmap visualization showing performance across different sports and years

![Country Analysis - India](https://github.com/user-attachments/assets/)  <!-- Will be updated with actual screenshot -->

![India Heatmap](https://github.com/user-attachments/assets/)  <!-- Will be updated with actual screenshot -->

### 4. Athlete-wise Analysis

- Top 10 athletes by sport
- Sport-specific age distribution analysis
- Performance comparisons across different sports

## Tech Stack

- **Streamlit**: Interactive web application framework
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive visualizations and charts
- **Seaborn**: Statistical data visualization (for heatmaps)
- **Matplotlib**: Plotting library

## Project Structure

```
Olympic_Data_Analysis/
├── app.py              # Main Streamlit application
├── helper.py           # Helper functions for data processing
├── preprocess.py       # Data preprocessing functions
├── data/
│   ├── athlete_events.csv    # Olympic athlete data
│   └── noc_regions.csv       # NOC to region mapping
└── README.md
```

## Key Features of the Code

### Data Preprocessing (`preprocess.py`)
- Filters for Summer Olympics only
- Merges regional data with athlete information
- Removes duplicate medals in team events
- Creates dummy columns for medal types

### Helper Functions (`helper.py`)
- `medal_tally()`: Aggregates medal counts by region and year
- `filter_data()`: Filters data based on year and country selection
- `event_based_data()`: Analyzes participation trends
- `country_based_data()`: Country-specific medal analysis
- `country_wise_data()`: Generates sport-wise performance matrices
- `top_10_data()`: Identifies top-performing athletes

### Main Application (`app.py`)
- Sidebar filters for analysis type, year, and country
- Dynamic title generation based on filters
- Modular page logic for different analysis types
- Interactive Plotly charts with zoom and hover capabilities

## Running the Application

1. Install required dependencies:
```bash
pip install streamlit pandas plotly seaborn matplotlib
```

2. Run the Streamlit app:
```bash
streamlit run app.py
```

3. Open your browser to `http://localhost:8501`

## Data Source

The application uses historical Olympic Games data including:
- Athlete demographics (Name, Age, Height, Weight, Sex)
- Competition details (Year, City, Sport, Event)
- Medal outcomes (Gold, Silver, Bronze)
- National Olympic Committee (NOC) codes and regions

## Visualizations

### Interactive Features
- **Plotly Charts**: All line charts and distribution plots are interactive with zoom, pan, and hover tooltips
- **Data Tables**: Sortable and scrollable tables with full dataset access
- **Heatmaps**: Color-coded performance matrices for easy pattern recognition
- **Filters**: Dynamic data filtering through sidebar controls

## Analysis Insights

The application enables discovery of:
- Historical trends in Olympic participation and performance
- Country-specific strengths in particular sports
- Age demographics of medal winners
- Growth of the Olympics over time
- Sport-specific athlete characteristics

## Future Enhancements

- Add winter Olympics data
- Include gender-based analysis
- Add predictive analytics for future Games
- Export functionality for reports
- Comparative analysis between multiple countries

## Author

**Mohammad Yaseen**
- GitHub: [@yaseenddar](https://github.com/yaseenddar)

## License

This project is open source and available for educational purposes.
