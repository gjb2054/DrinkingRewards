from post import Post


class WorkoutPost(Post):

    def __init__(self, post_str, username, body_part):
        Post.__init__(self, post_str, username)
        self.body_part = body_part

