: Automated Test Cases for Zudu AI

This repository contains a collection of automated test cases for the Zudu AI platform using Selenium. The goal is to ensure the reliability and quality of Zudu AI features through comprehensive end-to-end testing.

## Features

- Automated browser-based tests
- Easy-to-read test case documentation
- Continuous integration ready

## Getting Started

1. Clone this repository https://github.com/muhammadshamaas2022skipq/Zudu-AI-TestCases
2. Install dependencies as described in the setup guide.
3. Run the test suite using your preferred Selenium runner.

## Cloning the Repository

To clone this repository to your local machine, open your terminal and run:

```bash
git clone https://github.com/muhammadshamaas2022skipq/Zudu-AI-TestCases.git
```

This will create a local copy of the repository in your current directory.

## Installation

To activate virtual environment, run:

```bash
python3 -m venv venv
source ./venv/bin/activate
pip install selenium sounddevice scipy
```

## Environment Variables

Before running the tests, create a `.env` file in the project root.

Replace the values with your actual Selenium server URL and credentials as needed.

```bash
PROJECT_ID=...
API_KEY=...
URL=...
username=...
Password=...
```

## Running Tests

- To run the test suite locally, execute:

    ```bash
    python BrowserBase/local.py
    ```

- To run the test suite on Browser Base, execute:

    ```bash
    python BrowserBase/browser_base.py
    ```

Make sure you have Python and pip installed on your system.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements.
