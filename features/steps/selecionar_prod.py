# 1 - Bibliotecas / Imports
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I access the site Sauce Demo')
def step_impl(context):
    # setup / inicializacao
    context.driver = webdriver.Chrome()  
    context.driver.maximize_window()
    context.driver.implicitly_wait(2)

    # step 
    context.driver.get("https://www.saucedemo.com")

# fill the user and password
@when(u'I complete the login fields with user {user} and password {password}')
def step_impl(context, user, password):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

# fill the password with no user 
@when(u'I complete the login fields with user  and password {password}')
def step_impl(context, password):  
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

# fill the user with no password
@when(u'I complete the login fields with user {user} and password ')
def step_impl(context, user):
    context.driver.find_element(By.ID, "user-name").send_keys(user)
    # password will not informed
    context.driver.find_element(By.ID, "login-button").click()

# Click in the login button without filling user and password fields
@when(u'I complete the login fields with user  and password ')
def step_impl(context):
    # user and password will not informed
    context.driver.find_element(By.ID, "login-button").click()        

# fill the user and password through IF
@when(u'I fill the login fields with user {user} and password {password} adding IF')
def step_impl(context, user, password):
    if user != '<branco>':
        context.driver.find_element(By.ID, "user-name").send_keys(user)
        #if user <branco> there is no action for filling

    if password != '<branco>': 
        context.driver.find_element(By.ID, "password").send_keys(password)
        # if password <branco> there is no action for filling

    context.driver.find_element(By.ID, "login-button").click()

@then(u'I will be directed to a Home page')
def step_impl(context): 
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

    #teardown / encerramento
    context.driver.quit()

@then(u'shows the login message error')
def step_impl(context):
    #check the message error
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == "Epic sadface: Username and password do not match any user in this service"

    #teardown / encerramento
    context.driver.quit()

# check the message for the Scenario Oultine
@then(u'shows the login {message} error')
def step_impl(context, message):
    #check the message error
    assert context.driver.find_element(By.CSS_SELECTOR, "h3").text == message

    #teardown / encerramento
    context.driver.quit()    