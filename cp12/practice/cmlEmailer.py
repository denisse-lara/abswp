#!/usr/bin/python
# cmlEmailer - Sends an email using the command line
# Receives the sender credentials, the recepient email,
# and subject with content for the email.

import sys, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

if len(sys.argv) < 6:
    print("Usage: cmlEmailer <sender_email> <sender_password>" + \
    "<recepient_email> <subject> <content>")
    sys.exit()

# makes sure it only unpacks the 6 required arguments
file, sender, password, recepient, subject, content = sys.argv[:6]

browser = webdriver.Firefox()
browser.get('http://gmail.com')

time.sleep(1)

eInput = browser.find_element(by=By.ID, value='identifierId')
eInput.send_keys(sender)
eInput.send_keys(Keys.ENTER)

time.sleep(4)

pInput = browser.find_element(
    by=By.CSS_SELECTOR,
    value='input[type="password"]'
)
pInput.send_keys(password)
pInput.send_keys(Keys.ENTER)

time.sleep(10)

compose = browser.find_element(by=By.CSS_SELECTOR, value='.T-I.T-I-KE.L3')
compose.click()

time.sleep(3)

to = browser.find_element(by=By.CSS_SELECTOR, value='textarea[name="to"]')
to.send_keys(recepient)

time.sleep(3)

sInput = browser.find_element(
    by=By.CSS_SELECTOR,
    value='input[name="subjectbox"]'
)
sInput.send_keys(subject)

time.sleep(3)

cText = browser.find_element(
    by=By.CSS_SELECTOR,
    value='div[role="textbox"]'
)
cText.send_keys(content)

time.sleep(5)

send = browser.find_element(
    by=By.CSS_SELECTOR,
    value='div[data-tooltip="Send ‪(Ctrl-Enter)‬"]'
)
send.click()

print('Email sent.')
