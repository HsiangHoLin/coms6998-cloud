from slistener import SListener
import time, tweepy, sys

def main( mode = 1 ):

    track  = ["ebola"]
    follow = []
    

    ## auth. 
    consumer_key        = ""
    consumer_secret     = ""
    access_token        = ""
    access_token_secret = ""

    # Let's say this is a web app, so we need to re-build the auth handler
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token,access_token_secret)

    api = tweepy.API(auth)


    listen = SListener(api, 'test')
    stream = tweepy.Stream(auth, listen)

    print "Streaming started on %s users and %s keywords..." % (len(track), len(follow))

    try: 
        stream.filter(track = track, follow = follow)
        #stream.sample()
    except:
        print "error!"
        stream.disconnect()

if __name__ == '__main__':
    main()
