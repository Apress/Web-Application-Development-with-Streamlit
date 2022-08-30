from API import api_instance
import datetime


def get_feed():
    to_date = datetime.datetime.now()
    from_date = to_date - datetime.timedelta(days=1)
    posts = api_instance.get_posts(from_date, to_date)
    return posts
