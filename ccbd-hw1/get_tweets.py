import tweepy

consumer_key        = ""
consumer_secret     = ""
access_token        = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

import sql as s

c = s.connect_db()


for tweet in tweepy.Cursor(api.search,
                           q="ebola OR isis OR world series",
                           count=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    if(tweet.geo):
        coords = tweet.geo['coordinates']
        s.insert(c,tweet.created_at, tweet.text.strip().encode('ascii','ignore'), str(coords))
        #print ("%s,%s,%s") % (tweet.created_at, tweet.text.encode('utf-8').strip(), coords)
    else:
        s.insert(c,tweet.created_at, tweet.text.strip().encode('ascii','ignore'), "None")
      #print ("%s,%s,%s") % (tweet.created_at, tweet.text.encode('utf-8').strip(), tweet.geo)
    #print tweet._json
    #print "\n"


    ''' Attributes of tweet:
    ['__class__', '__delattr__', '__dict__', '__doc__', '__format__', 
    '__getattribute__', '__getstate__', '__hash__', '__init__', '__module__', 
    '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
    '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_api', 
    '_json', 'author', 'contributors', 'coordinates', 'created_at', 'destroy',
     'entities', 'favorite', 'favorite_count', 'favorited', 'geo', 'id', 
     'id_str', 'in_reply_to_screen_name', 'in_reply_to_status_id', 
     'in_reply_to_status_id_str', 'in_reply_to_user_id', 
     'in_reply_to_user_id_str', 'lang', 'metadata', 'parse', 'parse_list', 
     'place', 'possibly_sensitive', 'retweet', 'retweet_count', 'retweeted',
      'retweets', 'source', 'source_url', 'text', 'truncated', 'user']
    '''
