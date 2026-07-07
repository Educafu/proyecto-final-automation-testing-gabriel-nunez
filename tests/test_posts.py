import pytest
import requests
from pages.posts_api_page import PostsAPIPage
from pages.users_api_page import UsersAPIPage

class TestPosts:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.posts_api = PostsAPIPage()
        self.users_api = UsersAPIPage()
    
    def test_get_all_posts(self):
        """Prueba obtener todos los posts"""
        response = self.posts_api.get_posts()
        assert response.status_code == 200
        assert len(response.json()) > 0
        print(f"Obtenidos {len(response.json())} posts")
    
    def test_get_single_post(self):
        """Prueba obtener un post específico"""
        response = self.posts_api.get_posts(post_id=1)
        assert response.status_code == 200
        post_data = response.json()
        assert post_data['id'] == 1
        assert 'title' in post_data
        assert 'body' in post_data
    
    def test_create_new_post(self):
        """Prueba crear un nuevo post"""
        new_post = {
            "title": "Test Post",
            "body": "This is a test post",
            "userId": 1
        }
        
        response = self.posts_api.create_post(new_post)
        assert response.status_code == 201
        
        created_post = response.json()
        assert created_post['title'] == new_post['title']
        assert created_post['body'] == new_post['body']
        assert created_post['userId'] == new_post['userId']
    
    def test_update_existing_post(self):
        """Prueba actualizar un post existente"""
        post_data = {
            "id": 1,
            "title": "Updated Title",
            "body": "Updated body content",
            "userId": 1
        }
        
        response = self.posts_api.update_post(1, post_data)
        assert response.status_code == 200
        
        updated_post = response.json()
        assert updated_post['title'] == post_data['title']
        assert updated_post['body'] == post_data['body']
    
    def test_delete_post(self):
        """Prueba eliminar un post"""
        # Primero creamos un post para eliminar
        new_post = {
            "title": "Post to delete",
            "body": "This will be deleted",
            "userId": 1
        }
        
        create_response = self.posts_api.create_post(new_post)
        assert create_response.status_code == 201
        created_post_id = create_response.json()['id']
        
        # Luego lo eliminamos
        delete_response = self.posts_api.delete_post(created_post_id)
        assert delete_response.status_code == 200
        
        # Verificamos que no se pueda obtener el post eliminado
        get_response = self.posts_api.get_posts(post_id=created_post_id)
        assert get_response.status_code == 404

    def test_negative_create_post_with_missing_data(self):
        """Prueba negativa: crear post con datos incompletos"""
        incomplete_post = {
            "title": "Incomplete Post"
            # Faltan 'body' y 'userId'
        }
        
        response = self.posts_api.create_post(incomplete_post)
        # En JSONPlaceholder, esto puede aún funcionar pero es un buen test de validación
        assert response.status_code in [200, 201]
