import praw
import config

print "It's running"

def bot_login():
    r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "DeeterC's Bob Ross quote responder v0.1")
    return r

def run_bot(r):
    print "Logged in..."
    for comment in r.subreddit("test").comments(limit=10):
        if "happy little" in comment.body:
            print "String found"
            comment.reply('"You can do anything you want to do. This is your world." - Bob Ross')

r = bot_login()
run_bot(r)
print "...finished"