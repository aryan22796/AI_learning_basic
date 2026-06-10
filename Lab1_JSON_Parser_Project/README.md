# Lab1_JSON_Parser_Project

## Overview
This project demonstrates Day 1 Python fundamentals in a real lab structure. It reads customer records from JSON input, filters active customers, builds a text report, and writes the output to a file.

## Folder Structure
```
Lab1_JSON_Parser_Project/
├── data/
│   └── customers.json
├── output/
│   └── report.txt
├── src/
│   ├── reader.py
│   ├── processor.py
│   └── main.py
└── README.md
```

## Files
- `data/customers.json`: sample input records.
- `src/reader.py`: safe file reading and report writing.
- `src/processor.py`: filtering and formatting logic.
- `src/main.py`: orchestration, error handling, and execution.
- `output/report.txt`: generated report output.

## Setup
1. Create a Python virtual environment:
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
2. Install dependencies (no extra packages are required for this lab).
3. Run the project:
   - `cd Lab1_JSON_Parser_Project/src`
   - `python main.py`

## Expected Output
The project writes `output/report.txt` with a summary of active customers and the total count.

## Learning Goals
- Read JSON input
- Filter and transform records using functions
- Use list comprehensions for concise processing
- Write a formatted output report
- Handle errors in file reading and JSON parsing
