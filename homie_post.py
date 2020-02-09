from post import Post


class HomiePost(Post):

    def __init__(self, post_str, username, time):
        Post.__init__(self, post_str, username)
        self.workout_time = time

    def get_time(self):
        return self.workout_time
