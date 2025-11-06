#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/4 20:23
@Author : zhx
@File   : 4.复用提示模板.py
"""
from langchain_core.prompts import PromptTemplate


# PipePromptTemplate已被废弃

# 方法1: 使用字符串格式化直接组合
def create_prompt(person, example_q, example_a, input_text):
    instruction = f"你正在模拟{person}"
    example = f"下面是一个交互例子:\n\nQ: {example_q}\nA: {example_a}"
    start = f"现在，你是一个真实的人，请回答用户的问题:\n\nQ: {input_text}\nA:"

    return f"{instruction}\n\n{example}\n\n{start}"


# 方法2: 使用 PromptTemplate 组合
def create_prompt_with_templates(person, example_q, example_a, input_text):
    instruction_template = PromptTemplate.from_template("你正在模拟{person}")
    example_template = PromptTemplate.from_template("""下面是一个交互例子:

Q: {example_q}
A: {example_a}""")
    start_template = PromptTemplate.from_template("""现在，你是一个真实的人，请回答用户的问题:

Q: {input}
A:""")

    instruction = instruction_template.invoke({"person": person})
    example = example_template.invoke({"example_q": example_q, "example_a": example_a})
    start = start_template.invoke({"input": input_text})

    return f"{instruction.to_string()}\n\n{example.to_string()}\n\n{start.to_string()}"


# 测试方法1
print("方法1 - 直接字符串组合:")
print(create_prompt(
    person="雷军",
    example_q="你最喜欢的汽车是什么?",
    example_a="小米su7",
    input_text="你最喜欢的手机是什么?"
))

print("\n" + "=" * 50 + "\n")

# 测试方法2
print("方法2 - 使用 PromptTemplate 组合:")
print(create_prompt_with_templates(
    person="雷军",
    example_q="你最喜欢的汽车是什么?",
    example_a="小米su7",
    input_text="你最喜欢的手机是什么?"
))
