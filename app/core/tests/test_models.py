from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelsTests(TestCase):
    def test_new_user_email_normalized(seft):
        email = 'test@can.com'
        user = get_user_model().objects.create_user(email,'can')

        seft.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'can123')

    def test_create_new_supperuser(self):
        user = get_user_model().objects.create_superuser(
            'test@can.com',
            'can'
        )            

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)