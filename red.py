import praw
import config

def bot_login():
    print ("Logging in...")
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "jigztesting the dogbot v1")
    print("Logged in")

    return r

def run_bot(r):
    print ("Obtaining 30 comments")
    for comment in r.subreddit('a:t5_66rifp').comments(limit=30):
        if "Coin" or "Spin" in comment.body:
            print ("String found")
            comment.reply("Coinami incoming")
            print ("Replied to comment") == comment.id



while True:
    r = bot_login() 
    run_bot(r)
