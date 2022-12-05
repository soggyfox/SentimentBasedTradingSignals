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
The whole methodology and literature review can be seen on the "thesis Submission pdf" in the route folder of this git repo.

## Set up Natural language processor 
Use roberta and ernie to train your model on the training dataset. 
<img width="437" alt="image" src="https://user-images.githubusercontent.com/44605305/205715534-4e68dedb-bf2b-41b5-9095-6baf055bad3d.png">
<img width="754" alt="image" src="https://user-images.githubusercontent.com/44605305/205715668-e122d671-2e71-4953-8e14-f376ab5c6d99.png">

## Collecting and refining the data
### Field research
<img width="516" alt="image" src="https://user-images.githubusercontent.com/44605305/205716864-63fb98ec-f9dc-40d6-bfda-a326731e0edd.png">
### Cleaning and processing tweets 
Decipher whether a tweet has positive or negative market sentiment. Then using the right "trigger condition"(buy-sell algoithm used) to complete a trade of bitcoin on this Binance platform.

<img width="442" alt="image" src="https://user-images.githubusercontent.com/44605305/205717083-14087adb-7034-4d0c-81a0-2eee51d4200f.png">
<img width="403" alt="image" src="https://user-images.githubusercontent.com/44605305/205717099-ec3cddcd-def3-4248-80d5-00e592a8bc1a.png">
<img width="403" alt="image" src="https://user-images.githubusercontent.com/44605305/205717107-b197df0f-d971-449e-81fb-deee62b3f949.png">

## Conclusions
The bot was able to outperform a "buy and hold bitcoin strategy". Pseudo Trades were made on the Binance platform. There you can make a virtual account and trade with fake money.

It was market sentiment in combination with tweet volume that correlated to the price of bitcoin. 
<img width="502" alt="image" src="https://user-images.githubusercontent.com/44605305/205715950-e0e4e330-fed1-488e-81b0-475b0251cf5a.png">
<img width="509" alt="image" src="https://user-images.githubusercontent.com/44605305/205716212-936d3b3b-5388-4266-b134-0258929c1d50.png">
<img width="509" alt="image" src="https://user-images.githubusercontent.com/44605305/205716247-de003750-986a-4cb9-882a-6163362f05a4.png">



## Future Works 
Try tweaking the algorithms used to see what strategies work best. Can other social media platofrms be more useful than twitter at guaging market sentiment?
To test your new founded trading strategies in real time, you can use twitters API which allows you to get tweets in real time. From here you can trade based on your indicators. Platforms such as binance allow easy connection to a TRADING bot. This can be achieved by availing of the biancne API. 

use the command pip install python-binance. See docs here
https://pypi.org/project/python-binance/
