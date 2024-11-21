
# TVC Data Ingestor

A simple GUI application to import data from various traffic surveys into a SQLite database.

## Features

- Supports multiple survey types
- Automatically generates a template for the selected survey type
- Allows the user to select multiple files to import
- Creates a new SQLite database based on the selected survey type

## Installation

1. Clone the repository using `git clone https://github.com/gsulay/tvc-data-ingestor.git`
2. Install the required dependencies using `pip install -r requirements.txt`
3. Run the application using `python main.py`

## Usage

1. Select the survey type from the dropdown menu
2. Click on the "Generate Template" button to create a sample template
3. Click on the "Add Survey" button to select multiple files to import
4. Click on the "Create Database" button to create a new SQLite database

## Known Issues

- The application does not handle errors well
- The application does not handle large files well

## Contributing

Contributions are welcome! Please create a pull request if you have any fixes or features to add.

## License

This project is licensed under the MIT License. See the LICENSE file for details
