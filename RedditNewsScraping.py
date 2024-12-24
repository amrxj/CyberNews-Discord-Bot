import praw

#initialize Reddit API w/ credentials

reddit = praw.Reddit(
    client_id = 'CLIENT ID REDDIT HERE',
    client_secret = 'CLIENT SECRET HERE',
    user_agent = 'CyberNewsBot V1.0 by /u/Dry-Ad2357' #tbh anything here. 
)

def get_news():
#get our cybersecurity subreddit to scrape. 
    subreddit = reddit.subreddit('cybersecurity')
        
#base off of popularity as > upvotes = more important news
    upvote_minimum = 100 #only focus on the trending posts

    news_to_send = []

#we only want news, so we must specify which flairs in an index
    desired_flairs = ['news - general', 'news - breaches & ransoms', 'news - vulnerabilities']


#loop through the subreddit posts, filter by flair and upvote minimum
    for post in subreddit.top(time_filter='week', limit = 100): #100 for now, just a temp thing
        #strip whitespace and cmp
        if post.link_flair_text.strip().lower() in [flair.lower() for flair in desired_flairs]  and post.score >= upvote_minimum:
            news_to_send.append({
                "Title": post.title,
                "URL": post.url,
                "Category": post.link_flair_text
            }) 


    
    return news_to_send
