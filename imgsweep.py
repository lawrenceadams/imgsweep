# Imports
import praw

# Define Globals
USER_AGENT = "python: mayr.redditCrawlerApp:v0.0.1"
SUBREDDIT = "funny"
POST_LIMIT = 5 # (Maximum is 100 per PRAW reddit API call.)

# Initialise new PRAW instance
r = praw.Reddit(user_agent=USER_AGENT)

# Get all posts by subreddit
# posts = r.get_subreddit(SUBREDDIT).get_hot(limit=POST_LIMIT)

# Return these --> console.
# If stickied, ignore post
# print("---> Getting top 5 posts in subreddit: " + SUBREDDIT +"\n")
# for post in posts:
# 	if not post.stickied:
# 		print(post.url)

"""
	So we can get the top x posts ~ and can get URL attribute.
	Now we need to go through SUBREDDIT and determine if the url is an IMG or a SELF post.
"""
# print("---> Getting top 5 posts in subreddit: " + SUBREDDIT +"\n")
# for post in posts:
# 	if not post.stickied: # Probably not needed...
# 		if not post.is_self: # Is a self post?? 
# 			print(post.url) # woop

# We should turn this into a function!

"""
Learn PEP function guideline...

TODO: Filter images (png, jpg, bmp) from gif, gifv, non-image url etc
"""
def get_image_urls():
	posts = r.get_subreddit(SUBREDDIT).get_hot(limit=POST_LIMIT)

	for post in posts:
		if not post.stickied: # Probably not needed...
			if not post.is_self: # Is a self post?? 
				print(post.url) # woop

get_image_urls()