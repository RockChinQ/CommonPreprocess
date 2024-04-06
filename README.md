# Preprocessor

[QChatGPT项目](https://github.com/RockChinQ/QChatGPT)的插件，在请求接口回复前对`情景预设`进行预处理。

> 需要主程序版本高于`v3.1`

## 安装

完成主程序配置之后，使用管理员QQ私聊机器人发送以下命令：

```
!plugin get https://github.com/RockChinQ/CommonPreprocess
```

重启程序即可加载。

## 使用

若您的情景预设的内容中包含以下的key，如`$model` `$date_now`，插件将会自动替换成真实值

- `$model`: 当前使用的模型名称
- `$date_now`: 当前时间，如: `2023-07-31 17:19:13 Mon`