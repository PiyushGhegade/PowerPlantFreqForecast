# PowerPlantFreqForecast
Power Plant Frequency Forecast is a machine learning-based project that predicts power grid frequency variations using advanced deep learning techniques.

# ARIMA-LSTM Hybrid Model

## Overview

This project implements an ARIMA-LSTM hybrid model for time series forecasting. The combination of ARIMA (AutoRegressive Integrated Moving Average) and LSTM (Long Short-Term Memory) leverages the strengths of both statistical and deep learning approaches to improve predictive accuracy.

# Maha Data Processing

## Data Extraction
### Source Files
- The raw data originates from frequency profile reports in PDF format.
- The script `pdf_to_csv_with_proper_heading.py` is used to extract and structure the data.

### Extraction Process
1. **Extract Text**: The script utilizes `pdfplumber` to read text from PDF files.
2. **Parse Data**:
   - Identifies column headers (days) and rows (time blocks with frequency values).
   - Converts extracted data into a structured tabular format.
3. **Save as CSV**:
   - The processed data is saved as a CSV file.
   - The file is transposed to organize the data properly.

## Data Transformation and Merging
### Monthly CSV Processing
- The script `transposedata.py` processes each monthly CSV from the `transformed_data2024/` folder.
- The data is reformatted to include proper date representation in `DD-MM-YYYY` format.

### Merging Process
- All monthly CSV files are merged into a single dataset.
- The final merged file is saved as `maha_data.csv`.

## Final Output
The `maha_data.csv` file is the final structured dataset containing frequency profile data for all processed months in 2024.

## Dependencies
To run the scripts, ensure the following dependencies are installed:
```bash
pip install pandas pdfplumber
```

## Prerequisites

Ensure you have the following dependencies installed before running the notebook:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels tensorflow keras
```

## How to Run

1. Clone the repository or download the notebook.
2. Install the required dependencies.
3. Open the notebook using Jupyter Notebook or Jupyter Lab:
   ```bash
   jupyter notebook arima_lstm.ipynb
   ```
4. Execute the cells in sequence to preprocess data, train the model, and visualize the results.

## Model Details

- **ARIMA Model**: Captures linear trends and seasonality in the data.
- **LSTM Model**: Learns complex nonlinear dependencies in time series data.
- **Hybrid Approach**: ARIMA is used to model the linear component, while LSTM captures residual nonlinear patterns.

## Results

The final model's performance is evaluated using common error metrics such as RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error). Graphical analysis helps in assessing the forecast accuracy.

## Future Improvements

- Hyperparameter tuning for better performance.
- Forecating of a month
- Testing on larger and more complex datasets.
- Experimenting with other hybrid models Like LSTM+CNN.

