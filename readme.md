# Framework de Automatización de Pruebas

Framework completo para automatización de pruebas que combina UI y API testing.

## Características

- Automatización de pruebas UI con Selenium WebDriver
- Pruebas de API con Requests
- Patrón Page Object Model (POM)
- Generación de reportes visuales
- Logging detallado

## Tecnologías Utilizadas

- Python 3.8+
- Selenium WebDriver
- Requests
- Pytest
- Git/GitHub

## Estructura del Proyecto

proyecto-final/
├── pages/          # Páginas y elementos UI
├── tests/          # Casos de prueba
├── utils/          # Funciones auxiliares
├── config/         # Configuración
├── reports/        # Reportes generados
└── screenshots/    # Capturas de pantalla

## Requisitos

- Python 3.8+
- Git instalado

## Instalación

* en bash

pip install -r requirements.txt

## Ejecución de Pruebas

- Ejecutar todas las pruebas

pytest

- Ejecutar pruebas con reporte HTML

pytest --html=reports/report.html --self-contained-html
