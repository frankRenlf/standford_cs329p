# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : standford_cs329p 
    @Product : PyCharm
    @createTime : 2023/9/1 14:21 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

from selenium import webdriver

if __name__ == "__main__":
    chrome_options = webdriver.Chromeoptions()
    chrome_options.headless = True

    chrome = webdriver.Chrome(chrome_options=chrome_options)

    page = chrome.get(url)
