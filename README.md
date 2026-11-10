
# API Data Collector

A Python-based ETL project that retrieves data from a REST API and stores it in PostgreSQL.

## Features

- Fetch data from a REST API
- Process JSON responses
- Store records in PostgreSQL
- Prevent duplicate records using primary keys
- Handle database transactions
- Manage database configuration with environment variables
- Perform automated tests using pytest

## Technology Stack

- Python
- Requests
- PostgreSQL
- Psycopg 3
- python-dotenv
- pytest

## Project Structure

- `pipeline.py` - Main execution pipeline
- `api_client.py` - REST API integration
- `db.py` - PostgreSQL operations
- `post_utils.py` - Data processing utilities
- `tests/` - Automated tests

## Requirements

- Python 3.11 or later
- PostgreSQL
- pip

## Installation

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   pip install -r requirements.txt

4. Copy `.env.example` to `.env` and configure database access.
5. Create the PostgreSQL database and `posts` table.
6. Run the pipeline:

   python pipeline.py

## Testing

Run:

   python -m pytest -v

## Data Source

JSONPlaceholder:
https://jsonplaceholder.typicode.com/

This project uses publicly available mock API data for educational purposes.

## Future Improvements

- Improved API and database error handling
- Input schema validation
- Automated scheduling
- Logging and monitoring
- Additional integration tests
- Docker deployment

## Purpose

Developed as a practical exercise in Python programming, API integration, data processing, SQL, and automated testing.
