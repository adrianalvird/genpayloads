is# XSS Payload Generator

## Overview
This tool generates advanced XSS payloads that are context-aware, mutated, and designed to bypass WAFs. The payloads are tested against a target URL, and successful ones are reported.

## Structure
- **config/**: Configuration settings
- **payloads/**: Payload generation logic
- **generator/**: Main tool functionality
- **reports/**: Reporting functionality
- **utils/**: Helper functions
- **tests/**: Unit and integration tests
- **scripts/**: Executable scripts

## Usage
1. Install dependencies:
   ```sh
   pip install -r requirements.txt

2. Run Genpaylaods:
    ```sh
    python scripts/run_generator.py

3. Run the tests:
    ``` sh
    python scripts/run_tests.py

