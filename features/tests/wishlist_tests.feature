Feature: Wishlist behavior Tests
  Scenario: Add and Remove products in Wishlist
    Given Open app and skip the splash
    When  Get category number and choose random one
    And   Add Three random products to wishlist
    And   Check the wishlist page
    Then  Delete all products in Wishlist