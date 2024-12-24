import praw

#initialize Reddit API w/ credentials

reddit = praw.Reddit(
    client_id = 'client_id'
    client_secret = 'client_secret'
    user_agent = 'user_agent'
)

#get our cybersecurity subreddit to scrape. 
subreddit = reddit.subreddit('cybersecurity')

#base off of popularity as > upvotes = more important news
upvote_minimum = 250 #only focus on the trending posts

#loop through the subreddit posts, filter by flair and upvote minimum
for post in subreddit.new(limit = 10): #10 for now, just a temp thing
    if post.link_flair_text == 'News - Breaches & Ransoms' and post.score >= upvote_minimum:
        print(f"Title: {post.title}")
        print(f"URL: {post.url}")
        print(f"Flair: {post.link_flair_text}")
        print(f"Created: {post.created_est}")