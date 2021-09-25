class Variables:
    # Splash variables
    skip_btn_id = "com.allandroidprojects.getirsample:id/btn_skip"
    next_btn_id = "com.allandroidprojects.getirsample:id/btn_next"
    dots_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                 "/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android" \
                 ".widget.LinearLayout/android.widget.TextView "
    # Main Page variables
    hamburger_btn_xpath = "//android.widget.ImageButton[@content-desc='Open navigation drawer']"
    toolbar_id = "com.allandroidprojects.getirsample:id/toolbar"
    hamburger_baby_care_xpath = "//android.widget.CheckedTextView[@text = 'Baby Care']"
    hamburger_all_categories_xpath = "//android.widget.CheckedTextView"
    hamburger_snacks_xpath = "//android.widget.CheckedTextView[@text = 'Snacks']"
    snacks_in_scroll_xpath = "//android.support.v7.app.ActionBar.Tab[@content-desc='Snacks']"
    products_detail_id = "com.allandroidprojects.getirsample:id/image1"
    cart_btn_id = "com.allandroidprojects.getirsample:id/action_cart"
    wishlist_in_hamburger_xpath = "//android.widget.CheckedTextView[@text='My Wishlist']"

    # Product Page variables
    add_cart_btn_id = "com.allandroidprojects.getirsample:id/text_action_bottom1"
    price_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                       "/android.view.ViewGroup/android.widget.FrameLayout[" \
                       "2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout/android" \
                       ".widget.LinearLayout[1]/android.widget.TextView[2] "
    product_text_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                         ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[" \
                         "2]/android.widget.LinearLayout/android.widget.ScrollView/android.widget.LinearLayout" \
                         "/android.widget.LinearLayout[1]/android.widget.TextView[1] "
    products_wishlist_icon_xpath = "//android.widget.ImageView[@resource-id='com.allandroidprojects.getirsample:id" \
                                   "/ic_wishlist'] "

    # Cart Page variables
    remove_btn_xpath = "//android.widget.TextView [@resource-id='com.allandroidprojects.getirsample:id/text_action1']"
    product_names_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                          ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[" \
                          "2]/android.widget.LinearLayout/android.widget.LinearLayout[" \
                          "1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[" \
                          "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[1] "
    product_prices_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget" \
                           ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[" \
                           "2]/android.widget.LinearLayout/android.widget.LinearLayout[" \
                           "1]/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[" \
                           "1]/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView[3] "
    # Wishlist Page
    wishlist_items_xpath = "//android.widget.LinearLayout[@resource-id='com.allandroidprojects.getirsample:id" \
                           "/layout_item_desc'] "
    wishlist_remove_icon_xpath = "//android.widget.ImageView[@resource-id='com.allandroidprojects.getirsample:id" \
                                 "/ic_wishlist'] "
