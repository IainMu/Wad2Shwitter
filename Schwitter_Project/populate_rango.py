import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Schwitter_Project.settings')
import django
import datetime
django.setup()
from Schwitter.models import UserProfile, Post, Comment
from django.contrib.auth.models import User

def populate():

    users = [
         {"username": "SchwarnoldSchwarzenegger",
         "password": "gettotheschwoppa",
         "email": "SchwoleSchwarnold@schwotmail.com",
         "friends": ["SchweizerSchnitzel", "Schweppes"]},

        {"username": "SchweizerSchnitzel",
         "password": "Strudel69",
         "email": "Schnitzel@schweiz.ch",
         "friends": ["SchwarnoldSchwarzenegger", "Igiveup"]},

        {"username": "Schweppes",
         "password": "schwomething",
         "email": "schweppes@schwotmail.com",
         "friends": ["SchwarnoldSchwarzenegger", "SchweizerSchnitzel", "Igiveup"]}
         ,

        {"username": "Igiveup",
         "password": "whocares",
         "email": "ehhhhh@Schwotmail.com",
         "friends": ["SchweizerSchnitzel", "Schweppes"]}

    ]

    Posts = [
         {"poster": "SchwarnoldSchwarzenegger",
         "title": "Bach",
         "time": datetime.datetime(2018, 3, 22, 14, 10, 30),
         "content": "I'll be Bach",
         "likes": 2,
         "slug" : "Bach" },

         {"poster": "Schweppes",
         "title": "Buy Schweppes",
         "time": datetime.datetime(2018, 3, 22, 17, 15, 20),
         "content": "Please. Buy Schweppes.",
         "likes": 1,
         "slug" : "BuySchweppes"}
    ]


    Comments = [
        {"poster": "SchweizerSchnitzel",
         "post": "Bach",
         "time": datetime.datetime(2018, 3, 22, 14, 10, 35),
         "content": "I hope you're Bach soon :)",
         "likes": 1},

        {"poster": "Igiveup",
         "post": "BuySchweppes",
         "time": datetime.datetime(2018, 3, 22, 18, 25, 20),
         "content": "I hate Schweppes.",
         "likes": 2}
    ]



    for user in users:
        up = add_userprofile(user)
        print("added " + user["username"])



    for user in users:
        add_friends(user)

    for post in Posts:
        p = add_post(post)
        print("added " + post["title"])
        for comment in Comments:
            if comment["post"] == post["slug"]:
                add_comment(comment, p)
                print("added " + comment["poster"] + "'s comment on " + comment["post"])

def add_user(user):
    u = User.objects.get_or_create(username = user["username"],password = user["password"], email = user["email"])[0]
    u.set_password(user["password"])
    u.save()
    return u

def add_userprofile(user):
    u = UserProfile.objects.get_or_create(user = add_user(user))[0]
    u.save()
    return u

def add_friends(user):
    u = UserProfile.objects.get(user = User.objects.get(username = user["username"]))
    for friend in user["friends"]:
        f = UserProfile.objects.get(user=User.objects.get(username=friend))
        u.friends.add(f)
    u.save()

def add_post(post):
    u = UserProfile.objects.get(user=User.objects.get(username=post["poster"]))
    p = Post.objects.get_or_create(poster = u, title = post["title"], time = post["time"] , content = post["content"], likes = post["likes"], slug = post["slug"] )[0]
    p.save()
    return p

def add_comment(comment, p):
    u = UserProfile.objects.get(user=User.objects.get(username=comment["poster"]))
    #p = Post.objects.get(slug = comment["post"])
    c = Comment.objects.get_or_create(poster= u, post=p, time=comment["time"], content=comment["content"], likes=comment["likes"])[0]
    c.save()
    return c

if __name__ == '__main__':
    print("starting Schwitter population script...")
    populate()
