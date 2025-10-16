from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login():
    options = Options()
    options.add_experimental_option("detach", True)  # mantiene Chrome abierto
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    usuario = wait.until(EC.visibility_of_element_located((By.ID, "user-name")))
    usuario.send_keys("standard_user")

    password = driver.find_element(By.ID, "password")
    password.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    #No se cierra automáticamente
    print("✅ Navegador abierto. Cerralo manualmente cuando termines.")

#if __name__ == "__main__":
    test_login()

