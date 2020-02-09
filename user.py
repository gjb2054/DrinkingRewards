

class User:

    def __init__(self, level, username, rating, workout_type, position, experience):
        self.level = level
        self.rating = rating
        self.username = username
        self.workout_type = workout_type
        self.position = position
        self.experience = experience

    def change_workout(self, workout):
        self.workout_type = workout