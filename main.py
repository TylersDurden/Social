from twitter import *


def login():
    credentials = []
    f = open('auth.txt', 'r')
    for line in f:
        credentials.append(line.replace(" ", "").replace("\n", ""))
    token = credentials[0]
    secret = credentials[1]
    consumer_key = credentials[2]
    consumer_secret = credentials[3]
    return Twitter(auth=OAuth(token, secret, consumer_key, consumer_secret))


def crawlTimeline(timeline, twit):
    active = []
    userData = {}
    for line in timeline:
        active.append(line['user']['screen_name'])
    for user in set(active):
        print("Looking at " + user + "'s timeline")
        userData[user] = twit.statuses.user_timeline(screen_name=user)
    return userData, set(active)


def exploreNetwork(t, users):
    print("Exploring Network starting with " + str(len(users)) +
          " different users.")
    initialNetwork = {}
    for user in users:
        attr = []
        auser = t.users.lookup(screen_name=user)
        hasGeo = auser[0]['geo_enabled']
        name = auser[0]['name']
        nfollowers = auser[0]['followers_count']
        nfriends = auser[0]['friends_count']
        verified = auser[0]['verified']
        attr.append(nfollowers)
        attr.append(nfriends)
        attr.append(verified)
        attr.append(hasGeo)
        initialNetwork[name] = attr
        max = 0 
        ppl = {}
    for key, value in initialNetwork.items():
        # print(str(key) + " has " + str(value.pop(0)) + " followers and "
        #     + str(value.pop(0)) + " friends")
        nfollow = value.pop(0)
        ppl[nfollow] = key
        if(max < nfollow):
            max = nfollow
    print(ppl[max] + " has the most Followers. [" + str(max) + "]")
    return initialNetwork


def findUsersFollowers(user):
    URL = "twitter.com/"
    return None


def main():
    twit = login()
    timeline = twit.statuses.home_timeline()
    timelineinfo, users = crawlTimeline(timeline, twit)
    smallNetwork = exploreNetwork(twit, users)


if __name__ == '__main__':
    main()
