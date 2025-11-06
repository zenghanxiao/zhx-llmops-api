#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 09:28
@Author : zhx
@File   : 1.LLM与ChatModel使用技巧.py
"""
import os
from datetime import datetime

import dotenv
from langchain_community.chat_models.moonshot import MoonshotChat
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

# 修复：使用正确的参数初始化 MoonshotChat
llm = MoonshotChat(
    model="kimi-k2-turbo-preview",
    api_key=os.getenv("MOONSHOT_API_KEY"),
    # client=os.getenv("MOONSHOT_CLIENT"),
)

# 1.编排prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是OpenAI开发的聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}"),
]).partial(now=datetime.now())

response = llm.invoke(prompt.invoke({"query": "现在是几点，请讲一个程序员的冷笑话"}))

print(response.type)
print(response.content)
print(response.response_metadata)
