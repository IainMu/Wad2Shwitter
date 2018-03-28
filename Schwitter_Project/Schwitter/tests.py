from django.test import TestCase
from Schwitter.models import UserProfile, Post, Comment
# Create your tests here.

class UserTestCase(TestCase):
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

    def test_user_profile (self):
        users = [{"username": "Testy", "password": "testpassword", "email": "test@test.com",
                  "friends": ["Testy2", "Testy3"]},
                 {"username": "Testy2", "password": "testpassword", "email": "test2@test.com",
                  "friends": ["Testy", "Testy3"]},
                 {"username": "Testy3", "password": "testpassword", "email": "test3@test.com",
                  "friends": ["Testy2", "Testy"]}
        ]

        test_user = add_user(users[0])
        test_user2 = add_user(users[0])
        test_user3 = add_user(users[0])

        for user in users:
            add_friends(user)


        self.assertEqual(test_user.username, "Testy")
        
