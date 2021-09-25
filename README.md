# Getir Assignment

This repo is created to show subjects below:

* **Appium** library usage with Python Behave.
* Getting arguments in terminal before executing python file or you can use PyCharm
* You should add site packages to your python environment.

[Pyhton]: https://www.python.org/
[Python Behave]: https://behave.readthedocs.io/en/stable/
[Allure Behave]: https://pypi.org/project/allure-behave/
## How It Works

1. Install **[Pyhton]** to your pc.(Python 3.9.0)
2. Install **[Python Behave]** to your pc via pip.
3. Install **[Allure Behave]** to your pc.

## Usage
When every instalation is done you use command below for execution the test in the terminal or Run in the Pycharm.

 ```sh
    $ behave -f allure_behave.formatter:AllureFormatter -o reports/ features
 ```
To create allure test report you should execute command below:

 ```sh
    $ allure serve <path of the allure results folder>  
 ```
