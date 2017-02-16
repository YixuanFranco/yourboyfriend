# YBaaS (Your Boyfriend as a Service)

## Overview

该文件夹下是「蓝朋友」的 go 语言版本初期后端实现。

目前的想法是先做一个泛化 (client-agnostic) 的聊天机器人后端，会定期从不同数据源抓取内容（甜言蜜语，笑话，语言风格的训练语料等），开发统一的接口并逐渐实现各聊天工具比如微信，telegram，fb messenger 甚至 slack 等等的客户端（甚至 mobile app）。

选择 chat bot 入手是因为它相对比较简单，并且在后期可以 cover 到更多的功能（比如目前 fb messenger 支持的聊天购物、订花、订餐等），扩展性不错。

而之后一旦涉及到人工智能我们可能需要另一个 service 来做 machine learning 相关的工作。Microservices 应该是 YBaaS 会选择的架构。

聊天机器人完善之后可以向智能家居方向努力。

Let's build it.

PS: 好好好 作为死程我承认我很闲...

## Architecture

Microservices.

*bf* is the main backend service for YBaaS with RESTful API. *bf-telegram* is the [telegram](https://telegram.org/) client (also as a service).

Once *bf* is done, feel free to add other services (potentially in other languages) talking to it for variosu functionalities.   

## Features

(TODO section.)

1. 甜言蜜语
2. 睡前小故事
3. 订饭
4. 对话 (may need to investigate other existing APIs)