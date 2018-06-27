import os
from markovbot import MarkovBot

tweetbot = MarkovBot()

dirname = os.path.dirname(os.path.abspath(__file__))
headline = os.path.join(dirname, 'hosking_headlines.txt')
comment = os.path.join(dirname, 'hosking_comments.txt')

tweetbot.read(headline)
gen_head = tweetbot.generate_text(10)
print(u'\nMike Hosking: %s' % (gen_head))

tweetbot.clear_data()
tweetbot.read(comment)
gen_comm = tweetbot.generate_text(30)
print('COMMENT: %s' % (gen_comm))