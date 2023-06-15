from utils import get_time_id

from twtr import Tweet, Twitter


def main():
    time_id = get_time_id()
    twitter = Twitter()
    tweet = Tweet(f'Hello World from {time_id}')
    twitter.send(tweet)


if __name__ == '__main__':
    main()
