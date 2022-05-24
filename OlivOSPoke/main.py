# -*- encoding: utf-8 -*-
'''
   ____     __    _           ____    _____    ____            __
  / __ \   / /   (_) _   __  / __ \  / ___/   / __ \  ____    / /__  ___
 / / / /  / /   / / | | / / / / / /  \__ \   / /_/ / / __ \  / //_/ / _ \
/ /_/ /  / /   / /  | |/ / / /_/ /  ___/ /  / ____/ / /_/ / / ,<   /  __/
\____/  /_/   /_/   |___/  \____/  /____/  /_/      \____/ /_/|_|  \___/

@File      :   OlivOSPoke.main.py
@Author    :   Cute_CAT
@Contact   :   2971504919@qq.com
'''
import OlivOS
import OlivOSPoke
import os
import json
import re                               #正则表达式库，用于匹配指令
import random
import os
import uuid
import time
import requests

class Event(object):
    def init(plugin_event, Proc):
        if not os.path.exists("plugin/data/OlivOSPoke"):
            os.mkdir("plugin/data/OlivOSPoke")
        try:
            with open("plugin/data/OlivOSPoke/Data.json","r",encoding="utf-8") as file:
                json.load(file)
        except:
            data={'reply' : []}
            with open("plugin/data/OlivOSPoke/Data.json","w",encoding="utf-8") as file:
                json.dump(data, file,indent=4,ensure_ascii=False)

    def private_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        unity_reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        poke_reply(plugin_event, Proc)

    def save(plugin_event, Proc):
        pass

def deleteBlank(str):
    str_list = list(filter(None,str.split(" ")))
    return str_list

def unity_reply(plugin_event, Proc):
    command_list = deleteBlank(plugin_event.data.message)
    if command_list[0] == '戳一戳回复添加':
        try:
            with open("plugin/data/OlivOSPoke/Data.json","r",encoding="utf-8") as file:
                reply_text = json.load(file)
            with open("plugin/data/OlivOSPoke/Data.json","w",encoding="utf-8") as file:
                reply_text['reply'].append(command_list[1])
                reply_text['reply'] = list(set(reply_text['reply'])) #去重
                json.dump(reply_text, file, indent=4, ensure_ascii=False)
            plugin_event.reply('回复已添加')
        except Exception as e:
            print(e)
            plugin_event.reply('添加失败了')
    elif command_list[0] == '戳一戳回复删除':
        try:
            with open("plugin/data/OlivOSPoke/Data.json", "r", encoding="utf-8") as file:
                reply_text = json.load(file)
            with open("plugin/data/OlivOSPoke/Data.json", "w", encoding="utf-8") as file:
                reply_text['reply'] = list(set(reply_text['reply']))  # 去重
                reply_text['reply'].remove(command_list[1])
                json.dump(reply_text, file, indent=4, ensure_ascii=False)
            plugin_event.reply('回复已删除')
        except Exception as e:
            print(e)
            plugin_event.reply('删除失败了\n#可能不存在相关词条或文件读取失败')

def poke_reply(plugin_event, Proc):
    if plugin_event.data.target_id == plugin_event.base_info['self_id']:
        with open("plugin/data/OlivOSPoke/Data.json", "r", encoding="utf-8") as file:
            reply_text = json.load(file)
            if reply_text['reply'] == []:
                pass
            else:
                reply_text['reply'] = list(set(reply_text['reply']))  # 去重
                plugin_event.reply(random.choice(reply_text['reply']))
    elif plugin_event.data.group_id == -1:
        with open("plugin/data/OlivOSPoke/Data.json", "r", encoding="utf-8") as file:
            reply_text = json.load(file)
            if reply_text['reply'] == []:
                pass
            else:
                reply_text['reply'] = list(set(reply_text['reply']))  # 去重
                plugin_event.reply(random.choice(reply_text['reply']))
