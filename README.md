# COVID-19, Influenza, and Pneumonia Deaths Analysis

This project aims to analyze and visualize the monthly COVID-19, influenza, and pneumonia deaths data using Python. It generates interactive heatmaps to help understand the trends and patterns in these mortality rates.

## Data Source

The data used in this analysis is sourced from [CDC](https://data.cdc.gov/NCHS/Provisional-COVID-19-Deaths-by-Sex-and-Age/9bhg-hcku). It includes the number of deaths for each month and year, as well as the corresponding data as of date.

## Prerequisites

Before running the Python code, ensure you have the following packages installed:

- pandas
- seaborn
- matplotlib

You can install them using `pip`:

```bash
pip install pandas seaborn matplotlib
```

## Usage

1. Clone this repository:

```bash
git clone https://github.com/IAmJuniorB/COVID-Analysis.git
cd COVID-Analysis
```
1. Place the data file filtered_deaths.csv in the project folder.

2. Run the Python script:

```bash
python CovidDeaths.py
python PnaDeaths.py
python InfluenzaDeaths.py
```

The scripts will generate three heatmaps for COVID-19, influenza, and pneumonia deaths as of the latest data (7/12/23).

## Heatmaps

### COVID-19 Deaths

The COVID-19 heatmap illustrates the monthly deaths for each year, with a custom color scale. The highest monthly death count is highlighted.

![Will update with image](path/to/image.png)

### Influenza Deaths

The influenza heatmap illustrates the monthly deaths for each year, with a custom color scale. The highest monthly death count is highlighted.

![Will update with image](path/to/image.png)

### Pneumonia Deaths

The pneumonia heatmap illustrates the monthly deaths for each year, with a custom color scale. The highest monthly death count is highlighted.

![Will update with image](path/to/image.png)
