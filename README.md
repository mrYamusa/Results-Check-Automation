LMU Results Check Automation
=====================================

## Introduction

This project is a Python script that automates the process of checking exam results from the Landmark University `FP portal`. It uses Selenium WebDriver to interact with the website, navigate through the login process, and select the desired session and semester to retrieve the results.

## Features

### Automation

* Automate login to the Landmark University website
* Navigates to the Exams & Results page
* Selects the desired session (e.g., 2023/2024) and semester (e.g., Alpha)
* Retrieves the exam results
* Closes the browser session after completion

## How to Use

### Prerequisites

* Install the required dependencies: `selenium` and `webdriver-manager` (for ChromeDriver)

### Running the Script

1. Update the `username` and `password` variables with your actual login credentials
2. Run the script using Python (e.g., `python script.py`)
3. The script will automatically navigate through the website, retrieve the results, and close the browser session

### Note

* This script is intended for personal use only and should not be used for any malicious purposes.
* The script may not work if the website structure or login process changes.
* You may need to adjust the script to accommodate any changes to the website.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
