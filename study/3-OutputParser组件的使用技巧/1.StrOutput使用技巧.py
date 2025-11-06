#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 10:49
@Author : zhx
@File   : 1.StrOutput使用技巧.py
"""
import os

import dotenv
from langchain_community.chat_models import MoonshotChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

dotenv.load_dotenv()

# 2.构建一个提示模板
prompt = ChatPromptTemplate.from_template("{query}")

# 3.创建大语言模型
model = MoonshotChat(
    model="kimi-k2-turbo-preview",
    api_key=os.getenv("MOONSHOT_API_KEY"),
)

# 3.创建字符串输出解析器
parser = StrOutputParser()

# 4.调用大语言模型生成结果并解析
content = parser.invoke(model.invoke(prompt.invoke({"query": "你好，你是?"})))

print(content)
