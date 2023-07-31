from pkg.plugin.models import *
from pkg.plugin.host import EventContext, PluginHost


# 注册插件
@register(name="Preprocessor", description="预处理prompt：嵌入当前时间、使用的模型等信息。", version="0.1.0", author="RockChinQ")
class PreprocessPlugin(Plugin):

    # 插件加载时触发
    # plugin_host (pkg.plugin.host.PluginHost) 提供了与主程序交互的一些方法，详细请查看其源码
    def __init__(self, plugin_host: PluginHost):
        pass

    @on(PromptPreProcessing)
    def _(self, event: EventContext, default_prompt: list, **kwargs):

        import config
        import datetime
        import re

        local_default_prompt = default_prompt.copy()

        mapping = {
            "model": config.completion_api_params['model'],
            # yyyy-mm-dd hh:mm:ss day
            "date_now": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %a"),
        }

        for round in local_default_prompt:
            # 把 round['content'] 中的 $key 替换为 mapping[key]
            for key in mapping:
                round['content'] = re.sub(r"\$"+key, mapping[key], round['content'])

        event.add_return(
            "default_prompt", local_default_prompt
        )

        # event.prevent_postorder()

    # 插件卸载时触发
    def __del__(self):
        pass
