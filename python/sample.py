#!/opt/local/bin/python33
# -*- coding: utf-8 -*-
import oauth2
import urllib2
import json

consumer_key        = ""
consumer_secret     = ""
access_token        = ""
access_token_secret = ""
api_endpoint        = "https://stream.twitter.com/1.1/statuses/sample.json"

consumer = oauth2.Consumer(
	key = consumer_key,
	secret = consumer_secret
)
token = oauth2.Token(
	key = access_token,
	secret = access_token_secret
)

signature_method_hmac_sha1 = oauth2.SignatureMethod_HMAC_SHA1()
oauth_request = oauth2.Request.from_consumer_and_token(
	consumer,
	token=token,
	http_method='GET',
	http_url=api_endpoint
)
oauth_request.sign_request(signature_method_hmac_sha1, consumer, token)

res = urllib2.urlopen(oauth_request.to_url())
for r in res:
	tweet = json.loads(r)
	if "delete" in tweet:
		continue
	if tweet["user"]["lang"] != "ja":
		continue
	print("%s: %s" % (tweet["user"]["name"], tweet["text"]))
