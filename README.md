# Getir Assignment

This repo is created to show subjects below:

* **Appium** library usage with Python Behave.
* Getting arguments in terminal before executing python file or you can use PyCharm
* You should add site packages to your python environment.
* You have to load apk file to your android device or emulator to run the test.

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
## Test Cases

### Case 1:
* User should pass onboarding screens
* User checks if home page exists or not
* User changes category to ‘Baby Care’
* User open a random product detail
* User adds this product to basket and return last page
* User changes category to ‘Snacks’
* User open a random product detail
* User adds this product to basket and return last page
* User goes to basket and control added products and prices
* User should deletes all products from basket and makes
controls
### Case 2:
* User should pass onboarding screens
* User checks if home page exists or not
* User gets the number of categories and write this number to
console
* User open a random category
* User adds 3 random products to wishlist via mini heart icon
* User opens the menu in the left
* User go to ‘My Wishlist’
* User controls the page and products
* User deletes all of them from Wishlist
### Case 3:
* Please find 2 functional bugs in app and report them in
reporting standards
* Write two automation cases for handle this bugs.
