import praw
import urllib
import os

# Define Globals
USER_AGENT = "python: mayr.redditCrawlerApp:v0.0.1"
DEFAULT_SUBREDDIT = "all"
DEFAULT_POST_LIMIT = 5 # (Maximum is 100 per PRAW reddit API call.)
DOWNLOADED_IMAGE_FOLDER = "download"

# Initialise new PRAW instance
r = praw.Reddit(user_agent=USER_AGENT)

"""
A function that gets the top $x links from $subreddit.
Removes stickies. Does not filter images from other links.
"""
def get_image_urls(subreddit, post_limit):
	posts = r.get_subreddit(subreddit).get_hot(limit=post_limit)
	result = []

	for post in posts:
		if not post.stickied: # Ignore stickied posts
			result.append(post.url) # Add each post ---> Result.
	return result

"""
A function that takes a list and returns links ONLY containing valid images.
Will *not* handle albums (e.g. Imgur albums)

#WARN: only finds .jpg at the moment.
"""
def filter_links(input_list):
	result = [] # New empty list 

	for link in input_list:
		if link.find("jpg") == -1:
			pass
		else:
			result.append(link)
	return result

"""
A function that takes a single url as a string, and downloads the associated image.
"""
def download_image(image_url):
	filename = image_url.split('/')
	urllib.request.urlretrieve(image_url, filename + ".jpg")

"""
TODO

Find if file is present. Go to lowest int count for name of file.
 >>> e.g. 00001.jpg is present, so name next file 00002.jpg
"""
# def _file_present(directory):

def _is_download_directory_present():
	if os.path.exists(DOWNLOADED_IMAGE_FOLDER) and os.path.isdir(DOWNLOADED_IMAGE_FOLDER):
		pass
	else:
		os.makedir(DOWNLOADED_IMAGE_FOLDER)



if __name__ == "__main__":
	i = get_image_urls(DEFAULT_SUBREDDIT, DEFAULT_POST_LIMIT)
	# print(i)	