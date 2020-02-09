from pymongo import MongoClient, DESCENDING


class DatabaseHome:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://JimWebApp:mogulmove@jimwebapp-idcfd.mongodb.net/test?retryWrites=true&w=majority")
        self.userdb = self.client.JimApp.userdb
        self.homie_post = self.client.JimApp.homie_post

    def add_user(self, user):
        userInfo = {
            "username": user.username,
            "rating": user.rating,
            "ratings": user.ratings,
            "experience": user.experience,
            "position": user.position,
            "level": user.level,
            "workout_type": user.workout_type
        }
        self.userdb.insert_one(userInfo)

    def add_homie_post(self, homie_post):
        postInfo = {
            "username": homie_post.username,
            "post_str": homie_post.post_str,
            "posted": homie_post.postdate
        }
        self.homie_post.insert_one(postInfo)

    def get_sorted_homie_post(self):
        posts = self.homie_post.find({}).sort('postdate', DESCENDING)
        return posts
