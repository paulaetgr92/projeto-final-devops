import unittest
from app import app
import werkzeug
from flask_jwt_extended import create_access_token

if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCaseAdditional(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_protected_with_valid_token(self):
        with app.app_context():
            token = create_access_token(identity="usuario_exemplo")
        headers = {"Authorization": f"Bearer {token}"}
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Você acessou um recurso protegido"})

    def test_login_method_not_allowed(self):
        response = self.client.get('/login')  # GET ao invés de POST
        self.assertEqual(response.status_code, 405)

    def test_protected_with_invalid_token(self):
        headers = {"Authorization": "Bearer invalidtoken123"}
        response = self.client.get('/protected', headers=headers)
        self.assertEqual(response.status_code, 422)

if __name__ == '__main__':
    unittest.main()
