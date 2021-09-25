from behave import given, when, then


@when("Get category number and choose random one")
def get_category_number(context):
    context.app.main_page.get_category_number_and_choose_random()


@when("Add Three random products to wishlist")
def add_product_to_wishlist(context):
    context.app.product_page.add_three_product_to_wishlist()


@when("Check the wishlist page")
def check_the_wishlist(context):
    context.app.main_page.open_wishlist()
    count = context.app.wishlist_page.count_wishlist()
    assert count == 3


@then("Delete all products in Wishlist")
def delete_all_products_in_wishlist(context):
    context.app.wishlist_page.remove_items_in_wishlist()
