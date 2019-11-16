import tweepy as tw
# from tweepy import Stream
# from tweepy.auth import OAuthHandler
# from tweepy.streaming import StreamListener
# from tweepy import API


ckey = 'zAiNJKEQE3Ekt5HO5lKLyczAF'
csecret = 'DMXUQVkRbrvOvEWrgqGOk7uDtYink55aw7fgelQ2PZHbJAmSVA'
atoken = '2871600776-LQbNzopvJFzBV1sNomGqi6eSyET80fQwoBXnsRq'
asecret = '06STLNoUWNlqlnOdPCMS17IgKGhtkHRRYd5hplefYGZ6A'


class listener(tw.StreamListener):

    def on_status(self, status):
        print("context == ", status.text)
        print("screen name == " + status.user.screen_name)
        return True

    def on_error(self, status):
        print(status)


auth = tw.OAuthHandler(ckey, csecret)

auth.set_access_token(atoken, asecret)


# twitterStream = tw.Stream(auth, listener())
# twitterStream.filter(follow=['1142414488395821056'])  # listening to a certain object
api = tw.API(auth, wait_on_rate_limit=True)
# api.update_status("大家好") # posting a tweet
# public_tweets = api.home_timeline()

# user = api.get_user('HuangSicong')
# friends = user.friends() # getting user's friends
# for person in friends:
#     print(person.screen_name, person.name)
print(api.user_timeline('Dave2D'))  # getting user timeline
# for e in api.user_timeline('Dave2D'):
#     print("tweet == ", e.text)
print(api.friends('Dave2D'))    # getting friends
# for e in api.friends('Dave2D'):
#     print(e.screen_name, e.name)
