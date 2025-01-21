# Project: Hotel Booking Dataset 
by: Jacob Cano, Jared Go, Anilove Canasa, Danielle Sulay
Data Set Source: Kaggle

## Overview
This project contains scripts and data files related to processing hotel booking data. The primary focus appears to be on extracting, transforming, and loading (ETL) data, as well as applying specific data transformations.

## File Contents

### Scripts
- **`transformations.py`**
  - Handles data transformation tasks.
  - Ensure that dependencies are installed before running this script.

- **`etl.py`**
  - Implements the ETL (Extract, Transform, Load) process for the dataset.
  - Manages the workflow of importing raw data, applying transformations, and saving processed data.

### Data Files
- **`processed_hotel_bookings.csv`**
  - A CSV file containing processed hotel booking data.
  - Can be opened with any text editor or spreadsheet software.

- **`processed_hotel_bookings.xlsx`**
  - An Excel file version of the processed hotel booking data.
  - Useful for analysis with Excel or similar tools.

## Usage

### Prerequisites
1. Ensure you have Python installed.
2. Install required Python libraries by running:
   ```bash
   pip install -r requirements.txt
   ```
   (If a `requirements.txt` file is not provided, manually install the necessary libraries used in the scripts.)

### Running the Scripts
1. **Transformations**:
   Run `transformations.py` to apply transformations to your dataset:
   ```bash
   python transformations.py
   ```

2. **ETL Process**:
   Execute `etl.py` to perform the ETL process:
   ```bash
   python etl.py
   ```

### Data
- Use the provided processed data files (`.csv` or `.xlsx`) for further analysis or reporting.

## Notes
- Ensure all file paths in the scripts are updated to match your working directory.
- Refer to comments within the scripts for more detailed explanations of the code functionality.

## License
Include details about the license if applicable.

## Author
Add information about the author or contributors if required.
