# PowerPlantFreqForecast
Power Plant Frequency Forecast is a machine learning-based project that predicts power grid frequency variations using advanced deep learning techniques.

# ARIMA-LSTM Hybrid Model

## Overview

This project implements an ARIMA-LSTM hybrid model for time series forecasting. The combination of ARIMA (AutoRegressive Integrated Moving Average) and LSTM (Long Short-Term Memory) leverages the strengths of both statistical and deep learning approaches to improve predictive accuracy.

## Prerequisites

Ensure you have the following dependencies installed before running the notebook:

```bash
pip install numpy pandas matplotlib scikit-learn statsmodels tensorflow keras
```

## Dataset

The model requires a time series dataset. If a dataset is not provided within the notebook, ensure to update the file path accordingly.

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
- Forecating
- Testing on larger and more complex datasets.
- Experimenting with other hybrid models Like LSTM+CNN.

