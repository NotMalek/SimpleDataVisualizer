# Simple Data Visualizer

A performance benchmarking tool designed to compare and visualize the execution speed differences between Pandas and Polars data processing libraries. This interactive dashboard allows users to analyze sales data while measuring the computational efficiency of both libraries.

## Features

- Interactive dashboard with multiple visualization types:
  - Daily revenue trends
  - Product-wise revenue analysis
  - Store performance comparison
  - Payment method distribution
  - Product quantity analysis
  - Unit price analysis
- Month-wise data filtering
- Real-time performance measurement
- Side-by-side implementation in both Pandas and Polars

## Technologies Used

- **Python Libraries**:
  - Pandas: For traditional data manipulation
  - Polars: For high-performance data processing
  - Streamlit: For interactive web interface
  - Plotly Express: For dynamic visualizations

## Project Structure

```
SimpleDataVisualizer/
├── README.md
├── dash.iml
├── dash_pandas.py    # Pandas implementation
├── dash_polars.py    # Polars implementation
└── sales_data.csv    # Sample dataset
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/SimpleDataVisualizer.git
cd SimpleDataVisualizer
```

2. Install required dependencies:
```bash
pip install pandas polars streamlit plotly
```

## Usage

1. Start the Pandas version:
```bash
streamlit run dash_pandas.py
```

2. Start the Polars version:
```bash
streamlit run dash_polars.py
```

3. Use the sidebar month selector to filter data
4. Compare the execution time displayed at the bottom of each dashboard

## Data Format

The application expects a CSV file (`sales_data.csv`) with the following columns:
- SALE_DATE: Date of sale (YYYY-MM-DD format)
- STORE: Store identifier
- PRODUCT: Product name
- QUANTITY: Number of units sold
- UNIT_VALUE: Price per unit
- TOTAL_VALUE: Total sale value
- PAYMENT_METHOD: Method of payment

## Performance Comparison

The main differences between the Pandas and Polars implementations:

1. **Data Loading**:
   - Pandas: Uses `pd.read_csv()` with delimiter and encoding specifications
   - Polars: Uses `pl.read_csv()` with similar parameters but typically faster processing

2. **Date Processing**:
   - Pandas: Uses `pd.to_datetime()` and datetime accessors
   - Polars: Uses `str.strptime()` and datetime functions

3. **Aggregations**:
   - Pandas: Uses familiar `.groupby()` with method chaining
   - Polars: Uses more explicit `.groupby()` with `agg()` functions
