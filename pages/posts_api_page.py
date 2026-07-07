import requests
from config.config import Config
from utils.logger import logger

class PostsAPIPage:
    def __init__(self):
        self.base_url = Config.BASE_API_URL
        self.headers = {'Content-Type': 'application/json'}
        self.logger = logger
    
    def get_posts(self, post_id=None):
        """Obtiene todos los posts o un post específico"""
        if post_id:
            url = f"{self.base_url}/posts/{post_id}"
        else:
            url = f"{self.base_url}/posts"
        
        try:
            response = requests.get(url)
            self.logger.info(f"GET request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en GET request a {url}: {str(e)}")
            raise
    
    def create_post(self, post_data):
        """Crea un nuevo post"""
        url = f"{self.base_url}/posts"
        
        try:
            response = requests.post(url, json=post_data, headers=self.headers)
            self.logger.info(f"POST request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en POST request a {url}: {str(e)}")
            raise
    
    def update_post(self, post_id, post_data):
        """Actualiza un post existente"""
        url = f"{self.base_url}/posts/{post_id}"
        
        try:
            response = requests.put(url, json=post_data, headers=self.headers)
            self.logger.info(f"PUT request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en PUT request a {url}: {str(e)}")
            raise
    
    def delete_post(self, post_id):
        """Elimina un post"""
        url = f"{self.base_url}/posts/{post_id}"
        
        try:
            response = requests.delete(url)
            self.logger.info(f"DELETE request completed to {url}")
            return response
        except Exception as e:
            self.logger.error(f"Error en DELETE request a {url}: {str(e)}")
            raise
    
    def validate_post_response(self, response, expected_status_code=200):
        """Valida la respuesta de un post"""
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code}, but got {response.status_code}"
        
        if response.status_code == 200:
            assert 'title' in response.json(), "Missing title in response"
            assert 'body' in response.json(), "Missing body in response"
            assert 'userId' in response.json(), "Missing userId in response"
        
        self.logger.info(f"Response validation passed for status code {response.status_code}")
