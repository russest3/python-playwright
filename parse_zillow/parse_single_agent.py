from parsel import Selector
from playwright.sync_api import sync_playwright, Page
import re

def parse_agent(selector):
    _new_agency_address = []
    _new_agency_address_str = ""
    _name = selector.css("h1.Text-c11n-8-107-0__sc-aiai24-0 ::text").get()
    _agency = selector.xpath("//*[@id='__next']/div/div[2]/div[1]/header/div/div/div[1]/div/div[2]/div/div[2]/span/text()").get()
    _agency_url = selector.xpath("//*[@id='get-to-know-me']/div/div[2]/div/div[3]/a/@href").get()
    _agent_email = selector.xpath("//*[@id='__next']/div/div[2]/div[3]/div/div/div/div[3]/div/div[3]/a/@href").get()
    _agent_email = re.sub("mailto:", "", _agent_email)
    _agent_cell = selector.xpath("//*[@id='__next']/div/div[2]/div[3]/div/div/div/div[3]/div/div[1]/a/@href").get()
    _agent_cell = re.sub("tel:", "", _agent_cell)
    _agency_phone = selector.xpath("//*[@id='__next']/div/div[2]/div[3]/div/div/div/div[3]/div/div[2]/a/@href").get()
    _agency_phone = re.sub("tel:", "", _agency_phone)
    _agency_address = selector.xpath("//*[@id='__next']/div/div[2]/div[3]/div/div/div/div[3]/div/div[4]/a/text()").getall()
    for i in _agency_address:
        if ',' not in i:
            _new_agency_address.append(i)
    for i in _new_agency_address:
        _new_agency_address_str = _new_agency_address_str + ' ' + str(i)
    result = {
        "name": _name,
        "agency": _agency,
        "agency_url": _agency_url,
        "agent_email": _agent_email,
        "agent_cell": _agent_cell,
        "agency_phone": _agency_phone,
        "agency_address": _new_agency_address_str
    }
    return result
