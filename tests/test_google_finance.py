import pytest
from pages.google_finance_home import GoogleFinanceHomePage


@pytest.fixture(scope="function")
def home_page(driver):
    home_page = GoogleFinanceHomePage(driver)
    home_page.navigate_to_url()
    yield home_page


@pytest.mark.smoke
def test_home_page_load(home_page):
    PAGE_TITLE = 'Google Finance - Stock Market Prices, Real-time Quotes & Business News'
    assert PAGE_TITLE == home_page.get_page_title()


@pytest.mark.smoke
def test_compare_markets_load(home_page):
    home_page.click_on_element(home_page.compare_markets_elm)
    assert home_page.is_element_displayed(
        home_page.compare_markets_intraday_data_model_elm)


def test_headings_presence(home_page):
    headings_to_check = ["US", "Europe", "India",
                         "Currencies", "Crypto", "Futures"]
    assert home_page.are_headings_present(headings_to_check)


@pytest.mark.smoke
def test_main_menu_home_navigation(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    HOME_PAGE_URL = "https://www.google.com/finance/"
    assert HOME_PAGE_URL == home_page.select_option_from_main_menu(
        home_page.main_menu_home_elm)


@pytest.mark.smoke
def test_main_menu_market_trends_navigation(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    MARKET_TRENDS_URL = "https://www.google.com/finance/markets/indexes"
    assert MARKET_TRENDS_URL == home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)


def test_search_stock_functionality(home_page):
    if not home_page.is_market_heading_selected(home_page.india_market_elm):
        home_page.select_market(home_page.india_market_elm)
    home_page.searchStock("PNB")
    assert "Punjab National Bank" in home_page.driver.page_source


def test_market_trends_displayed(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    assert home_page.is_section_displayed(home_page.market_trends_elm)


def test_stock_list_in_market_trends(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    count = home_page.get_list_items_count(home_page.stock_list_elm)
    assert count > 0


def test_interactive_elements_in_market_trends(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    assert home_page.is_element_enabled(home_page.interactive_button_elm)


def test_most_active_section(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    home_page.click_on_element(home_page.most_active_button_elm)
    count = home_page.get_list_items_count(
        home_page.stock_list_elm)
    assert count > 0, "Most Active section should have items"


def test_gainers_section(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    home_page.click_on_element(home_page.gainers_button_elm)
    count = home_page.get_list_items_count(
        home_page.stock_list_elm)
    assert count > 0, "Gainers section should have items"


def test_losers_section(home_page):
    home_page.click_on_element(home_page.main_menu_button_elm)
    home_page.select_option_from_main_menu(
        home_page.main_menu_market_trends_elm)
    home_page.click_on_element(home_page.losers_button_elm)
    count = home_page.get_list_items_count(home_page.stock_list_elm)
    assert count > 0, "Losers section should have items"
