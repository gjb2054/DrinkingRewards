from post import Post


class HomiePost(Post):

    def __init__(self, post_str, username):
        Post.__init__(self, post_str, username)

    def get_time(self):
        return self.workout_time
