twitter = Twython(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def openfiles(filename1, filename2):
    with open(filename1, 'rb') as fileobject2, open(filename2, 'rb') as fileobject2:
        file_lines1, file_lines2 = fileobject1.readlines(), fileobject2.readlines()
        file_lines1 ,filelines2 = [element for element in file_lines1 if len(element) <= 70 and len(element) > 7],
                                  [element for element in file_lines2 if len(element) <= 70 and len(element) > 7]
    return file_lines1, file_lines2


def random_tweets(*file_lines):
    plath_tweet, gaga_tweet = random.choice(file_lines)
    return plath_tweet, gaga_tweet


def tweet_order(*tweets):
    randomchoice = [1,2]  # still trying to figure whats the essence here yet to learn about randoms
    tweetorder = random.choice(randomchoice)
    if tweetorder == 1:
        tweet = "{} {}".format(tweets)
        return twitter.update_status(status=tweet)
    else:
        tweet = "{} {}".format(tweets)
        return twitter.update_status(status=tweet) 


def main():
    files = openfiles('gaga.txt','plath.txt')
    random_tweets = random_tweets(files)
    print(tweet_order(random_tweets))  # testing :)

if __name__ == '__main__' :
    main()
