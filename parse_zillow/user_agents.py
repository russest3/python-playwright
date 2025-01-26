#!/usr/bin/python3
from fake_useragent import UserAgent

def getRandomUserAgent():
    ua = UserAgent()
    random_user_agent = ua.random
    return random_user_agent
