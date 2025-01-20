import re
from parsel import Selector
from playwright.sync_api import sync_playwright

def parse_category(selector):
    category_list = selector.xpath("//div[@class='content']/div[@class='background-color-white border-color-cumulus     padding-left-zero padding-right-zero padding-top-small padding-bottom-small border-left-zero border-right-zero border-top-zero border-bottom-1px flex-container flex-align-items-stretch flex-align-content-flex-start flex-full-width amsg-2018 border-color-cumulus design-Sell mobile--50-parent fonts-loaded']/div[@class='border-color-squid-ink     padding-left-xsmall padding-right-xsmall padding-top-zero padding-bottom-zero border-left-zero border-right-zero border-top-zero border-bottom-zero flex-container flex-align-items-stretch flex-align-content-flex-start amsg-2018 border-color-squid-ink design-Sell mobile--50 fonts-loaded']/div/text()").getall()
    for i in category_list:
        i = re.sub(r',', '', i)        
    referral_fee_list = selector.xpath("//div[@class='content']/div[@class='background-color-white border-color-cumulus     padding-left-zero padding-right-zero padding-top-small padding-bottom-small border-left-zero border-right-zero border-top-zero border-bottom-1px flex-container flex-align-items-stretch flex-align-content-flex-start flex-full-width amsg-2018 border-color-cumulus design-Sell mobile--50-parent fonts-loaded']/div[@style='width:41.666666666666664%']/div/text()").getall()
    for i in referral_fee_list:
        i = re.sub(r'\t', '', i)
        i = re.sub(r'•', '', i)
    min_ref_fee_list = selector.xpath("//div[@class='content']/div[@class='background-color-white border-color-cumulus     padding-left-zero padding-right-zero padding-top-small padding-bottom-small border-left-zero border-right-zero border-top-zero border-bottom-1px flex-container flex-align-items-stretch flex-align-content-flex-start flex-full-width amsg-2018 border-color-cumulus design-Sell mobile--50-parent fonts-loaded']/div[@style='width:25%']/div/text()").getall()
    zipped_list = zip(list(category_list), list(referral_fee_list), list(min_ref_fee_list))
    zipped_list = list(zipped_list)
    return zipped_list

