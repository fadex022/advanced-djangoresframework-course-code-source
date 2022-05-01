import email
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        #Test creating a new user with a email is successful
        email = "fadel@mail.com"
        password = "12345"
        user = get_user_model().objects.create_user(
            email= email,
            password= password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        #Test if a new user's email is normalized
        email = "fadel@EMaIl.Com"
        user = get_user_model().objects.create_user(
            email= email, 
            password=("12345")
        )

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        #Test if a new user's email is valid
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password=("12345")
            )
    
    def test_create_superuser(self):
        #Test creating a super user
        user = get_user_model().objects.create_superuser(email="fadel@email.com", password="12345")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)