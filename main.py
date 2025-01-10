from pkg.plugin.context import register, handler, llm_func, BasePlugin, APIHost, EventContext
from pkg.plugin.events import *  # 导入事件类


# 注册插件
@register(name="Preprocessor", description="预处理prompt：嵌入当前时间、使用的模型等信息。", version="0.1.0", author="RockChinQ")
class PreprocessPlugin(BasePlugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: APIHost):
        pass

    @handler(PromptPreProcessing)
    async def _(self, ctx: EventContext):

        import datetime
        import re

        local_default_prompt = ctx.event.default_prompt.copy()

        mapping = {
            "model": ctx.event.query.use_model.name,
            # yyyy-mm-dd hh:mm:ss day
            "date_now": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %a"),
        }

        for round in local_default_prompt:
            # 把 round['content'] 中的 $key 替换为 mapping[key]
            for key in mapping:
                round.content = re.sub(r"\$"+key, mapping[key], round.content)

        ctx.add_return(
            "default_prompt", local_default_prompt
        )

        # event.prevent_postorder()

    # 插件卸载时触发
    def __del__(self):
        pass
