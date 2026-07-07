import pytest
from pages.posts_api_page import PostsAPIPage
from pages.users_api_page import UsersAPIPage

class TestAPIIntegration:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.posts_api = PostsAPIPage()
        self.users_api = UsersAPIPage()
    
    def test_api_response_structure(self):
        """Prueba la estructura de las respuestas API"""
        # Test posts
        response = self.posts_api.get_posts(post_id=1)
        assert response.status_code == 200
        
        post_data = response.json()
        required_fields = ['id', 'title', 'body', 'userId']
        for field in required_fields:
            assert field in post_data, f"Falta el campo {field}"
        
        # Test users
        response = self.users_api.get_users(user_id=1)
        assert response.status_code == 200
        
        user_data = response.json()
        required_fields = ['id', 'name', 'email', 'phone']
        for field in required_fields:
            assert field in user_data, f"Falta el campo {field}"
    
    def test_api_status_codes(self):
        """Prueba que los códigos de estado sean correctos"""
        # Test POST
        new_post = {
            "title": "Test Post",
            "body": "Test content",
            "userId": 1
        }
        
        response = self.posts_api.create_post(new_post)
        assert response.status_code == 201
        
        # Test GET
        response = self.posts_api.get_posts(post_id=1)
        assert response.status_code == 200
        
        # Test PUT
        updated_post = {
            "id": 1,
            "title": "Updated",
            "body": "Updated content",
            "userId": 1
        }
        
        response = self.posts_api.update_post(1, updated_post)
        assert response.status_code == 200
        
        # Test DELETE
        delete_response = self.posts_api.delete_post(999)  # ID que no existe
        # JSONPlaceholder permite borrar IDs no existentes sin error (200)
        # Pero en APIs reales, esto podría dar error 404 o 405
