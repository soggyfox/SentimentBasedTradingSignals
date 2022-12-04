# Bachelor Thesis Project
## Sentiment Analysis Trading Signals
Trading bots have become commonplace.
They use a wide array of different algorithms and 
heuristics with the goal of predicting future stock prices via extrapolation.
Current implementations range from using machine learning to availing of basic 
trading strategies such as the relative strength index. Here we use sentiment analysis.
A lot of research has been carried out on analysing market sentiment which provide the 
positive and negative signals but here we will go more in depth with regard to the strength
in trading signals which none of the literature provides and is one of the gap observed 
in the literature review.

## Project Methodology
The whole methodology and literature review can be seen on the "thesis Submission pdf in the route folder of this git repo"

## Set up Natural language processor 
Go to https://github.com/labteral/ernie and then go to
"open in collab" --> https://colab.research.google.com/drive/10lmqZyAHFP_-x4LxIQxZCavYpPqcR28c

Use roberta and ernie to train your model on the training dataset. 
Find the data set I used here https://data.world/mercal/btc-tweets-sentiment.

Now download the output directory. This contains your trained natural language processor.
Use your natural language processor to create sentiment scores for your testing data set.
I used https://www.kaggle.com/kaushiksuresh147/bitcoin-tweets\\?select=Bitcoin\_tweets.csv.

One can contract their data set using an excell modifier to get one out of every 50 rows. Then append market sentiment scores to each one of the tweets.
Change the date format which will allow you to obtain the BTC price on said given day. 

Now use the jupytr files to plot graphs and analyse your findings.
Different strategies can be created from then on. 

## Conclusions
The bot was able to outperform a "buy and hold bitcoin strategy". Pseudo Trades were made on the Binance platform. There you can make a virtual account and trade with fake money.

## Future Works 
To test your new founded trading strategies in real time, you can use twitters API which allows you to get tweets in real time. From here you can trade based on your indicators. Platforms such as binance allow easy connection to a tarding bot by use of the biancne API. 

use the command pip install python-binance. See docs here
https://pypi.org/project/python-binance/
