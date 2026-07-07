import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config.config import Config

@pytest.fixture(scope="session")
def driver():
    """Fixture para el WebDriver"""
    # Configuración del driver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Para ejecución sin navegador visible
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # Inicializar el driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Configurar timeouts
    driver.implicitly_wait(Config.SELENIUM_IMPLICIT_WAIT)
    driver.set_page_load_timeout(Config.SELENIUM_TIMEOUT)
    
    yield driver
    
    # Cerrar el driver al finalizar
    driver.quit()

@pytest.fixture(scope="function")
def base_url():
    """URL base para las pruebas"""
    return Config.BASE_API_URL

@pytest.fixture(scope="function")
def api_endpoints():
    """Endpoints de la API"""
    return {
        'posts': f"{Config.BASE_API_URL}/posts",
        'users': f"{Config.BASE_API_URL}/users"
    }

# Fixture para captura de pantalla en caso de fallo
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para capturar screenshots en caso de fallo"""
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        # Aquí podrías implementar la captura de pantalla
        pass
