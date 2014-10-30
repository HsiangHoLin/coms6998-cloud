#Tweet Map
---
##Software requirements
Python 2.7 with Flask, Tweepy, and Sqlite3 packages.

##Modules
app.py is the Flask project. It serves tweets from a Sqlite database.

sql.py defines the methods to interact with the database.

get_all.py is used to fetch tweets statically. I also have code to stream tweets, but I got rid of it because it would require keeping my credentials on the server. get_all was used to fetch a large number of tweets, but my credentials have also been removed.




