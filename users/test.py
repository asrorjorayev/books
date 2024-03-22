from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import get_user

# test register page
class RegisterTestCace(TestCase):
# registerni test qilishj
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



# # username test
#     def test_register_field(self):
#         response=self.client.post(
#             reverse('users:register'),
#             data={
#                 'username':'asd',
#                 'first_name':'sardorbek',
#                 'last_name':'egamberdiyev',
#                 'email':'s@gmail.com',
#                 'password':'2003',
#                 'password_confirm':'2003',
                
#             }
#         )
#         form=response.context['form']
#         user_count=User.objects.all().count()

#         self.assertEqual(user_count,0)
#         self.assertTrue(form.errors)
#         self.assertIn('username',form.errors.keys())
#         self.assertEqual(form.errors['username'],["username uzunligi 5 dan katta 30 dan kichik bolishi kerakl"])
        
# #password test
#     def test_password_field(self):
#         response=self.client.post(
#         reverse('users:register'),
#         data={
#                 'username':'asr',
#                 'first_name':'sardorbek',
#                 'last_name':'egamberdiyev',
#                 'email':'s@gmail.com',
#                 'password':'2003',
#                 'password_confirm':'203',
                
#             }
#         )
#         form=response.context['form']
#         user_count=User.objects.all().count()
#         self.assertEqual(user_count,0)
#         self.assertTrue(form.errors)
#         self.assertIn('password_confirm',form.errors.keys())
#         self.assertEqual(form.errors['password_confirm'],['Parolni tekshiring va bir xil kiriting'])
# #Email test
#     def test_email(self):
#         response=self.client.post(
#             reverse('users:register'),
#             data={
#                 'username':'asror',
#                 'first_name':'sardorbek',
#                 'last_name':'egamberdiyev',
#                 'email':'s@gmail',
#                 'password':'2003',
#                 'password_confirm':'203',
                
#             }
#         )

#         form=response.context['form']
#         user_count=User.objects.all().count()
#         self.assertEqual(user_count,0)
#         self.assertTrue(form.errors)
#         self.assertIn('email',form.errors.keys())
#         self.assertEqual(form.errors['email'],['Enter a valid email address.'])
# #Username test
#     # def test_username(self):
#         response=self.client.post(
#             reverse('users:register'),
#             data={
#                 'username':'sardor',
#                 'first_name':'sardorbek',
#                 'last_name':'egamberdiyev',
#                 'email':'s@gmail.com',
#                 'password':'2003',
#                 'password_confirm':'2003',
#                  }
#         )

#         form=response.context['form']
#         user_count=User.objects.all().count()
#         self.assertEqual(user_count,1)
#         self.assertTrue(form.errors)
#         self.assertIn('username',form.errors.keys())
#         # self.assertEqual(form.errors['username'],['A user with that username already exists.'])

        
        
        
        

# #login test
# class loginTestCase(TestCase):
#     def test_login(self):
#         user=User.objects.create(username='asrorbek',first_name='asror',last_name='jorayev')
#         user.set_password('1234')
#         user.save()
#         self.client.post(
#             reverse('users:login_page'),
#             data={
#                 'username':'asrorbek',
#                 'password':'1234'
#             }
#         )
#         user_cpount=User.objects.all().count()
#         self.assertEqual(user_cpount,1)

#         user=get_user(self.client)
#         self.assertTrue(user.is_authenticated)

    

#     def test_logout(self):
#         user=User.objects.create(username='asrorbek',first_name='asror',last_name='jorayev')
#         user.set_password('1234')
#         user.save()
#         self.client.post(
#             reverse('users:login_page'),
#             data={
#                 'username':'asrorbek',
#                 'password':'123'
#             }
#         )
#         user_cpount=User.objects.all().count()
#         self.assertEqual(user_cpount,1)

#         user=get_user(self.client)
#         self.assertFalse(user.is_authenticated)
