#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 14:21
@Author : zhx
@File   : LCEL表达式简化版本.py
"""
import os

import dotenv
from langchain_community.chat_models import MoonshotChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

prompt = ChatPromptTemplate.from_template("{query}")
llm = MoonshotChat(
    model="kimi-k2-turbo-preview",
    api_key=os.getenv("MOONSHOT_API_KEY"),
)
parser = StrOutputParser()

# 3.编排链
chain = prompt | llm | parser

# 4.执行链并获取结果
print(chain.invoke({"query": "你好，你是?"}))
