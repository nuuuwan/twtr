
from twtr import Tweet, Twitter


def main():
    twitter = Twitter()
    tweet = Tweet('Hello World from Script!')
    twitter.send(tweet)


if __name__ == '__main__':
    main()
