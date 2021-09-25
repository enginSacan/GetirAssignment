from behave import given, when, then


@given("Open app and skip the splash")
def open_main_page(context):
    context.app.splash_page.skip_splash_page()


@when("Home page appears")
def open_hamburger_menu(context):
    context.app.main_page.open_hamburger_menu()


@when("Click Random Product Details")
def click_product_details(context):
    context.app.product_page.open_random_product_details()


@when("Add the product to basket")
def add_product_to_cart(context):
    context.app.product_page.add_product_to_cart()


@when("Return last page")
def back_last_page(context):
    context.app.product_page.back_last_page()


@when("Change category to {category}")
def go_to_baby_care_page(context, category):
    if category in "Baby Care":
        context.app.main_page.go_to_baby_products()
    if category in "Snacks":
        context.app.main_page.go_to_snack_products()


@when("Go to Basket")
def back_last_page(context):
    context.app.main_page.go_to_cart()


@when("Check products in the Basket")
def check_basket(context):
    check_result = context.app.cart_page.check_products_in_cart(context.app.product_page.added_products)
    print(str(check_result))
    assert check_result is True


@then("Delete all products from basket")
def delete_all_products(context):
    context.app.cart_page.remove_all_products()
