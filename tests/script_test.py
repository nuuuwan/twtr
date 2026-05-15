from utils import Time, TimeFormat

from twtr import Tweet, Twitter


def main():
    time_id = TimeFormat.TIME.format(Time.now())

    twitter = Twitter()
    tweet = Tweet(f"Hello World from {time_id}")
    twitter.send(tweet)


if __name__ == "__main__":
    main()
