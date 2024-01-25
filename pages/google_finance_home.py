from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

SITE_URL = 'https://finance.google.com'


class GoogleFinanceHomePage:

    compare_markets_elm = (By.CSS_SELECTOR, ".PxxJne.lSOaoc")
    search_box_elm = (
        By.CSS_SELECTOR, "div[class='L6J0Pc ZB3Ebc nz7KN'] input[aria-label='Search for stocks, ETFs & more']")
    india_market_elm = (By.XPATH, "//div[@role='tab' and text()='India']")
    pnb_stock_heading_elm = (
        By.XPATH, "//div[@role='heading'][normalize-space()='Punjab National Bank']")
    market_tab_elm = (
        By.XPATH, "//div[@class='UJweIb']//div[@class='SJyhnc']/div/div")
    compare_markets_intraday_data_model_elm = (
        By.CSS_SELECTOR, "c-wiz[jsrenderer='FfFYBb']")
    main_menu_button_elm = (
        By.XPATH, "//*[name()='path' and contains(@d,'M3 18h18v-')]")
    main_menu_home_elm = (By.XPATH, "//div[normalize-space()='Home']")
    main_menu_market_trends_elm = (
        By.XPATH, "//div[@class='jjm4k'][normalize-space()='Market trends']")
    market_trends_elm = (By.CSS_SELECTOR, ".e1AOyf .TnyjJd")
    stock_list_elm = (
        By.CSS_SELECTOR, "#yDmH0d > c-wiz:nth-child(33) > div > div.e1AOyf > div.ZuWnOb.E1gI8e > div.hyO8N > div > div:nth-child(1) > ul")
    interactive_button_elm = (
        By.CSS_SELECTOR, "div.J3INNd.stxVfe[role='tablist'] a")
    most_active_button_elm = (
        By.CSS_SELECTOR, "a[href='./markets/most-active']")
    gainers_button_elm = (
        By.CSS_SELECTOR, "c-wiz[class='zQTmif SSPGKf rU0AKc'] div[class='ZuWnOb'] a:nth-child(3)")
    losers_button_elm = (
        By.CSS_SELECTOR, "c-wiz[class='zQTmif SSPGKf rU0AKc'] div[class='ZuWnOb'] a:nth-child(4)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def navigate_to_url(self):
        self.driver.get(SITE_URL)

    def get_page_title(self):
        return self.driver.title

    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False

    def select_market(self, locator):
        self.driver.find_element(*locator).click()

    def searchStock(self, stock):
        search_box = self.driver.find_element(*self.search_box_elm)
        search_box.send_keys(stock)
        search_box.send_keys(Keys.RETURN)

    def are_headings_present(self, headings_to_check):
        try:
            market_tabs = self.driver.find_elements(*self.market_tab_elm)
            tab_text = [tab.text for tab in market_tabs]
            return all(heading in tab_text for heading in headings_to_check)
        except NoSuchElementException:
            return False

    def click_on_element(self, locator):
        ActionChains(self.driver).click(
            self.driver.find_element(*locator)).perform()

    def select_option_from_main_menu(self, option_locator):
        try:
            option_button = self.wait.until(
                EC.element_to_be_clickable(option_locator))
            option_button.click()
            return self.driver.current_url
        except NoSuchElementException:
            return False

    def is_market_heading_selected(self, locator):
        market_heading = self.driver.find_element(*locator)
        return market_heading.get_attribute("aria-selected") == "true"

    def is_section_displayed(self, locator):
        return self.is_element_displayed(locator)

    def get_list_items_count(self, locator):
        try:
            list_element = self.driver.find_element(*locator)
            items = list_element.find_elements(By.TAG_NAME, "li")
            return len(items)
        except NoSuchElementException:
            return 0

    def is_element_enabled(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_enabled()
        except NoSuchElementException:
            return False
