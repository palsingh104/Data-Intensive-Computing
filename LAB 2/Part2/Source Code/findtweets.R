library(rtweet)
library(dplyr)
library(rtweet)
library(openssl)
library(httpuv)

api_key<-"JwxAZv9mbgAb2d5J5bRRhnDQ2"
api_secret<- "gVniZOmgWBoTLm9VYbKpmPLmboUd89HUIg70DPqWtXhx5ztWDO"
token <- "960987055831617537-6Q38dFTdWUrbSvrj9EQxW1HQ2IkwQbl"
token_secret <-"4uQiMwawbgg3GxWoV6D5gLOXNpM86x3KXpvE3shqNPrA8"

twitter_tokens <- create_token(app = "Flu Analysis",
consumer_key = api_key,
consumer_secret = api_secret)
keywds="#facebook OR #fb OR #cambridgeAnalytica OR #datatheft OR #privacy OR #breach OR 'personal data'"
data=search_tweets( keywds,geocode = lookup_coords("US"), n = 10000,include_rts = FALSE)
x=as.data.frame(data)
xx <- apply(x,2,as.character)

write.csv(xx[,5],'fb tweets.txt')
