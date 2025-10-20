# git-AutomationQA-Python

## Pre-Entrega de proyecto final QA-Automation en Python.

## Objetivo: 
Automatizar flujos de navegación web utilizando Selenium WebDriver y Python.

## Sitio Web a utilizar:
www.saucedemo.com

## -Tecnologías Requeridas:
Python como lenguaje principal.
Pytest para estructura de testing.
Selenium WebDriver para automatización.
Pytest-HTML para generación de reportes HTML.
WebDriver Manager para manejo automático de drivers de navegador.
Google Chrome como navegador utilizado para la ejecución de pruebas.
Git y GitHub para control de versiones y repositorio de entrega.

## Dependencias e instalación:
Dependencias:
selenium>=4.10.0
pytest>=7.0.0
pytest-html>=3.0.0
webdriver-manager>=4.0.0

## Instalación de dependencias: 
Para ejecutar las pruebas de automatización, instalar las siguientes dependencias:
Crear venv en carpeta raiz: 
python -m venv venv
Activar el venv:
.\venv\Scripts\Activate.ps1
Instalar dependencias usando el venv:
pip install selenium pytest pytest-html webdriver-manager

## Ejecutar tests y generar HTML:
pytest -v --html=reports/reporte.html --self-contained-html

## Estructura
pre-Entrega-Automation-Testing--FedericoPeche/
├─ tests/
│  ├─ test_login.py          # Test de login automatizado (TC-001)
│  ├─ test_inventory.py      # Validación de catálogo y elementos (TC-002)
│  └─ test_cart.py           # Interacción con productos y carrito (TC-003)
├─ utils/
│  ├─ browser.py             # Configuración del WebDriver
│  └─ saucedemo_pages.py     # Clases y métodos reutilizables (Page Objects)
├─ reports/
│  └─ screenshots/           # Capturas automáticas en caso de fallos
├─ conftest.py               # Fixtures y configuración de Pytest
└─ README.md                 # Documentación del proyecto

## Enlace y avance del armado de los diferentes Test Cases:
https://drive.google.com/drive/folders/1ukOp_9HD0p2HdavNIu8mbCe2951tsFGd?usp=sharing


