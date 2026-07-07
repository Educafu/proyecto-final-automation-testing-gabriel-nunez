import pytest
from pages.users_api_page import UsersAPIPage

class TestUsers:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.users_api = UsersAPIPage()
    
    def test_get_all_users(self):
        """Prueba obtener todos los usuarios"""
        response = self.users_api.get_users()
        assert response.status_code == 200
        assert len(response.json()) > 0
        print(f"Obtenidos {len(response.json())} usuarios")
    
    def test_get_single_user(self):
        """Prueba obtener un usuario específico"""
        response = self.users_api.get_users(user_id=1)
        assert response.status_code == 200
        user_data = response.json()
        assert user_data['id'] == 1
        assert 'name' in user_data
        assert 'email' in user_data
        assert 'phone' in user_data
    
    def test_create_new_user(self):
        """Prueba crear un nuevo usuario"""
        new_user = {
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com"
        }
        
        response = self.users_api.create_user(new_user)
        assert response.status_code == 201
        
        created_user = response.json()
        assert created_user['name'] == new_user['name']
        assert created_user['username'] == new_user['username']
        assert created_user['email'] == new_user['email']
    
    def test_update_existing_user(self):
        """Prueba actualizar un usuario existente"""
        user_data = {
            "id": 1,
            "name": "Updated User Name",
            "username": "updateduser",
            "email": "updated@example.com"
        }
        
        response = self.users_api.update_user(1, user_data)
        assert response.status_code == 200
        
        updated_user = response.json()
        assert updated_user['name'] == user_data['name']
        assert updated_user['username'] == user_data['username']
    
    def test_negative_get_nonexistent_user(self):
        """Prueba negativa: obtener usuario inexistente"""
        response = self.users_api.get_users(user_id=99999)
        assert response.status_code == 404
