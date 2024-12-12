class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self):
        print(f"{self.username} has logged in.")
    
    def post(self, content):
        print(f"{self.username} posted: {content}")

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers
    
    def share_story(self, story_content):
        print(f"{self.username} shared a story: {story_content}")

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets
    
    def tweet(self, tweet_content):
        self.number_of_tweets += 1
        print(f"{self.username} tweeted: {tweet_content}")
        print(f"Total tweets: {self.number_of_tweets}")


insta_account = InstagramAccount("insta_user", "insta_pass", 150)
insta_account.login()
insta_account.post("Check out my latest photo!")
insta_account.share_story("Loving the sunset!")
print(f"Followers: {insta_account.number_of_followers}")

twitter_account = TwitterAccount("twitter_user", "twitter_pass", 30)
twitter_account.login()
twitter_account.tweet("Just had an amazing lunch!")
print(f"Tweets: {twitter_account.number_of_tweets}")