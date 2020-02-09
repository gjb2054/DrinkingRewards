from pymongo import MongoClient, DESCENDING, ASCENDING


class DatabaseHome:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://JimWebApp:mogulmove@jimwebapp-idcfd.mongodb.net/test?retryWrites=true&w=majority")
        self.userdb = self.client.JimApp.userdb
        self.homie_post = self.client.JimApp.homie_post
        self.workout_post = self.client.JimApp.workout_post
        self.tip_post = self.client.JimApp.tip_post

    def clean_b(self):
        self.userdb.delete_many({"username":"b"})
        self.homie_post.delete_many({"username":"b"})

    def add_username(self, username):
        if self.userdb.find({"username":username, "loggedOn":True}).count() > 0:
            return False
        else:
            if self.userdb.find({"username":username}).count() >0:
                self.userdb.update_one({"username":username}, {"$set":{"loggedOn":True}})
            else:
                userInfo = {
                    "username": username,
                    "rating": "0.00",
                    "ratings": [],
                    "experience": "0",
                    "position": "Casual",
                    "level": "Beginner",
                    "workout_type": "Cardio",
                    "loggedOn":True
                }
                self.userdb.insert_one(userInfo)
            return True

    def sign_out(self, username):
        self.userdb.update_one({"username":username},{"$set":{"loggedOn":False}})

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

    def find_usernames(self):
        user = self.userdb.find({}, {"username": 1, "_id": 0})
        return user

    def find_user(self, username):
        return self.userdb.find_one({"username": username})

    def edit_user(self, user, rating, ratings, experience, position, level, workout_type):
        self.userdb.update_one({"username":user},{"$set":{"rating":rating,"ratings":ratings,"experience":experience,"position":position,"level":level,"workout_type":workout_type}})

    def logout_user(self, username):
        user = self.userdb.update_one({"username": username}, {"$set":{"loggedOn":False}})

    def add_homie_post(self, homie_post):
        postInfo = {
            "username": homie_post.username,
            "post_str": homie_post.post_str,
            "posted": homie_post.postdate
        }
        self.homie_post.insert_one(postInfo)

    def get_sorted_homie_post(self):
        posts = self.homie_post.find({}).sort('posted', DESCENDING)
        return posts

    def add_workout_post(self, workout_post):
        postInfo = {
            "post_str": workout_post.post_str,
            "body_part": workout_post.body_part,
            "ratings": workout_post.ratings,
            "rating": workout_post.rating
        }
        self.workout_post.insert_one(postInfo)

    def get_body_workout_post(self, body_part):
        posts = self.workout_post.find({body_part})
        return posts

    def get_all_body_workout_post(self):
        posts = self.workout_post.find({}).sort("body_part", DESCENDING)
        return posts

    def add_tip_post(self, tip_post):
        postInfo = {
            "username": tip_post.username,
            "post_str": tip_post.post_str,
            "ratings": tip_post.ratings,
            "rating": tip_post.rating,
            "option": tip_post.option
        }
        self.tip_post.insert_one(postInfo)

    def get_spec_tips(self, param):
        posts = self.tip_post.find({"option":param}).sort("rating", DESCENDING)
        return posts

    def get_all_tip_posts(self):
        posts = self.tip_post.find({}).sort("ratings", DESCENDING)
        return posts
