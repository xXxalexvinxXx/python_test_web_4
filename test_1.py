import logging

from testpage import OperationsHelper
import yaml
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info("Test 1 Start")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser):
    logging.info("Test 2 Start")
    testpage = OperationsHelper(browser)
    testpage.enter_login(testdata["user"])
    testpage.enter_pass(testdata["pass"])
    testpage.click_login_button()
    assert testpage.get_user_text() == f"Hello, {testdata['user']}"


def test_step3(browser):
    logging.info("Test 3 Start")
    testpage = OperationsHelper(browser)
    testpage.click_new_post_btn()
    testpage.enter_title(testdata["title"])
    testpage.enter_description(testdata["descript"])
    testpage.enter_content(testdata["cont"])
    testpage.click_save_post_btn()
    time.sleep(2)
    assert testpage.get_res_text() == testdata["title"]


def test_step4(browser):
    logging.info("Test 4 Start")
    testpage = OperationsHelper(browser)
    testpage.open_contact_us()
    testpage.enter_name(testdata["user"])
    testpage.enter_email(testdata["email"])
    testpage.enter_message(testdata["message"])
    testpage.contact_btn()
    time.sleep(2)
    assert testpage.get_alert_text() == testdata["answer"]
