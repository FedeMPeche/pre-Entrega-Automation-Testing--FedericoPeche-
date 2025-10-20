#Con este contenido usamos el driver y dirigimos los reportes a las carpetas correspondientes#
import os
import pytest
from utils.browser import create_driver

REPORT_DIR = os.path.join(os.getcwd(), "reports")
SCREEN_DIR = os.path.join(REPORT_DIR, "screenshots")
os.makedirs(SCREEN_DIR, exist_ok=True)

@pytest.fixture(scope="function")
def driver():
    d = create_driver(headless=False)  # headless=True si querés CI
    yield d
    d.quit()
