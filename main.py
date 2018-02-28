from twitter import *


def login(token, secret, ckey, csec):
    return Twitter(auth=OAuth(token, secret, ckey, csec))


def main():
    credentials = []
    f = open('auth.txt', 'r')
    for line in f:
        credentials.append(line.replace(" ", "").replace("\n", ""))
    token = credentials[0]
    secret = credentials[1]
    consumer_key = credentials[2]
    consumer_secret = credentials[3]
    twit = login(token, secret, consumer_key, consumer_secret)
    print(twit.statuses.home_timeline()[0])


if __name__ == '__main__':
    main()
