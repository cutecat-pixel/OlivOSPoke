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
import re                             
import random
import os
import uuid
import time

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
        with open("plugin/data/OlivOSPoke/Data.json","r",encoding="utf-8") as file:
            reply_text = json.load(file)
        with open("plugin/data/OlivOSPoke/Data.json","w",encoding="utf-8") as file:
            reply_text['reply'].append(command_list[1])
            json.dump(reply_text, file, indent=4, ensure_ascii=False)

def poke_reply(plugin_event, Proc):
    if plugin_event.data.target_id == plugin_event.base_info['self_id']:
         plugin_event.reply(random.choice(reply_text['reply']))
    elif plugin_event.data.group_id == -1:
         plugin_event.reply(random.choice(reply_text['reply']))
