import os
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


class TranslationService:
    def __init__(self, api_key, model_name="qwen-max", model_provider="openai", base_url=None):
        """
        初始化翻译服务类。

        :param api_key: OpenAI API 密钥
        :param model_name: 使用的模型名称，默认为 "qwen-max"
        :param model_provider: 模型提供者，默认为 "openai"
        :param base_url: 自定义的 API 基础 URL
        """
        self.api_key = api_key
        self.model_name = model_name
        self.model_provider = model_provider
        self.base_url = base_url or "https://dashscope.aliyuncs.com/compatible-mode/v1"

        # 设置环境变量
        os.environ["OPENAI_API_KEY"] = self.api_key

        # 初始化模型和解析器
        self.model = init_chat_model(
            self.model_name,
            model_provider=self.model_provider,
            base_url=self.base_url
        )
        self.parser = StrOutputParser()

        # 定义系统提示模板
        self.system_content = "你需要将我发送给你的英文翻译成中文"
        self.prompt_template = ChatPromptTemplate.from_messages(
            [("system", self.system_content), ("user", "{text}")]
        )

        # 构建链式调用
        self.chain = self.prompt_template | self.model | self.parser

    def translate(self, text):
        """
        翻译方法，将输入的英文文本翻译成中文。

        :param text: 要翻译的英文文本
        :return: 翻译后的中文文本
        """
        if not text:
            raise ValueError("输入的文本不能为空")

        response = self.chain.invoke({"text": text})
        return response


# 使用示例
if __name__ == "__main__":
    # 替换为你的 API 密钥
    api_key = "sk-0510de2c979d43ec8c7997b55cb00edb"

    # 初始化翻译服务
    translator = TranslationService(api_key)

    # 要翻译的文本
    english_text = "hello"

    # 调用翻译方法
    chinese_text = translator.translate(english_text)
    print(chinese_text)