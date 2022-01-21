from BDDTest.Utilities.customLogger import LogGen
from BDDTest.Utilities.readproperty import ReadConfig
from behave import *
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

baseURL = ReadConfig.getURL()
mylogger = LogGen.loggen()

@given('Launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install)
    mylogger.info("****Driver Installed*******")
    context.driver.get(baseURL)
    mylogger.info("Browser launched")

@then('verify the page title')
def step_imp(context):
    actual_title = context.driver.title
    excepted_title = "Happypaws"

    if actual_title == excepted_title:
        assert True
        mylogger.info("****Title matched****")

    else:
        mylogger.info("****Title not matched****")
        assert False

@then('close the browser')
def step_impl(context):
    context.driver.close()
    mylogger.info('Browser closed')