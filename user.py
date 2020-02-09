

class User:

    def __init__(self, level, username, ratings, workout_type, position, experience):
        self.level = level
        self.ratings = ratings
        self.rating = 0
        count = 0
        for r in ratings:
            self.rating += float(r)
            count += 1
        if count != 0:
            self.rating = f"{(self.rating/count):.2f}"
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
            rate += float(r)
            count += 1
        self.rating = f"{(rate/count):.2f}"

    def set_username(self, username):
        self.username = username

    def set_position(self, position):
        self.position = position

    def set_experience(self, experience):
        self.experience = experience
