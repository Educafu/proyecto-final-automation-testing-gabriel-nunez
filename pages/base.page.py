from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from utils.logger import logger
import time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = logger
    
    def find_element(self, locator, timeout=10):
        """Encuentra un elemento con espera explícita"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            self.logger.error(f"Elemento no encontrado: {locator}")
            raise
    
    def click_element(self, locator):
        """Hace clic en un elemento"""
        try:
            element = self.find_element(locator)
            element.click()
            self.logger.info(f"Clic realizado en: {locator}")
        except Exception as e:
            self.logger.error(f"Error al hacer clic en {locator}: {str(e)}")
            raise
    
    def input_text(self, locator, text):
        """Ingresa texto en un campo"""
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Texto ingresado en {locator}: {text}")
        except Exception as e:
            self.logger.error(f"Error al ingresar texto en {locator}: {str(e)}")
            raise
    
    def get_text(self, locator):
        """Obtiene el texto de un elemento"""
        try:
            element = self.find_element(locator)
            return element.text
        except Exception as e:
            self.logger.error(f"Error al obtener texto de {locator}: {str(e)}")
            raise
    
    def is_element_present(self, locator):
        """Verifica si un elemento está presente"""
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False
    
    def wait_for_element(self, locator, timeout=10):
        """Espera a que un elemento esté presente"""
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            return None
    
    def take_screenshot(self, name):
        """Toma una captura de pantalla"""
        screenshot_dir = "screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        
        screenshot_path = f"{screenshot_dir}/{name}.png"
        self.driver.save_screenshot(screenshot_path)
        self.logger.info(f"Captura de pantalla guardada: {screenshot_path}")
