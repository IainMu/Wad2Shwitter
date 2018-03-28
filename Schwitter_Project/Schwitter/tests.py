from django.test import TestCase
from Schwitter.models import UserProfile, Post, Comment
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import Client
# Create your tests here.

def add_user(user):
    u = User.objects.get_or_create(username=user["username"], password=user["password"], email=user["email"])[0]
    u.set_password(user["password"])
    u.save()
    return u


def add_userprofile(user):
    u = UserProfile.objects.get_or_create(user=add_user(user))[0]
    u.save()
    return u


def add_friends(user):
    u = UserProfile.objects.get(user=User.objects.get(username=user["username"]))
    for friend in user["friends"]:
        f = UserProfile.objects.get(user=User.objects.get(username=friend))
        u.friends.add(f)
    u.save()

def add_post(post):
    u = UserProfile.objects.get(user=User.objects.get(username=post["poster"]))
    p = Post.objects.get_or_create(poster = u, title = post["title"], time = post["time"] , content = post["content"], likes = post["likes"], slug = post["slug"] )[0]
    p.save()
    return p

class UserTestCase(TestCase):

    def test_user_profile (self):
        #testing data housed in user profile model
        users = [{"username": "Testy", "password": "testpassword", "email": "test@test.com",
                  "friends": ["Testy2", "Testy3"]},
                 {"username": "Testy2", "password": "testpassword", "email": "test2@test.com",
                  "friends": ["Testy", "Testy3"]},
                 {"username": "Testy3", "password": "testpassword", "email": "test3@test.com",
                  "friends": ["Testy2", "Testy"]}
        ]

        test_user = add_userprofile(users[0])
        test_user2 = add_userprofile(users[1])
        test_user3 = add_userprofile(users[2])

        for user in users:
            add_friends(user)


        self.assertEqual(test_user.user.username, "Testy")
        self.assertEqual(test_user.user.email, "test@test.com")
        self.assertEqual(test_user.friends.count(), 2)

    def test_profile_view (self):
        #testing profile view
        user = {"username": "Testy", "password": "testpassword", "email": "test@test.com"}
        test_user = add_user(user)

        response = self.client.get(reverse('profile',"Testy"))
        self.assertEqual(response.statuse_code, 200)
        self.assertContains(response,"Testy")


class HomeViewTests(TestCase):

    def test_home_view_not_logged_in (self):
        #testing home view when logged in
        response = self.client.get(reverse('home'))
        self.assertEqual(response.statuse_code, 200)
        self.assertContains(response, "Here could be posts, if you were logged in...")

    def test_home_view_logged_in_with_no_posts (self):
        #testing home view when logged in but no posts are displayed
        user = {"username": "Testy", "password": "testpassword", "email": "test@test.com"}
        test_user = add_user(users[0])

        c = Client()
        logged_in = c.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.statuse_code, 200)
        self.assertContains(response, "None of your friends have posted anything...or maybe you just have no friends :P")

    def test_home_view_logged_in_with_posts(self):
        # testing home view when logged in and posts are displayed
        users = [{"username": "Testy", "password": "testpassword", "email": "test@test.com",
                  "friends": ["Testy2", ]},
                 {"username": "Testy2", "password": "testpassword", "email": "test2@test.com",
                  "friends": ["Testy", ]},
                 ]
        test_post = {"poster": "Testy2",
         "post": "Test Post",
         "time": datetime.datetime(2018, 3, 22, 18, 25, 20),
         "content": "This is a test post.",
         "likes": 2}

        test_user = add_userprofile(users[0])
        test_user2 = add_userprofile(users[1])

        for user in users:
            add_friends(user)

        add_post(test_post)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.statuse_code, 200)
        self.assertContains(response, "Test Post")
