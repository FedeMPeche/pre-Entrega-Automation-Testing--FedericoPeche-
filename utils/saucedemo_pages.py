#Page Object (locators + acciones)#
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.saucedemo.com/"

class LoginPage:
    URL = BASE_URL
    USER = (By.ID, "user-name")
    PASS = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.USER)).clear()
        self.driver.find_element(*self.USER).send_keys(username)
        self.driver.find_element(*self.PASS).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

class InventoryPage:
    HEADER = (By.CLASS_NAME, "title")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    FIRST_ITEM_NAME = (By.CSS_SELECTOR, ".inventory_item .inventory_item_name")
    FIRST_ITEM_PRICE = (By.CSS_SELECTOR, ".inventory_item .inventory_item_price")
    FILTER = (By.CLASS_NAME, "product_sort_container")
    MENU_BTN = (By.ID, "react-burger-menu-btn")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_BTN = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_for_page(self):
        self.wait.until(EC.url_contains("/inventory.html"))
        self.wait.until(EC.visibility_of_element_located(self.HEADER))

    def get_title_text(self):
        return self.driver.find_element(*self.HEADER).text

    def count_items(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def first_item_name(self):
        return self.driver.find_element(*self.FIRST_ITEM_NAME).text

    def first_item_price(self):
        return self.driver.find_element(*self.FIRST_ITEM_PRICE).text

    def add_first_item_to_cart(self):
        btn = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item .btn_inventory")
        btn.click()

    def get_cart_count(self):
        el = self.driver.find_elements(*self.CART_BADGE)
        return el[0].text if el else "0"

    def go_to_cart(self):
        self.driver.find_element(*self.CART_BTN).click()

class CartPage:
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def count_items(self):
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_list")))
        return len(self.driver.find_elements(*self.CART_ITEMS))
