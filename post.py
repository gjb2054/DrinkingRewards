from datetime import datetime


class Post:

    def __init__(self, post_str, username):
        self.post_str = post_str
        self.username = username
        self.postdate = datetime.now()
