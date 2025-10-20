# TC-002: Navegación y verificación del catálogo
from utils.saucedemo_pages import LoginPage, InventoryPage
import os

def test_inventory_page_contents(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)
    inv.wait_for_page()

    # evidencia
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-002_inventory_loaded.png"))

    # Validaciones
    assert inv.get_title_text().strip() == "Products"
    assert inv.count_items() >= 1

    # verificar elementos UI
    assert inv.driver.find_element(*inv.MENU_BTN).is_displayed()
    assert inv.driver.find_element(*inv.FILTER).is_displayed()
    assert inv.driver.find_element(*inv.CART_BTN).is_displayed()

    nombre = inv.first_item_name()
    precio = inv.first_item_price()
    print(f"Primer producto: {nombre} - {precio}")

    # captura del primer producto visible
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-002_first_item.png"))
