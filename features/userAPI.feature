# Creater by Owner 03/30/2021


Feature: Verify if user able to register and login

  @register
  Scenario Outline: Verify user register API functionality
    Given the user detail which <username> and <password> need to be added to db
    When we executed the user_register API Method
    Then User should successfully registered

     Examples:
      |username|password|
      |user1|Bazinga_1|
#      |user2    |Bazinga_2  |
#      |user3    |Bazinga_3  |

  @login
  Scenario: Verify User Login API Functionality
    Given the user details <username> and <password> are provided for login
    When we executed the login API Method
    Then user should able to login successfully
#
#     Examples:ta
#      |username |password   |
#      |user1    |Bazinga_1  |