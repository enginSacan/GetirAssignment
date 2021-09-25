Feature: Tests for adding and removing Baby Care Basket

  Scenario: Baby Care Products tests
    Given Open app and skip the splash
    When  Home page appears
    And   Change category to Baby Care
    And   Click Random Product Details
    And   Add the product to basket
    And   Return last page
    And   Change category to Snacks
    And   Click Random Product Details
    And   Add the product to basket
    And   Return last page
    And   Go to Basket
    And   Check products in the Basket
    Then  Delete all products from basket