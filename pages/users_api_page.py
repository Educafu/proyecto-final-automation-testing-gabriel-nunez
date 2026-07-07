import requests
from config.config import Config
from utils.logger import logger

class UsersAPIPage:
    def __init__(self):
        self.base_url = Config.BASE_API_URL
        self.headers = {'Content-Type': 'application/json'}
        self.logger = logger
    
    def get_users(self, user_id=None):
        """Obtiene todos los usuarios o un usuario específico"""
        if user_id:
            url = f"{self.base_url}/users/{user_id}"
        else:
            url = f"{self.base_url}/users"
        
        try:
            response = requests.get(url)
            self.logger.info(f"GET request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en GET request a {url}: {str(e)}")
            raise
    
    def create_user(self, user_data):
        """Crea un nuevo usuario"""
        url = f"{self.base_url}/users"
        
        try:
            response = requests.post(url, json=user_data, headers=self.headers)
            self.logger.info(f"POST request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en POST request a {url}: {str(e)}")
            raise
    
    def update_user(self, user_id, user_data):
        """Actualiza un usuario existente"""
        url = f"{self.base_url}/users/{user_id}"
        
        try:
            response = requests.put(url, json=user_data, headers=self.headers)
            self.logger.info(f"PUT request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en PUT request a {url}: {str(e)}")
            raise
    
    def delete_user(self, user_id):
        """Elimina un usuario"""
        url = f"{self.base_url}/users/{user_id}"
        
        try:
            response = requests.delete(url)
            self.logger.info(f"DELETE request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en DELETE request a {url}: {str(e)}")
            raise
    
    def validate_user_response(self, response, expected_status_code=200):
        """Valida la respuesta de un usuario"""
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status_code}"
        
        if response.status_code == 200:
            assert 'name' in response.json(), "Missing name in response"
            assert 'email' in response.json(), "Missing email in response"
            assert 'phone' in response.json(), "Missing phone in response"
        
        self.logger.info(f"Response validation passed for status code {response.status_code}")
