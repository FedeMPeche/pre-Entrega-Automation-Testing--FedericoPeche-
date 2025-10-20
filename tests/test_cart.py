# TC-003: Interacción con productos - Carrito
from utils.saucedemo_pages import LoginPage, InventoryPage, CartPage
import os

def test_add_to_cart_and_verify(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")

    inv = InventoryPage(driver)
    inv.wait_for_page()

    # screenshot antes de agregar
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-003_before_add.png"))

    # agregar primer producto
    inv.add_first_item_to_cart()

    # pequeña espera implícita via find/read; captura del contador
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-003_after_add.png"))

    cart_count = inv.get_cart_count()
    assert cart_count == "1", f"Contador del carrito incorrecto: {cart_count}"

    inv.go_to_cart()
    cart = CartPage(driver)
    assert cart.count_items() == 1, "El carrito no contiene el producto agregado"

    # captura del carrito
    driver.save_screenshot(os.path.join("reports", "screenshots", "TC-003_cart.png"))
