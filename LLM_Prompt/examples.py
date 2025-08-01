# -*- coding: utf-8 -*-
"""
多种大模型调用示例代码
支持的模型：Anthropic Claude、OpenAI、火山方舟豆包、DeepSeek
"""

import os
from model import get_completion

# =============================================================================
# 1. 基本调用示例
# =============================================================================

def example_basic_calls():
    """基本调用示例"""
    print("=== 基本调用示例 ===")
    
    # 设置环境变量（可以在环境中设置，这里仅作演示）
    # os.environ["ANTHROPIC_API_KEY"] = "你的API密钥"
    # os.environ["OPENAI_API_KEY"] = "你的API密钥"
    # os.environ["ARK_API_KEY"] = "你的火山方舟API密钥"
    # os.environ["DEEPSEEK_API_KEY"] = "你的API密钥"
    
    prompt = "请用中文简要介绍人工智能的发展历程"
    
    # Anthropic Claude
    try:
        response = get_completion(prompt, provider="anthropic")
        print(f"Claude 回复: {response[:100]}...")
    except Exception as e:
        print(f"Claude 调用失败: {e}")
    
    # OpenAI
    try:
        response = get_completion(prompt, provider="openai")
        print(f"OpenAI 回复: {response[:100]}...")
    except Exception as e:
        print(f"OpenAI 调用失败: {e}")
    
    # 火山方舟豆包
    try:
        response = get_completion(prompt, provider="volcengine")
        print(f"火山方舟豆包 回复: {response[:100]}...")
    except Exception as e:
        print(f"火山方舟豆包 调用失败: {e}")
    
    # DeepSeek
    try:
        response = get_completion(prompt, provider="deepseek")
        print(f"DeepSeek 回复: {response[:100]}...")
    except Exception as e:
        print(f"DeepSeek 调用失败: {e}")

# =============================================================================
# 2. 指定模型调用示例
# =============================================================================

def example_specific_models():
    """指定特定模型调用示例"""
    print("\n=== 指定模型调用示例 ===")
    
    prompt = "写一首关于春天的短诗"
    
    # Claude 不同模型
    models_claude = ["claude-3-haiku-20240307", "claude-3-sonnet-20240229"]
    for model in models_claude:
        try:
            response = get_completion(prompt, provider="anthropic", model=model)
            print(f"Claude {model}: {response[:50]}...")
        except Exception as e:
            print(f"Claude {model} 调用失败: {e}")
    
    # OpenAI 不同模型
    models_openai = ["gpt-4o", "gpt-3.5-turbo"]
    for model in models_openai:
        try:
            response = get_completion(prompt, provider="openai", model=model)
            print(f"OpenAI {model}: {response[:50]}...")
        except Exception as e:
            print(f"OpenAI {model} 调用失败: {e}")
    
    
    # DeepSeek 不同模型
    models_deepseek = ["deepseek-chat", "deepseek-reasoner"]
    for model in models_deepseek:
        try:
            response = get_completion(prompt, provider="deepseek", model=model)
            print(f"DeepSeek {model}: {response[:50]}...")
        except Exception as e:
            print(f"DeepSeek {model} 调用失败: {e}")

# =============================================================================
# 3. 参数调整示例
# =============================================================================

def example_parameter_tuning():
    """参数调整示例"""
    print("\n=== 参数调整示例 ===")
    
    prompt = "请生成一个创意故事开头"
    
    # 不同温度设置
    temperatures = [0.0, 0.5, 1.0]
    for temp in temperatures:
        try:
            response = get_completion(
                prompt, 
                provider="deepseek", 
                temperature=temp,
                max_tokens=100
            )
            print(f"温度 {temp}: {response[:80]}...")
        except Exception as e:
            print(f"温度 {temp} 调用失败: {e}")

# =============================================================================
# 4. 错误处理示例
# =============================================================================

def example_error_handling():
    """错误处理示例"""
    print("\n=== 错误处理示例 ===")
    
    def safe_call(prompt, provider, model=None):
        """安全调用函数"""
        try:
            response = get_completion(prompt, provider=provider, model=model)
            print(f"✅ {provider} 调用成功: {response[:50]}...")
            return response
        except ValueError as e:
            print(f"❌ {provider} 参数错误: {e}")
        except ImportError as e:
            print(f"❌ {provider} 依赖错误: {e}")
        except RuntimeError as e:
            print(f"❌ {provider} API调用失败: {e}")
        except Exception as e:
            print(f"❌ {provider} 未知错误: {e}")
        return None
    
    prompt = "你好，请自我介绍"
    
    # 测试各个提供商
    providers = ["anthropic", "openai", "volcengine", "deepseek"]
    for provider in providers:
        safe_call(prompt, provider)

# =============================================================================
# 5. 批量比较示例
# =============================================================================

def example_batch_comparison():
    """批量比较不同模型的回答"""
    print("\n=== 批量比较示例 ===")
    
    questions = [
        "什么是量子计算？",
        "如何学习编程？",
        "介绍一下机器学习"
    ]
    
    providers = [
        ("deepseek", "deepseek-chat"),
        ("openai", "gpt-4o"),
        ("volcengine", "ep-20241226120407-8qk9p")
    ]
    
    for question in questions:
        print(f"\n📝 问题: {question}")
        print("-" * 50)
        
        for provider, model in providers:
            try:
                response = get_completion(
                    question, 
                    provider=provider, 
                    model=model,
                    max_tokens=150
                )
                print(f"🤖 {provider}({model}): {response[:100]}...")
            except Exception as e:
                print(f"❌ {provider}({model}) 失败: {e}")

# =============================================================================
# 6. 配置管理示例
# =============================================================================

class ModelConfig:
    """模型配置管理类"""
    
    def __init__(self):
        self.configs = {
            "创意写作": {
                "provider": "deepseek",
                "model": "deepseek-chat",
                "temperature": 0.8,
                "max_tokens": 500
            },
            "技术问答": {
                "provider": "openai",
                "model": "gpt-4o",
                "temperature": 0.2,
                "max_tokens": 300
            },
            "翻译任务": {
                "provider": "volcengine",
                "model": "ep-20241226120407-8qk9p",
                "temperature": 0.1,
                "max_tokens": 200
            }
        }
    
    def get_response(self, task_type, prompt):
        """根据任务类型获取响应"""
        if task_type not in self.configs:
            raise ValueError(f"不支持的任务类型: {task_type}")
        
        config = self.configs[task_type]
        return get_completion(prompt, **config)

def example_config_management():
    """配置管理示例"""
    print("\n=== 配置管理示例 ===")
    
    config_manager = ModelConfig()
    
    tasks = [
        ("创意写作", "写一个关于机器人的科幻故事开头"),
        ("技术问答", "Python中的装饰器是什么？"),
        ("翻译任务", "Please translate 'Hello World' to Chinese")
    ]
    
    for task_type, prompt in tasks:
        try:
            response = config_manager.get_response(task_type, prompt)
            print(f"📋 {task_type}: {response[:80]}...")
        except Exception as e:
            print(f"❌ {task_type} 失败: {e}")

# =============================================================================
# 主函数
# =============================================================================

if __name__ == "__main__":
    print("🚀 多种大模型调用示例")
    print("=" * 60)
    
    # 运行所有示例
    example_basic_calls()
    example_specific_models()
    example_parameter_tuning()
    example_error_handling()
    example_batch_comparison()
    example_config_management()
    
    print("\n✅ 所有示例运行完成！")
    print("\n💡 使用提示:")
    print("1. 需要先设置相应的API密钥环境变量:")
    print("   - ANTHROPIC_API_KEY (Claude)")
    print("   - OPENAI_API_KEY (OpenAI)")
    print("   - ARK_API_KEY (火山方舟)")
    print("   - DEEPSEEK_API_KEY (DeepSeek)")
    print("2. 火山方舟需要使用endpoint ID作为model参数")
    print("3. 火山方舟需要安装: pip install volcengine-python-sdk[ark]")
    print("4. 各个模型的具体名称请参考官方文档")
    print("5. 根据需要调整temperature和max_tokens参数")