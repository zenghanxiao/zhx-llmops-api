#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 10:10
@Author : zhx
@File   : 3.Model流式输出.py
"""
import os
from datetime import datetime

import dotenv
from langchain_community.chat_models import MoonshotChat
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

# 1.编排Prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是聊天机器人，请回答用户的问题，现在的时间是{now}"),
    ("human", "{query}")
]).partial(now=datetime.now().strftime("%Y/%m/%d %H:%M:%S"))

# 2.创建大语言模型
llm = MoonshotChat(
    model="kimi-k2-turbo-preview",
    api_key=os.getenv("MOONSHOT_API_KEY"),
)

response = llm.stream(prompt.invoke({"query": "你能简单介绍下LLM和LLMOps吗?"}))

for chunk in response:
    print(chunk.content, flush=True, end="")
