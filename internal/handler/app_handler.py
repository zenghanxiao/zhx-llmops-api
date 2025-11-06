#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time   : 2025/11/1 14:51
@Author : zhx
@File   : app_handler.py
"""
import os
import uuid
from dataclasses import dataclass

from injector import inject
from langchain_community.chat_models import MoonshotChat
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import validate_error_json, success_json, success_message


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的APP记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已经成功创建，id为{app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是{app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id是{app.id}")

    def debug(self, app_id: uuid.UUID):
        """聊天接口"""
        # 1.提取从接口中获取的输入，POST
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        # query = request.json.get("query")

        # 2.构建组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = MoonshotChat(
            model="kimi-k2-turbo-preview",
            api_key=os.getenv("MOONSHOT_API_KEY"),
        )
        parser = StrOutputParser()

        # 3.构建链
        chain = prompt | llm | parser

        # 4.调用链得到结果
        content = chain.invoke({"query": req.query.data})

        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
        # return {"ping": "pong"}
