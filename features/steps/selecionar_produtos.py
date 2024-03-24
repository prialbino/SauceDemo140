# 1 - Bibliotecas / Imports
import time
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

@when(u'I complete the login fields with user {user}')
def step_impl(context, user):
    context.driver.find_element(By.ID, "user-name").send_keys(user)

@when(u'I enter the password {password}')
def step_impl(context, password):  
    context.driver.find_element(By.ID, "password").send_keys(password)
    context.driver.find_element(By.ID, "login-button").click()

@then(u'I will be directed to a Home page')
def step_impl(context): 
    assert context.driver.find_element(By.CSS_SELECTOR, ".title").text == "Products"

    #teardown / encerramento
    context.driver.quit()