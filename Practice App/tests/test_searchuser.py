from rest_framework.test import APITestCase
from api.models import ArtItem, Tag, myUser
from django.contrib.auth.models import User
from faker import Faker

class TestSearchUsername(APITestCase):
    #creating mockup users 
    def setUp(self):  

        faker = Faker()
        
        self.usernames=[]
        myusers=[[]]*5

        for i in range(5):
            name=faker.unique.first_name()
            surname=faker.unique.last_name()
            email = faker.unique.email()
            pw=faker.unique.password()
            self.usernames.append(name)
            t_user=User.objects.create(username=name,password=pw)
            myusers[i]=myUser.objects.create(user=t_user,name=name,surname=surname,email=email)
            
    

    def tearDown(self):
        
        print("TestSearchUsername:setUp_:begin")

        print("TestSearchUsername:setUp_:end")

    def test_search_by_username(self):
        index=0
        for _ in self.usernames:
            response = self.client.get('/api/v1/search_user/{}'.format(self.usernames[index]))
            self.assertEqual(response.status_code, 200)  # check status code
            index+=1
        
    