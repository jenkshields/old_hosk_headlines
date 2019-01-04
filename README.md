# hosk_headlines

NOTE: this has been [rewritten in ruby](https://github.com/jenkshields/hosk_headlines).

Python bot to generate nzherald-style Mike Hosking headlines &amp; comments. Though created from twitter bots this does not post to twitter.

Update: Returned to esdalmaijer's markovbot as basis. hosk.py (based on srome's tutorial) runs but does not output... hosking_bot.py runs as expected. 

Old:

Working based on this tutorial: http://srome.github.io/Making-A-Markov-Chain-Twitter-Bot-In-Python/

Did it from scratch because while the first take (using https://github.com/esdalmaijer/markovbot) enabled me to read from two files (to generate the "Mike Hosking: [GENERATED HEADLINE]" and "COMMENT: [GENERATED COMMENT]" syntax) it used too much of the original string in a way that wasn't satisfying. Second attempt (using https://github.com/tommeagher/heroku_ebooks) had the sensibilty variable I was looking for, but I couldn't find a way with the existing code to read from two files and generate output in two parts - so I decided to start from scratch and use it as a learning opportunity!
