import os, json, tweepy

def tweet():
    #setup the actual bot
    consumer = [os.environ.get('NH_C_KEY'), os.environ.get('NH_C_SECRET')]
    access = [os.environ.get('NH_A_TOKEN'), os.environ.get('NH_A_TOKEN_SECRET')]

    auth = tweepy.OAuthHandler(consumer[0], consumer[1])
    auth.set_access_token(access[0], access[1])
    api = tweepy.API(auth)

    #open the availble titles list and pick the first one
    with open("titles.json") as f:
        titleList = json.load(f)
    title = titleList.pop()

    #grab all the titles that have already been tweeted and add the new title
    with open('outbox.json') as f:
        outbox = json.load(f)
    outbox.append(title)

    #actually tweet
    api.update_status(title)

    #update titles with the used title removed
    with open("titles.json", 'w') as z:
        json.dump(titleList, z)

    #add the new title to the outbox file
    with open("outbox.json", 'w') as z:
        json.dump(outbox, z)

if __name__ == "__main__":
    tweet()
