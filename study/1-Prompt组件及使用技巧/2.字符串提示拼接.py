#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/4 20:15
@Author : zhx
@File   : 2.字符串提示拼接.py
"""
from langchain_core.prompts import PromptTemplate

prompt = (
        PromptTemplate.from_template("请讲一个关于{subject}的冷笑话")
        + "，让我开心一下" +
        "\n使用{language}语言"
)

print(prompt.invoke({"subject": "程序员", "language": "中文"}).to_string())
