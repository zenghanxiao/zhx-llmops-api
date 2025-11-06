#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/4 20:18
@Author : zhx
@File   : 3.消息提示模板拼接.py
"""
from langchain_core.prompts import ChatPromptTemplate

system_chart_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请根据用户的提问进行回复，我叫{username}")
])

human_chat_prompt = ChatPromptTemplate.from_messages([
    ("human", "{query}")
])

chat_prompt = system_chart_prompt + human_chat_prompt

print(chat_prompt.invoke({
    "username": "慕小课",
    "query": "你好，你是？"
}))
