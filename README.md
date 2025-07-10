Automation Final Project – Aluminum + Browser-use aviel katz
Features
Support for Aluminum and Browser-use frameworks (mocked with Selenium)
Unified configuration system (YAML)
Logging and reporting
Modular page objects
CLI parameter support
Run tests
pytest tests/ --html=reports/report.html --self-contained-html
Project Structure
configs/ – Global config file (YAML)
runners/ – Wrappers for Aluminum and Browser-use
aluminum/ – Local mock of Aluminum framework
browseruse/ – Local mock of Browser-use framework
utils/ – Logger, config loader, report tools
tests/ – Example tests using both frameworks
page_objects/ – Optional: implement Page Object Model
reports/ – Generated HTML/Allure reports
