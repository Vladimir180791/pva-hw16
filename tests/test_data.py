class TestData:
    BASE_URL = "https://demo.opencart.com/"
    ADMIN_URL = "https://demo.opencart.com/admin/"
    ADMIN_USERNAME = "user"
    ADMIN_PASSWORD = "bitnami"
    
    # Test product data
    TEST_PRODUCT = {
        'name': 'Test Product ',
        'meta_tag': 'test meta tag',
        'model': 'Test Model',
        'price': '100',
        'quantity': '10'
    }
    
    # Test user data
    @staticmethod
    def get_test_user():
        import random
        random_num = random.randint(1000, 9999)
        return {
            'first_name': 'Test',
            'last_name': 'User',
            'email': f'testuser{random_num}@example.com',
            'telephone': '1234567890',
            'password': 'testpassword123'
        }