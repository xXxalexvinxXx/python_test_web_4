import logging

from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    # login
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]//div[1]/label/input""")
    # passwd
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    # login button
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    # error 401 place
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    # hello,user string
    LOCATOR_HELLO = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    # create new post button
    LOCATOR_NEW_POST_BTN = (By.CSS_SELECTOR, """button#create-btn""")
    # post title field
    LOCATOR_TITLE = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[1]/div/label/input""",
    )
    # post description field
    LOCATOR_DESCRIPTION = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""",
    )
    # post content field
    LOCATOR_CONTENT = (
        By.XPATH,
        """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""",
    )
    # save post button
    LOCATOR_SAVE_POST_BTN = (By.CSS_SELECTOR, """.mdc-button""")
    # new post title
    LOCATOR_NEW_POST_TITLE = (By.XPATH, """/html/body/div[1]/main/div/div[1]/h1""")
    # contact us
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    # name field
    LOCATOR_NAME = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    # e-mail field
    LOCATOR_EMAIL_FIELD = (
        By.XPATH,
        """//*[@id="contact"]/div[2]/label/input""",
    )
    # message field
    LOCATOR_MESSAGE_FIELD = (
        By.XPATH,
        """//*[@id="contact"]/div[3]/label/span/textarea""",
    )
    # send button field
    LOCATOR_SUBMIT_BTN = (By.CSS_SELECTOR, """.mdc-button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(
            f"Send '{word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}"
        )
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(
            f"Send '{word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}"
        )
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info(f"Send click to element {TestSearchLocators.LOCATOR_LOGIN_BTN[1]}")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        logging.info(
            f"Read text of element {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}"
        )
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        return text

    def get_user_text(self):
        logging.info(f"Read text of element {TestSearchLocators.LOCATOR_HELLO[1]}")
        user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO, time=2)
        text = user_field.text
        return text

    def click_new_post_btn(self):
        logging.info(
            f"Send click to element {TestSearchLocators.LOCATOR_NEW_POST_BTN[1]}"
        )
        self.find_element(TestSearchLocators.LOCATOR_NEW_POST_BTN).click()

    def enter_title(self, word):
        logging.info(f"Send '{word} to element {TestSearchLocators.LOCATOR_TITLE[1]}")
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE)
        title_field.clear()
        title_field.send_keys(word)

    def enter_description(self, word):
        logging.info(
            f"Send '{word} to element {TestSearchLocators.LOCATOR_DESCRIPTION[1]}"
        )
        descript_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION)
        descript_field.clear()
        descript_field.send_keys(word)

    def enter_content(self, word):
        logging.info(f"Send '{word} to element {TestSearchLocators.LOCATOR_CONTENT[1]}")
        cont_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        cont_field.clear()
        cont_field.send_keys(word)

    def click_save_post_btn(self):
        logging.info(
            f"Send click to element {TestSearchLocators.LOCATOR_SAVE_POST_BTN[1]}"
        )
        self.find_element(TestSearchLocators.LOCATOR_SAVE_POST_BTN).click()

    def get_res_text(self):
        logging.info(
            f"Read text of element {TestSearchLocators.LOCATOR_NEW_POST_TITLE[1]}"
        )
        user_field = self.find_element(
            TestSearchLocators.LOCATOR_NEW_POST_TITLE, time=2
        )
        text = user_field.text
        return text

    def open_contact_us(self):
        logging.info(f'Open "Contact Us" {TestSearchLocators.LOCATOR_CONTACT_US_BTN} ')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def enter_name(self, word):
        logging.info(f"Send '{word} to element {TestSearchLocators.LOCATOR_NAME[1]}")
        name_field = self.find_element(TestSearchLocators.LOCATOR_NAME)
        name_field.clear()
        name_field.send_keys(word)

    def enter_email(self, word):
        logging.info(
            f"Send '{word} to element {TestSearchLocators.LOCATOR_EMAIL_FIELD[1]}"
        )
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(word)

    def enter_message(self, word):
        logging.info(
            f"Send '{word} to element {TestSearchLocators.LOCATOR_MESSAGE_FIELD[1]}"
        )
        message_field = self.find_element(TestSearchLocators.LOCATOR_MESSAGE_FIELD)
        message_field.clear()
        message_field.send_keys(word)

    def contact_btn(self):
        logging.info(f"Send form {TestSearchLocators.LOCATOR_SUBMIT_BTN[1]}")
        self.find_element(TestSearchLocators.LOCATOR_SUBMIT_BTN).click()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        alert.accept()
        return text
