#!/opt/local/bin/python33
# -*- coding: utf-8 -*-
import oauth2
import urllib
import urllib2
import json

consumer_key        = ""
consumer_secret     = ""
access_token        = ""
access_token_secret = ""
api_endpoint        = "https://stream.twitter.com/1.1/statuses/filter.json"

consumer = oauth2.Consumer(
	key = consumer_key,
	secret = consumer_secret
)
token = oauth2.Token(
	key = access_token,
	secret = access_token_secret
)

params = {}
params["track"] = "mixi"
p = urllib.urlencode(params)
signature_method_hmac_sha1 = oauth2.SignatureMethod_HMAC_SHA1()
oauth_request = oauth2.Request.from_consumer_and_token(
	consumer,
	token           = token,
	http_method     = 'POST',
	http_url        = api_endpoint,
	parameters      = params,
	is_form_encoded = True
)
oauth_request.sign_request(signature_method_hmac_sha1, consumer, token)

req = urllib2.Request(api_endpoint, oauth_request.to_postdata(), oauth_request.to_header())
res = urllib2.urlopen(req)
for r in res:
	tweet = json.loads(r)
	if "delete" in tweet:
		continue
	print("%s: %s" % (tweet["user"]["name"], tweet["text"]))
