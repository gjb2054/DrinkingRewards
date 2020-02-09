from post import Post


class TipPost(Post):

    def __init__(self, post_str, username, ratings):
        Post.__init__(post_str, username)
        self.ratings = ratings
        count = 0
        rating = 0
        for r in ratings:
            self.rating += float(r)
            count += 1
        self.rating = f"{(rating/count):.2f}"
