

class User:

    def __init__(self, level, username, ratings, workout_type, position, experience):
        self.level = level
        self.ratings = ratings
        self.rating = "0"
        count = 0
        #for r in ratings:
            #self.rating += r
            #count += 1
        #if count != 0:
            #self.rating = self.rating/count
        self.username = username
        self.workout_type = workout_type
        self.position = position
        self.experience = experience

    def change_workout(self, workout):
        self.workout_type = workout

    def get_rated(self, rating):
        self.ratings.add(rating)
        rate = 0
        count = 0
        for r in self.ratings:
            rate += r
            count += 1
        self.rating = rate/count

    def set_username(self, username):
        self.username = username

    def set_position(self, position):
        self.position = position

    def set_experience(self, experience):
        self.experience = experience

    def to_json(self):
        return "{\"username\":\""+self.username+"\",\"rating\":\""+self.rating+"\",\"level\":\""+self.level+"\",\"position\":\""+self.position+"\",\"experience\":\""+self.experience+"\",\"workout_type\":\""+self.workout_type+"\"}"
