# **Power Plant Frequency Forecast**

Power Plant Frequency Forecast is a machine learning-based project designed to predict power grid frequency variations using advanced deep learning techniques.

---

## **ARIMA-LSTM Hybrid Model**

### **Overview**

This project implements an ARIMA-LSTM hybrid model for time series forecasting. By combining **ARIMA** (AutoRegressive Integrated Moving Average) and **LSTM** (Long Short-Term Memory), the model leverages the strengths of both statistical and deep learning approaches, resulting in improved predictive accuracy.

---

## **Maha Data Processing**

### **Data Extraction**

#### **Source Files**
- The raw data originates from frequency profile reports in **PDF format**.
- The script **`PDFtoCSV.py`** is used to extract and structure the data efficiently.

#### **Extraction Process**
1. **Extract Text**: The script utilizes `pdfplumber` to read text from PDF files.
2. **Parse Data**:
   - Identifies column headers (days) and rows (time blocks with frequency values).
   - Converts the extracted data into a structured tabular format.
3. **Save as CSV**:
   - The processed data is saved as a CSV file.
   - The file is transposed to ensure proper data organization.

### **Data Transformation and Merging**

#### **Monthly CSV Processing**
- The script **`transform.py`** processes each monthly CSV file stored in the **`transformed_data2024/`** folder.
- The data is reformatted to include proper date representation in **DD-MM-YYYY** format.

#### **Merging Process**
- All monthly CSV files are merged into a single dataset.
- The final merged dataset is saved as **`maha_final_data.csv`**.

### **Final Output**
The **`maha_final_data.csv`** file is the structured dataset containing frequency profile data for all processed months in 2024.

---

## **Dependencies**

To run the scripts, ensure the following dependencies are installed:
```bash
pip install pandas pdfplumber
```

### **Prerequisites**
Before running the notebook, install the required dependencies:
```bash
pip install numpy pandas matplotlib scikit-learn statsmodels tensorflow keras
```

---

## **How to Run**

1. Clone the repository or download the notebook.
2. Install the required dependencies.
3. Open the notebook using Jupyter Notebook or Jupyter Lab:
   ```bash
   jupyter notebook arima_lstm.ipynb
   ```
4. Execute the cells in sequence to preprocess the data, train the model, and visualize the results.

---

## **Model Details**

- **ARIMA Model**: Captures linear trends and seasonality in the data.
- **LSTM Model**: Learns complex nonlinear dependencies in time series data.
- **Hybrid Approach**: ARIMA models the linear component, while LSTM captures residual nonlinear patterns.

---

## **Results**

The final model's performance is evaluated using common error metrics such as:
- **RMSE** (Root Mean Squared Error)
- **MAE** (Mean Absolute Error)

Graphical analysis is also used to assess forecast accuracy.

---

## **Future Improvements**

- **Hyperparameter tuning** for better performance.
- **Forecasting for an entire month** to improve long-term accuracy.
- **Testing on larger and more complex datasets**.
- **Experimenting with other hybrid models**, such as **LSTM + CNN**.

---

This project aims to enhance power grid stability by providing precise frequency variation forecasts, ultimately contributing to a more efficient energy management system.

