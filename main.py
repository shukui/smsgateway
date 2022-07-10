#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : Shukui Zhang
# @File    : main.py
from twilio.rest import Client
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import configparser
from sms import Sms
import pyautogui
import pyperclip
import time

from typing import Optional

# read config.ini
cf = configparser.ConfigParser()
cf.read("config.ini")

# Your Account SID from twilio.com/console
twilio_account_sid = cf.get("twilio", "twilio_sid")
# Your Auth Token from twilio.com/console
twilio_auth_token = cf.get("twilio", "twilio_auth_token")

client = Client(twilio_account_sid, twilio_auth_token)

app = FastAPI()

@app.post("/sms")
async def send_sms(sms : Sms):
    print(sms.from_num)
    print(sms.to_num)
    print(sms.msg)
    send_sms(sms.from_num, sms.to_num, sms.msg)

@app.post("/wechat")
async def send_sms(sms : Sms):
    print(sms.from_num)
    print(sms.to_num)
    print(sms.msg)
    send_wechat(sms.to_num, sms.msg)

@app.get("/")
def read_root():
    return {"message" : "hello world"}

def send_sms(from_num = "+19853317467", to_num = "+4915905823956", msg=""):
    message = client.messages.create(
        # 这里中国的号码前面需要加86
        to=to_num,
        from_=from_num,
        body=msg)
    print(message.sid)

def send_wechat(to_num = "文件传输助手", msg="微信消息"):
    if to_num in ["文件传输助手","filehelper", "树魁", "shukui", "YuanQuan_1956", "ChangLe138999", "GabyGuo1985"]:
        wx_gui_send_msg(to_num, msg)

    else:
        pass

def wx_gui_send_msg(wxid, msg):
    # if wechat window exist
    if pyautogui.getWindowsWithTitle("微信") != None:
        # if current window is wechat
        if pyautogui.getActiveWindow() != None :
            if pyautogui.getActiveWindow().title != "微信":
                pyautogui.hotkey("ctrl", "alt", "w")
                time.sleep(0.5)
        # search in wechat
        pyautogui.hotkey("ctrl", "f")
        time.sleep(0.5)
        pyperclip.copy(wxid)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.5)
        pyautogui.press("enter")
        pyperclip.copy(msg)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        pyautogui.hotkey("ctrl", "alt", "w")

if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port = 8000)


