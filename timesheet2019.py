#!/usr/bin/env python
# coding: utf-8

# ## Timesheet (remember to check case)
# * This is a timesheet script
# 

# In[ ]:


# run the script below
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pandas as pd
import time
import datetime as dt
import xlrd


driver = webdriver.Chrome()
driver.get("https://secure.casefox.com/Login")
driver.find_element_by_id("Email").send_keys("your email")
driver.find_element_by_id("Password").send_keys("your password")
driver.find_element_by_id("submit").click()

# read timesheet
timesheet = '~/Desktop/Timesheet.xlsx'
# load timesheet
df = pd.read_excel(timesheet)
# select column name
df1 = df[['Client Name', 'Case Name',
          'Date', 'Work Performed', 'Hours', 'StartTime']]
df1.head()

rowcount = len(df1.index)

for x in range(0, rowcount):
    case_name = df1.loc[x, 'Case/Matter Name']
    case_date = df1.loc[x, 'Date'].strftime("%m/%d/%Y")
    case_time = df1.loc[x, 'StartTime'].strftime("%I:%M")
    case_ampm = df1.loc[x, 'StartTime'].strftime("%p")
    case_hour = str(df1.loc[x, 'Hours'])
    case_note = df1.loc[x, 'Work Performed']

    driver.find_element_by_partial_link_text(case_name).click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "/html/body/outputcache/div[6]/div[3]/div/div[7]/div[2]/div[3]/div/div[2]/div/div/a[2]").click()
    time.sleep(2)
    driver.find_element_by_id("OnDate").clear()
    driver.find_element_by_id("OnDate").send_keys(case_date)
    time.sleep(1)
    driver.find_element_by_id("OnTime").clear()
    driver.find_element_by_id("OnTime").send_keys(case_time)
    time.sleep(1)
    ampm = Select(driver.find_element_by_id("AmPmValue"))
    ampm.select_by_value(case_ampm)

    time.sleep(1)
    driver.find_element_by_id("ForTHours").send_keys(case_hour)

    time.sleep(1)
    driver.find_element_by_id("Note").send_keys(case_note)

    time.sleep(1)
    driver.find_element_by_id("btnSaveNote").click()
    time.sleep(3)

    if x == rowcount:
        break

