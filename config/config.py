import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # URLs de la API
    BASE_API_URL = "https://jsonplaceholder.typicode.com"
    
    # URLs de la aplicación web (puedes usar una demo)
    BASE_WEB_URL = "https://jsonplaceholder.typicode.com"
    
    # Configuración de Selenium
    SELENIUM_TIMEOUT = 10
    SELENIUM_IMPLICIT_WAIT = 10
    
    # Configuración de logging
    LOG_LEVEL = "INFO"
    LOG_FILE = "logs/test.log"
    
    # Configuración de reportes
    REPORTS_DIR = "reports"
    SCREENSHOTS_DIR = "screenshots"
