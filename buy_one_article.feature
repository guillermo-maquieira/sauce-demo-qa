Feature: Buy One Article

Scenario: User can add one article to cart
    Given I open "https://www.saucedemo.com/"
    And I login as "standard_user" with "secret_sauce"
    When I click the "ADD TO CART" button
    Then I should see the one article icon in my cart
