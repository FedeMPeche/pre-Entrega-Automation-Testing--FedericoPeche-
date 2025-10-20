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
Dependencias: selenium>=4.10.0 | pytest>=7.0.0 | pytest-html>=3.0.0 | webdriver-manager>=4.0.0

## Instalación de dependencias: 
Para ejecutar las pruebas de automatización, instalar las siguientes dependencias:
Crear venv en carpeta raiz: python -m venv venv | Activar el venv: .\venv\Scripts\Activate.ps1 | Instalar dependencias usando el venv: pip install selenium pytest pytest-html webdriver-manager

## Ejecutar tests y generar HTML:
pytest -v --html=reports/reporte.html --self-contained-html

## Estructura
pre-Entrega-Automation-Testing--FedericoPeche/
## Test de login automatizado (TC-001)
├─ tests/ test_login.py
## Validación de catálogo y elementos (TC-002)
│  ├─ test_inventory.py
## Interacción con productos y carrito (TC-003)
│  └─ test_cart.py
## pre-Entrega-Automation-Testing--FedericoPeche/
├─ utils/
## Configuración del WebDriver
│  ├─ browser.py
## Clases y métodos reutilizables (Page Objects)
│  └─ saucedemo_pages.py
## Capturas automáticas en caso de fallos
├─ pre-Entrega-Automation-Testing--FedericoPeche/reports/
│  └─ screenshots/
## Fixtures y configuración de Pytest
├─ conftest.py
## Documentación del proyecto
└─ README.md                

## Enlace y avance del armado de los diferentes Test Cases:
https://drive.google.com/drive/folders/1ukOp_9HD0p2HdavNIu8mbCe2951tsFGd?usp=sharing


