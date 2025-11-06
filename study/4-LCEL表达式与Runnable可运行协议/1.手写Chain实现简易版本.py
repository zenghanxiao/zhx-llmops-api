#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 14:20
@Author : zhx
@File   : 1.手写Chain实现简易版本.py
"""
import os
from typing import Any

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


class Chain:
    steps: list = []

    def __init__(self, setps: list):
        self.steps = setps

    def invoke(self, input: Any) -> Any:
        for step in self.steps:
            input = step(input)
            print("步骤:", step)
            print("输出:", input)
            print("===============")
        return input


# 3.编排链
chain = Chain([prompt, llm, parser])

# 4.执行链并获取结果
print(chain.invoke({"query": "你好，你是?"}))
