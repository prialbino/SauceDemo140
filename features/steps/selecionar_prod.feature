Feature: Select product

    Scenario: Select product "Sauce Labs Backpack"
        Given I access the site Sauce Demo
        When I complete the login fields with user standard_user and password secret_sauce 
        Then I will be directed to a Home page

    Scenario: Login with the wrong password
        Given I access the site Sauce Demo
        When I complete the login fields with user standard_user and password laranja
        Then shows the login message error 

   Scenario Outline: Login invalid
        Given I access the site Sauce Demo
        When I complete the login fields with user <user> and password <password>
        Then shows the login <message> error 

        Examples:   
        | id | user          | password     | message  |
        | 01 | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user |              | Epic sadface: Password is required                                        |
        | 03 |               | secret_sauce | Epic sadface: Username is required                                        |  
        | 04 | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service |  
        | 05 | juca          | laranja      | Epic sadface: Username and password do not match any user in this service |  
        | 06 | juca          |              | Epic sadface: Password is required                                        |  
        | 07 |               |              | Epic sadface: Username is required                                        | 
        | 08 |               | laranja      | Epic sadface: Username is required                                        | 

    Scenario Outline: Login invalid adding IF
        Given I access the site Sauce Demo
        When I fill the login fields with user <user> and password <password> adding IF
        Then shows the login <message> error 

        Examples:   
        | id | user          | password     | message  |
        | 01 | standard_user | laranja      | Epic sadface: Username and password do not match any user in this service |
        | 02 | standard_user | <branco>     | Epic sadface: Password is required                                        |
        | 03 | <branco>      | secret_sauce | Epic sadface: Username is required                                        |  
        | 04 | juca          | secret_sauce | Epic sadface: Username and password do not match any user in this service |  
        | 05 | juca          | laranja      | Epic sadface: Username and password do not match any user in this service |  
        | 06 | juca          | <branco>     | Epic sadface: Password is required                                        |  
        | 07 | <branco>      | <branco>     | Epic sadface: Username is required                                        | 
        | 08 | <branco>      | laranja      | Epic sadface: Username is required                                        |     