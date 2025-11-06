#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/5 16:30
@Author : zhx
@File   : 1.回调功能使用技巧.py
"""
import os
import time
from typing import Any
from uuid import UUID

import dotenv
from langchain_community.chat_models import MoonshotChat
from langchain_core.callbacks import StdOutCallbackHandler, BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.outputs import LLMResult
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableConfig

dotenv.load_dotenv()


class LLMOpsCallbackHandler(BaseCallbackHandler):
    """自定义LLMOps回调处理器"""
    start_at: float = 0

    def on_chat_model_start(
            self,
            serialized: dict[str, Any],
            messages: list[list[BaseMessage]],
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            tags: list[str] | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> Any:
        print("聊天模型开始执行了")
        print("serialized:", serialized)
        print("messages:", messages)
        self.start_at = time.time()

    def on_llm_end(
            self,
            response: LLMResult,
            *,
            run_id: UUID,
            parent_run_id: UUID | None = None,
            **kwargs: Any,
    ) -> Any:
        end_at: float = time.time()
        print("完整输出:", response)
        print("程序消耗:", end_at - self.start_at)


# 1.编排prompt
prompt = ChatPromptTemplate.from_template("{query}")

# 2.创建大语言模型
llm = MoonshotChat(
    model="kimi-k2-turbo-preview",
    api_key=os.getenv("MOONSHOT_API_KEY"),
)

# 3.创建输出解析器
parser = StrOutputParser()

# 4.编排链
chain = RunnablePassthrough(query=lambda x: x) | prompt | llm | parser

# 5.调用链并执行
resp = chain.stream(
    "你好，你是？",
    config=RunnableConfig(callbacks=[StdOutCallbackHandler(), LLMOpsCallbackHandler()])
)

for chunk in resp:
    pass
