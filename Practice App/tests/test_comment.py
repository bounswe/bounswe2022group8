from urllib import response
from rest_framework import status
from rest_framework.test import APITestCase
from django.test import TestCase, Client
from api.serializers import CommentSerializer
from api.models import ArtItem, Tag, myUser,Comment
from django.contrib.auth.models import User
import json
from faker import Faker

class TestComment(APITestCase):
  
    def setUp(self):  

        # setting up for the test
        print("TestComment:setUp_:begin")
        
        ##### Mock up data #####

        fake = Faker()
        self.client = Client()

        user1 = User.objects.create(username = fake.unique.first_name(), password=fake.password())
        user2 = User.objects.create(username = fake.unique.first_name(), password=fake.password())

        myUser1 = myUser.objects.create(user=user1, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        myUser2 = myUser.objects.create(user=user2, name= fake.first_name(), surname = fake.last_name(), email = fake.email())
        
        tag1 = Tag.objects.create(tagname = fake.word(), description = fake.paragraph(nb_sentences=3))
        tag2 = Tag.objects.create(tagname = fake.word(), description = fake.paragraph(nb_sentences=3))
        artitem1 = ArtItem.objects.create(title= fake.word(), description = fake.paragraph(nb_sentences=3), owner = myUser1, artitem_image = fake.file_path(depth=1, category='image', extension='png'))
        artitem2 = ArtItem.objects.create(title= fake.word(), description = fake.paragraph(nb_sentences=3), owner = myUser2, artitem_image = fake.file_path(depth=1, category='image', extension='png'))
        artitem1.tags.add(tag1)
        artitem2.tags.add(tag2)

        comment1 = Comment.objects.create(body= fake.sentence(), commented_by = myUser1, commented_on = artitem1, created_at = fake.date_time_between() , updated_at= fake.future_date())
        comment2 = Comment.objects.create(body= fake.sentence(), commented_by = myUser2, commented_on = artitem2, created_at = fake.date_time_between() , updated_at= fake.future_date())
       
        self.user = myUser2
        self.artitem = artitem2
        self.commentId = comment2.id
    
        print("TestComment:setUp_:end")


    def tearDown(self):
        # cleaning up after the test
        print("TestComment:setUp_:begin")

        # do something
        print("TestComment:setUp_:end")


    def test_commentsOfArtItem_get(self):
        for id in range(1, 3):
            response = self.client.get('/api/v1/comments/artitem/{}'.format(id))
            
            self.assertEqual(response.status_code, 200)  # check status code
            
            serializer = CommentSerializer(Comment.objects.filter(commented_on=id), many=True)
            expected = serializer.data
            self.assertEqual(response.json(), expected)


    def test_commentOfArtItems_post(self):

        fake = Faker()
        newBody = fake.sentence()
        newComment = {'id':3,
        'body' : newBody,
        'commented_by' :self.user.id,
        'commented_on': self.artitem.id}

        response = self.client.post('/api/v1/comments/artitem/{}'.format(self.artitem.id), data = newComment,  headers = {'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 201)  # check status code
       
        serializer = CommentSerializer(Comment.objects.get(pk=3)) # lastly added
        expected = serializer.data
        self.assertEqual(response.json(), expected)
        

    def test_getDeleteComment_get(self):
        response = self.client.get('/api/v1/users/{id}/comment/{commentid}'.format(id= self.user.id, commentid=self.commentId))
        self.assertEqual(response.status_code, 200)  # check status code
            
        serializer = CommentSerializer(Comment.objects.get(pk=self.commentId))
        expected = serializer.data
        self.assertEqual(response.json(), expected)


    def test_getDeleteComment_delete(self):
        response = self.client.delete('/api/v1/users/{id}/comment/{commentid}'.format(id= self.user.id, commentid=self.commentId))
        self.assertEqual(response.status_code, 204)  # check status code
        
        self.assertFalse(Comment.objects.filter(pk=self.commentId).exists())
        