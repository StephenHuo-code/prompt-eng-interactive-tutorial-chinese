# -*- coding: utf-8 -*-
"""
火山方舟（Volcengine Ark）使用示例代码
使用官方 volcengine-python-sdk[ark] SDK
"""

import os
from model import get_completion

# 也可以直接使用火山方舟官方SDK
try:
    from volcenginesdkarkruntime import Ark
except ImportError:
    Ark = None
    print("请先安装火山方舟SDK: pip install volcengine-python-sdk[ark]")

def example_direct_ark_usage():
    """直接使用火山方舟官方SDK的示例"""
    print("=== 直接使用火山方舟官方SDK ===")
    
    if Ark is None:
        print("❌ 火山方舟SDK未安装")
        return
    
    # 从环境变量中获取您的API KEY
    api_key = os.getenv('ARK_API_KEY')
    if not api_key:
        print("❌ 请设置环境变量 ARK_API_KEY")
        return
    
    # 替换为您的模型ID（endpoint ID）
    model = "ep-20241226120407-8qk9p"  # 示例模型ID，请替换为实际的
    
    try:
        # 初始化Ark客户端
        client = Ark(api_key=api_key)
        
        # 创建一个对话请求
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "请将下面内容进行结构化处理：火山方舟是火山引擎推出的大模型服务平台，提供模型训练、推理、评测、精调等全方位功能与服务，并重点支撑大模型生态。 火山方舟通过稳定可靠的安全互信方案，保障模型提供方的模型安全与模型使用者的信息安全，加速大模型能力渗透到千行百业，助力模型提供方和使用者实现商业新增长。"},
            ],
        )
        
        print("✅ 火山方舟直接调用成功:")
        print(completion.choices[0].message.content)
        
    except Exception as e:
        print(f"❌ 火山方舟直接调用失败: {e}")

def example_unified_interface():
    """使用统一接口调用火山方舟的示例"""
    print("\n=== 使用统一接口调用火山方舟 ===")
    
    # 确保设置了环境变量
    if not os.getenv('ARK_API_KEY'):
        print("❌ 请设置环境变量 ARK_API_KEY")
        return
    
    prompts = [
        "请介绍一下量子计算的基本原理",
        "如何学习机器学习？给出具体的学习路径",
        "解释一下什么是大语言模型"
    ]
    
    # 可以指定不同的模型
    models = [
        "ep-20241226120407-8qk9p",  # 示例模型ID，请替换为实际的
        # 可以添加更多模型ID
    ]
    
    for i, prompt in enumerate(prompts):
        print(f"\n📝 问题 {i+1}: {prompt}")
        print("-" * 50)
        
        for model in models:
            try:
                response = get_completion(
                    prompt, 
                    provider="volcengine", 
                    model=model,
                    max_tokens=500,
                    temperature=0.7
                )
                print(f"🤖 火山方舟({model}): {response[:200]}...")
                
            except Exception as e:
                print(f"❌ 模型 {model} 调用失败: {e}")

def example_parameter_comparison():
    """参数对比示例"""
    print("\n=== 参数对比示例 ===")
    
    if not os.getenv('ARK_API_KEY'):
        print("❌ 请设置环境变量 ARK_API_KEY")
        return
    
    prompt = "请写一首关于春天的诗"
    temperatures = [0.1, 0.5, 0.9]
    
    for temp in temperatures:
        print(f"\n🌡️ 温度设置: {temp}")
        print("-" * 30)
        
        try:
            response = get_completion(
                prompt,
                provider="volcengine",
                model="ep-20241226120407-8qk9p",  # 请替换为实际模型ID
                temperature=temp,
                max_tokens=200
            )
            print(f"📝 生成结果: {response}")
            
        except Exception as e:
            print(f"❌ 温度 {temp} 调用失败: {e}")

def example_streaming_response():
    """流式响应示例（如果SDK支持）"""
    print("\n=== 流式响应示例 ===")
    
    if Ark is None:
        print("❌ 火山方舟SDK未安装")
        return
    
    api_key = os.getenv('ARK_API_KEY')
    if not api_key:
        print("❌ 请设置环境变量 ARK_API_KEY")
        return
    
    try:
        client = Ark(api_key=api_key)
        model = "ep-20241226120407-8qk9p"  # 请替换为实际模型ID
        
        print("🚀 开始流式生成...")
        
        # 注意：这是示例代码，具体的流式API可能略有不同
        # 请参考火山方舟官方文档获取准确的流式API用法
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": "请详细介绍人工智能的发展历程，包括重要的里程碑事件"}
            ],
            stream=True,  # 启用流式响应
            max_tokens=1000
        )
        
        print("📝 流式输出:")
        for chunk in completion:
            if hasattr(chunk, 'choices') and chunk.choices:
                content = chunk.choices[0].delta.content
                if content:
                    print(content, end='', flush=True)
        
        print("\n✅ 流式生成完成")
        
    except Exception as e:
        print(f"❌ 流式响应示例失败: {e}")
        print("💡 提示: 流式API的具体用法请参考火山方舟官方文档")

def main():
    """主函数"""
    print("🚀 火山方舟（Volcengine Ark）使用示例")
    print("=" * 60)
    print("💡 使用前请确保:")
    print("1. 已安装火山方舟SDK: pip install volcengine-python-sdk[ark]")
    print("2. 已设置环境变量 ARK_API_KEY")
    print("3. 已获取有效的模型ID（endpoint ID）")
    print("=" * 60)
    
    # 运行示例
    example_direct_ark_usage()
    example_unified_interface()
    example_parameter_comparison()
    example_streaming_response()
    
    print("\n✅ 所有示例运行完成！")
    print("\n📚 更多信息:")
    print("- 火山方舟官方文档: https://www.volcengine.com/docs/82379")
    print("- SDK文档: https://github.com/volcengine/volcengine-python-sdk")
    print("- 模型配置: 登录火山引擎控制台获取模型ID")

if __name__ == "__main__":
    main()