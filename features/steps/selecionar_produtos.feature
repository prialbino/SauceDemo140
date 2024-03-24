Feature: Select product

    Scenario: Select product "Sauce Labs Backpack"
        Given I access the site Sauce Demo
        When I complete the login fields with user standard_user
        And I enter the password secret_sauce 
        Then I will be directed to a Home page