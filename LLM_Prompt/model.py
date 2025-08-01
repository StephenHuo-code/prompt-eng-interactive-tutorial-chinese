import os
import anthropic
import openai
from http import HTTPStatus
from volcenginesdkarkruntime import Ark  # 火山方舟官方SDK

DEFAULT_PROVIDER = "anthropic"
DEFAULT_ANTHROPIC_MODEL = "claude-3-haiku-20240307"
DEFAULT_OPENAI_MODEL = "gpt-4o"
DEFAULT_VOLCENGINE_MODEL = "doubao-seed-1.6"  # 火山方舟豆包模型
DEFAULT_DEEPSEEK_MODEL = "deepseek-chat"  # DeepSeek模型

def _unified_llm_call(prompt: str, provider: str, model: str, max_tokens: int, temperature: float):
    """
    统一处理openai、volcengine、deepseek的调用逻辑
    """
    if provider == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("请设置环境变量 OPENAI_API_KEY")
        if model is None:
            model = DEFAULT_OPENAI_MODEL
        client = openai.OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    elif provider == "volcengine":
        api_key = os.getenv("ARK_API_KEY")
        if not api_key:
            raise ValueError("请设置环境变量 ARK_API_KEY")
        if Ark is None:
            raise ImportError("请先安装火山方舟SDK: pip install volcengine-python-sdk[ark]")
        if model is None:
            model = DEFAULT_VOLCENGINE_MODEL
        client = Ark(base_url="https://ark.cn-beijing.volces.com/api/v3",api_key=api_key)
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        return completion.choices[0].message.content

    elif provider == "deepseek":
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("请设置环境变量 DEEPSEEK_API_KEY")
        if model is None:
            model = DEFAULT_DEEPSEEK_MODEL
        client = openai.OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com"
        )
        response = client.chat.completions.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content

    else:
        raise ValueError("不支持的provider，请选择'openai'、'volcengine'或'deepseek'")

def get_completion(prompt: str, provider: str = DEFAULT_PROVIDER, model: str = None, max_tokens: int = 2000, temperature: float = 0.0):
    """
    通用LLM调用函数，支持anthropic（Claude）、openai、火山方舟豆包、deepseek

    Args:
        prompt: 发送给模型的提示文本
        provider: 模型提供商，可选值为 'anthropic', 'openai', 'volcengine'(火山方舟), 'deepseek'
        model: 模型名称，如果为None则使用默认模型
        max_tokens: 生成的最大token数量
        temperature: 采样温度，控制输出的随机性

    Returns:
        str: 模型生成的响应文本
    """
    provider = provider.lower()
    if provider == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("请设置环境变量 ANTHROPIC_API_KEY")
        if model is None:
            model = DEFAULT_ANTHROPIC_MODEL
        client = anthropic.Anthropic(api_key=api_key)
        # anthropic官方SDK没有chat.completions的调用方式，只有messages.create
        message = client.messages.create(
            model=model,
            max_tokens=max_tokens,
            temperature=temperature,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return message.content[0].text
    elif provider in ("openai", "volcengine", "deepseek"):
        return _unified_llm_call(prompt, provider, model, max_tokens, temperature)
    else:
        raise ValueError("不支持的provider，请选择'anthropic'、'openai'、'volcengine'或'deepseek'")