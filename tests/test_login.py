# TC-001: Login con credenciales válidas
from utils.saucedemo_pages import LoginPage, InventoryPage
import os

def test_login_success(driver):
    login = LoginPage(driver)
    login.open()

    # screenshot antes de login (evidencia)
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-001_before_login.png"))

    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.wait_for_page()

    # screenshot luego de login (evidencia)
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-001_after_login.png"))

    assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"
    assert "Products" in inventory.get_title_text() or "Swag Labs" in driver.title
