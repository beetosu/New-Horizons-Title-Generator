# New Horizons Title Generator
A twitter bot that generates all possible passport titles for the game "Animal Crossing: New Horizons" every hour

Basically 2 different files:
* create_list.py: takes the left and right titles (compiled in left.txt and right.txt respectively) to create all possible combinations (titles.json)
* tweet_title.py: tweets an entry from titles.json, removes said entry, and places it in outbox.json



In total it is about 28724 titles, meaning it will just under 1200 days (or 3 1/4 years) to finish running through everything.
