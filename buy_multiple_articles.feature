Feature: Buy Multiple Articles

Scenario: User can add multiple articles to cart
    Given I open "https://www.saucedemo.com/"
    And I login as "standard_user" with "secret_sauce"
    When I click the "ADD TO CART" button
    And I click click "ADD TO CART" button
    Then I should see the two articles icon in my cart
