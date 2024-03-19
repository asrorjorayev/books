from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class RegisterTestCace(TestCase):

    def test_register(self):
        self.client.post(
            reverse('users:register'),
            data={
                'username':'sardor',
                'first_name':'sardorbek',
                'last_name':'egamberdiyev',
                'email':'s@gmail.com',
                'password':'2003',
                'password_confirm':'2003',
                
            }
        )
        user_count=User.objects.all().count()
        user=User.objects.get(username='sardor')
        self.assertEqual(user_count,1),
        self.assertEqual(user.first_name,'sardorbek')
        self.assertEqual(user.last_name,'egamberdiyev')
        self.assertEqual(user.email,'s@gmail.com')
        self.assertNotEqual(user.password,'2003')
        self.assertTrue(user.check_password,'2003')

class loginTestCase(TestCase):
    def test_login(self):
        self.client.post(
            reverse('users:login_page'),
            data={
                'username':'mushukcha',
                'password':'0000'
            }
        )
        user_cpount=User.objects.all().count()
        user=User.objects.get(username='mushukcha')
        self.assertEqual(user_cpount,1)
        self.assertTrue(user.check_password,'0000')