# WAP Testing Demo

Automated testing framework for web application testing, specifically designed
for mobile web view testing. The framework implements Page Object Model pattern
and includes Allure reporting integration.

## Requirements

- Python 3.11
- UV package manager
- Chrome or Firefox browser
- Docker + docker-compose

## Project Structure
wap-testing-demo/
├── framework/
│ ├── devices/ # Device management
│ ├── fixtures/ # Pytest fixtures
│ ├── pom/ # Page Object Model implementations
│ ├── reporter/ # Reporting functionality
│ └── sut/ # System Under Test configurations
├── reports/ # Test execution reports
├── tests/ # Test cases
├── utilities/ # Helper functions
└── conftest.py # Pytest configuration


## Installation

1. Clone the repository
    ```bash
    git clone https://github.com/Vladimir-Pozdniakov/wap-testing-demo.git
    ```
2. Create and activate a virtual environment:
    ```bash
    uv venv --python 3.11
    source .venv/bin/activate
    ```
3. Install dependencies using UV:
    ```bash
    uv pip install -r pyproject.toml
    ```
4. Copy the environment file and configure it:
    ```bash
    cp .env.example .env
    ```

## Running Tests
### Basic Usage
Run all tests (by default all tests will be ran in the Chrome mobile view):
```bash
pytest
```

### Browser Selection
Specify the browser for test execution:
```bash
pytest --browser chrome-mobile # Run tests with mobile Chrome
pytest --browser chrome # Run tests with desktop Chrome
pytest --browser firefox # Run tests with Firefox
```

### Test Reports
The framework generates Allure reports automatically after test execution.
To view the reports, set up the Allure server docker containers:
```bash
docker-compose up -d
```
After containers are up and running, a test run reports
will be available by url: https://localhsot:5252

## Framework Features
### Page Object Model
The framework implements the Page Object Model pattern with a robust class
that provides common functionality: `BasePage`
- Explicit and implicit wait mechanisms
- Screenshot capture
- DOM loading verification
- Element scrolling
- Dynamic element handling

### Device Management
The class handles browser configuration and provides appropriate
WebDriver instances based on the selected browser type: `DeviceManager`

### Reporting
- Automatic Allure report generation
- Screenshot capture on test failures
- Custom test properties and environment information
- Clean report directory management
