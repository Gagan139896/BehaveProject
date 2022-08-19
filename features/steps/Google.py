import time
from behave import *
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


@given(u'I launched chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(
    executable_path="C:/Users/crochet-08/PycharmProjects/BehaveProject/Chrome/chromedriver.exe")
    context.driver.implicitly_wait(3)
    context.driver.maximize_window()
    print("Chrome Browser Opened Successfully")
    time.sleep(10)

@when(u'I opened google URL')
def step_impl(context):
    context.driver.implicitly_wait(3)
    context.driver.get("https://www.google.com/")
    print("URL opened Successfully")
    time.sleep(10)

@when(u'I searched python')
def step_impl(context):
    context.driver.implicitly_wait(3)
    context.driver.find_element_by_xpath("//input[@title='Search']").send_keys("Python")
    action = ActionChains(context.driver)
    action.send_keys(Keys.ENTER).perform()

@then(u'Title is verified after performing search action')
def step_impl(context):
    ExpectedText = "Welcome to Python.org"
    try:
        context.driver.implicitly_wait(3)
        ActualText = context.driver.find_element_by_xpath("//h3[text()='Welcome to Python.org']").text
        assert ActualText in ExpectedText, "Page is not verified"
    except Exception as e:
        print(e)

@then(u'Title is not verified after performing search action')
def step_impl(context):
    ExpectedText1 = "Welcome to Python.org"
    context.driver.implicitly_wait(3)
    ActualText1 = context.driver.find_element_by_xpath("//h3[text()='Welcome to Python.org1111']").text
    print(ActualText1)
    assert ActualText1 in ExpectedText1, "Page is not verified"