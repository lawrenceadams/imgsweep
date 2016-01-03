# Imports
import praw

# Define Globals
USER_AGENT = "python: mayr.redditCrawlerApp:v0.0.1"
SUBREDDIT = "funny"

# Initialise new PRAW instance
r = praw.Reddit(user_agent=USER_AGENT)

# Get all posts by subreddit
posts = r.get_subreddit(SUBREDDIT).get_hot(limit=5)

# Return these --> console.
# If stickied, ignore post
print("---> Getting top 5 posts in subreddit: " + SUBREDDIT +"\n")
for post in posts:
	if not post.stickied:
		print(post)