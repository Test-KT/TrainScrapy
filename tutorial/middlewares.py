# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http import HtmlResponse
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from random import choice


class SeleniumMiddleware(object):

    def process_request(self, req, spider):
        click_url = 'http://weixin.sogou.com'
        if req.url() == click_url:
            driver = webdriver.PhantomJS()
            try:
                driver.get(req.url)
                driver.implicitly_wait(3)
                time.sleep(5)

                look_more = ".//div[@class='jzgd']/a"
                for n in range(4):
                    driver.find_element_by_css_selector(look_more).click()
                    time.sleep(5)
                ture_page = driver.page_source
                driver.close()
                return HtmlResponse(req.url,body=ture_page, encoding='utf-8', request=req)
            except:
                print("get new page faild")

        else:
            None
