#Tweet Map
---
##Software requirements
Python 2.7 with Flask, Tweepy, and Sqlite3 packages.
See requirements for versions

##Modules
app.py is the Flask project. It serves tweets from a Sqlite database.

sql.py defines the methods to interact with the database.

get_all.py is used to fetch tweets statically. I also have code to stream tweets, but I got rid of it because it would require keeping my credentials on the server. get_all was used to fetch a large number of tweets, but my credentials have also been removed.

Streaming code is in the streaming folder.

##Visit page
http://ccbd-hw1-env-xuuwjzwg3h.elasticbeanstalk.com/map

##Elastic Beanstalk and Load balancing
I followed this site for deploying my site with EB and load balancing enabled:
http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Python_flask.html

Screenshots are included showing that load balancing is on.  


