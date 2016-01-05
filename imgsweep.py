import praw
import urllib
import os
import sys
import argparse


# Define Globals
USER_AGENT = "python: mayr.redditCrawlerApp:v0.0.1"
DEFAULT_SUBREDDIT = "indianbabes"
DEFAULT_POST_LIMIT = 20 # (Maximum is 100 per PRAW reddit API call.)
DOWNLOADED_IMAGE_FOLDER = "download"

__version__ = "0.0.2"
__author__ = "Lawrence Adams"

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
def filter_urls(input_list):
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
	filename = str(os.getcwd()) + str("\\download\\") + _get_filename_from_url(image_url)
	urllib.request.urlretrieve(image_url, filename)


"""
TODO

Find if file is present. Go to lowest int count for name of file.
 >>> e.g. 00001.jpg is present, so name next file 00002.jpg
"""
# def _file_present(directory):

# -------- PRIVATE FUNCTIONS --------
def _check_download_directory_present():
	if os.path.exists(DOWNLOADED_IMAGE_FOLDER) and os.path.isdir(DOWNLOADED_IMAGE_FOLDER):
		pass
	else:
		print("---> [WARN] No download directory detected, creating...")
		os.mkdir(DOWNLOADED_IMAGE_FOLDER)

def _get_filename_from_url(dirtyUrl):
	return str(dirtyUrl.split('/')[-1].split(".jpg")[0] + ".jpg")

def _overwrite_console_output(output):
	sys.stdout.write("\r" + output)
	sys.stdout.flush()

# -------- MAIN --------
def main(subredditToSweep, numberOfPosts):
	print("ImgSweep " + __version__ + ", " + __author__ + "\n")
	print("---> Getting top " + str(numberOfPosts) + " post(s) from subreddit " + subredditToSweep)

	links = filter_urls(get_image_urls(subredditToSweep, numberOfPosts))

	print("---> Got " + str(len(links)) + " links")

	_check_download_directory_present()

	for link in links:
		# _overwrite_console_output("---> Downloading: " + link)
		print("---> Downloading: " + link)
		download_image(link)

	print("\n---> Downloaded " + str(len(links)) + " image(s)")


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("subreddit", help="Subreddit to sweep.")
	parser.add_argument("posts", help="Number of posts to check", type=int)
	parser.add_argument("--silent", help="Disable output to console", action="store_true")

	args = parser.parse_args()

	targetSubreddit = args.subreddit
	targetPosts = args.posts

	if args.silent:
		sys.stdout = open(os.devnull, 'w')

	try:
	    main(targetSubreddit, targetPosts)
	except KeyboardInterrupt: # Handle Ctrl+C interrupts silently
	    print('[ERROR] Operation cancelled.')
	    try:
	        sys.exit(0)
	    except SystemExit:
	        os._exit(0)