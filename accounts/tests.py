from django.test import TestCase

from django.contrib.auth import get_user_model

class UsersManagerTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "testuser",
            password = "test1234" ,
            email =  "testemail@gmail.com" ,
        )
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"testemail@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username = "testuser",
            password = "test1234" ,
            email =  "testemail@gmail.com" ,
        )
        self.assertEqual(user.username,"testuser")
        self.assertEqual(user.email,"testemail@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)