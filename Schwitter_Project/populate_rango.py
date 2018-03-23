import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
import datetime
django.setup()
from Schwitter.models import UserProfile, Post, Comment
from django.contrib.auth.models import User

def populate():
    users = {
        "SchwarnoldSchwarzenegger":
         {"username": "SchwarnoldSchwarzenegger",
         "password": "gettotheschwoppa",
         "email": "SchwoleSchwarnold@schwotmail.com"},

        "SchweizerSchnitzel":
        {"username": "SchweizerSchnitzel",
         "password": "Strudel69",
         "email": "Schnitzel@schweiz.ch"},

        "Schweppes":
        {"username": "Schweppes",
         "password": "schwomething",
         "email": "schweppes@schwotmail.com"},

        "Igiveup":
        {"username": "Igiveup",
         "password": "whocares",
         "email": "ehhhhh@Schwotmail.com"}

    }

    user_profiles = {
        "SchwarnoldSchwarzenegger":
        {"user": users["SchwarnoldSchwarzenegger"],
         "friends": ["SchweizerSchnitzel", "Schweppes"]},

        "SchweizerSchnitzel":
        {"user": users["SchweizerSchnitzel"],
         "friends": ["SchwarnoldSchwarzenegger", "Igiveup"]},

        "Schweppes":
            {"user": users["Schweppes"],
             "friends": ["SchwarnoldSchwarzenegger", "SchweizerSchnitzel", "Igiveup"]},

        "Igiveup":
            {"user": users["Igiveup"],
             "friends": ["SchweizerSchnitzel", "Schweppes"]}
    }

    Posts = {
        "Bach": {"poster": "SchwarnoldSchwarzenegger",
         "title": "Bach",
         "time": datetime.datetime(2018, 3, 22, 14, 10, 30),
         "content": "I'll be Bach",
         "likes": 2},

        "BuySchweppes!": {"poster": "Schweppes",
         "title": "Buy Schweppes!",
         "time": datetime.datetime(2018, 3, 22, 17, 15, 20),
         "content": "Please. Buy Schweppes.",
         "likes": 1}
    }

    Comments = [
        {"poster": "SchweizerSchnitzel",
         "post": Posts["Bach"],
         "time": datetime.datetime(2018, 3, 22, 14, 10, 35),
         "content": "I hope you're Bach soon :)",
         "likes": 1},

        {"poster": "Igiveup",
         "post": Posts["BuySchweppes!"],
         "time": datetime.datetime(2018, 3, 22, 18, 25, 20),
         "content": "I hate Schweppes.",
         "likes": 2}
    ]

    user_p_dict = {}
    post_dict = {}

    for user_p in user_profiles:
        user = user_p["user"]
        u = add_user(user["username"], user["password"], user["email"])
        up = add_userprofile(u, user_p["friends"])
        user_p_dict[user["username"]] = up
        for post in Posts:
            if post["poster"] == user["username"]:
                p = add_post(up, post["title"], post["time"], post["content"], post["likes"])
                post_dict[post["title"]] = p

    for com in Comments:
        c = add_comment(user_p_dict[com["poster"]], post_dict[com["post"]], com["time"], com["content"], com["likes"])

def add_user(username, password, email):
    u = User.objects.get_or_create(username = username, email = email, password = password)[0]
    u.save()
    return u

def add_userprofile(user, friends):
    u = UserProfile.objects.get_or_create(user = user, friends = friends)[0]
    u.save()
    return u

def add_post(poster, title, time, content, likes):
    p = Post.objects.get_or_create(poster = poster, title = title, time = time, content = content, likes = likes)[0]
    p.save()
    return p

def add_comment(poster, post, time, content, likes):
    c = Comment.objects.get_or_create(poster=poster, post=post, time=time, content=content, likes=likes)[0]
    c.save()
    return c

if __name__ == '__main__':
    print("starting Schwitter population script...")
    populate()
