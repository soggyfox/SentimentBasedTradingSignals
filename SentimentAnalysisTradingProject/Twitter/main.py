# import requests
# import json
# import config
# import preprocessor as p
# from langdetect import detect
# from ernie import SentenceClassifier
# import numpy as np
#
# # To set your enviornment variables in your terminal run the following line:
# # export 'BEARER_TOKEN'='<your_bearer_token>'
#
# classifier = SentenceClassifier(model_path='./output')
#
# in_position = False
# TRADE_SYMBOL = "BTCUSDT"
# TRADE_QUANTITY = 0.0005
#
# sentimentList = []
# neededSentiment = 500
#
#
# def Average(lst):
#     if len(lst == 0):
#         return len(lst)
#     else:
#         return sum(lst[-neededSentiment:] / neededSentiment)
#
#
# def create_headers(bearer_token):
#     headers = {"Authorization": "Bearer {}".format(bearer_token)}
#     return headers
#
#
# def get_rules(headers, bearer_token):
#     response = requests.get(
#         "https://api.twitter.com/2/tweets/search/stream/rules", headers=headers
#     )
#     if response.status_code != 200:
#         raise Exception(
#             "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
#         )
#     print(json.dumps(response.json()))
#     return response.json()
#
#
# def delete_all_rules(headers, bearer_token, rules):
#     if rules is None or "data" not in rules:
#         return None
#
#     ids = list(map(lambda rule: rule["id"], rules["data"]))
#     payload = {"delete": {"ids": ids}}
#     response = requests.post(
#         "https://api.twitter.com/2/tweets/search/stream/rules",
#         headers=headers,
#         json=payload
#     )
#     if response.status_code != 200:
#         raise Exception(
#             "Cannot delete rules (HTTP {}): {}".format(
#                 response.status_code, response.text
#             )
#         )
#     print(json.dumps(response.json()))
#
#
# def set_rules(headers, delete, bearer_token):
#     # You can adjust the rules if needed
#     sample_rules = [
#         {"value": "bitcoin", "tag": "BBBbitcoin"}
#     ]
#     payload = {"add": sample_rules}
#     response = requests.post(
#         "https://api.twitter.com/2/tweets/search/stream/rules",
#         headers=headers,
#         json=payload,
#     )
#     if response.status_code != 201:
#         raise Exception(
#             "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
#         )
#     print(json.dumps(response.json()))
#
#
# def get_stream(headers, set, bearer_token):
#     response = requests.get(
#         "https://api.twitter.com/2/tweets/search/stream", headers=headers, stream=True,
#     )
#     print(response.status_code)
#     if response.status_code != 200:
#         raise Exception(
#             "Cannot get stream (HTTP {}): {}".format(
#                 response.status_code, response.text
#             )
#         )
#     for response_line in response.iter_lines():
#         if response_line:
#             json_response = json.loads(response_line)
#             # print(json.dumps(json_response, indent=4, sort_keys=True))
#             tweet = json_response['data']['text']
#             tweet = p.clean(tweet)
#             tweet = tweet.replace(':', '')
#             try:
#                 if detect(tweet) == 'en':
#                     print(tweet)
#                     try:
#                         classes = ["bad", "ok", "good"]
#                         probabilities = classifier.predict_one(tweet)
#                         polarity = classes[np.argmax(probabilities)]
#                         print(polarity)
#                         sentimentList.append(polarity)
#
#                         if len(sentimentList) > 5:
#                             endList = sentimentList[-20:]
#                             print("************TOTAL GOOD: " + str(endList.count('good')))
#                             print("************TOTAL BADD: " + str(endList.count('bad')))
#                     except:
#                         pass
#             except:
#                 pass
#
#
# def main():
#     bearer_token = config.BEARER_TOKEN
#     headers = create_headers(bearer_token)
#     rules = get_rules(headers, bearer_token)
#     delete = delete_all_rules(headers, bearer_token, rules)
#     set = set_rules(headers, delete, bearer_token)
#     get_stream(headers, set, bearer_token)
#
#
# if __name__ == "__main__":
#     main()
