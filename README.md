# Welcome to Anthropic's Prompt Engineering Interactive Tutorial
# 欢迎来到 Anthropic 提示工程交互式教程

---

## 🌐 Language Selection / 语言选择

**Choose your language / 选择您的语言:**
- [English Version](#english-version) | [中文版本](#中文版本)

---

## English Version

### Course introduction and goals

This course is intended to provide you with a comprehensive step-by-step understanding of how to engineer optimal prompts within Claude.

**After completing this course, you will be able to**:
- Master the basic structure of a good prompt 
- Recognize common failure modes and learn the '80/20' techniques to address them
- Understand Claude's strengths and weaknesses
- Build strong prompts from scratch for common use cases

### Course structure and content

This course is structured to allow you many chances to practice writing and troubleshooting prompts yourself. The course is broken up into **9 chapters with accompanying exercises**, as well as an appendix of even more advanced methods. It is intended for you to **work through the course in chapter order**. 

**Each lesson has an "Example Playground" area** at the bottom where you are free to experiment with the examples in the lesson and see for yourself how changing prompts can change Claude's responses. There is also an [answer key](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing).

Note: This tutorial uses our smallest, fastest, and cheapest model, Claude 3 Haiku. Anthropic has [two other models](https://docs.anthropic.com/claude/docs/models-overview), Claude 3 Sonnet and Claude 3 Opus, which are more intelligent than Haiku, with Opus being the most intelligent.

*This tutorial also exists on [Google Sheets using Anthropic's Claude for Sheets extension](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing). We recommend using that version as it is more user friendly.*

When you are ready to begin, go to `01_Basic Prompt Structure` to proceed.

### Table of Contents

Each chapter consists of a lesson and a set of exercises.

#### Beginner
- **Chapter 1:** Basic Prompt Structure
- **Chapter 2:** Being Clear and Direct  
- **Chapter 3:** Assigning Roles

#### Intermediate 
- **Chapter 4:** Separating Data from Instructions
- **Chapter 5:** Formatting Output & Speaking for Claude
- **Chapter 6:** Precognition (Thinking Step by Step)
- **Chapter 7:** Using Examples

#### Advanced
- **Chapter 8:** Avoiding Hallucinations
- **Chapter 9:** Building Complex Prompts (Industry Use Cases)
  - Complex Prompts from Scratch - Chatbot
  - Complex Prompts for Legal Services
  - **Exercise:** Complex Prompts for Financial Services
  - **Exercise:** Complex Prompts for Coding
  - Congratulations & Next Steps

- **Appendix:** Beyond Standard Prompting
  - Chaining Prompts
  - Tool Use
  - Search & Retrieval

---

## 中文版本

### 课程介绍和目标

本课程旨在为您提供全面的逐步指导，教您如何在 Claude 中设计最优的提示词。

**完成本课程后，您将能够**：
- 掌握优秀提示词的基本结构
- 识别常见失败模式并学习解决这些问题的"80/20"技巧
- 了解 Claude 的优势和局限性
- 从零开始为常见用例构建强大的提示词

### 课程结构和内容

本课程的结构设计让您有很多机会亲自练习编写和调试提示词。课程分为 **9个章节和配套练习**，以及一个包含更高级方法的附录。建议您**按章节顺序学习课程**。

**每节课底部都有一个"示例练习区"**，您可以自由地对课程中的示例进行实验，亲自体验更改提示词如何改变 Claude 的响应。这里还有一个[答案键](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing)。

注意：本教程使用我们最小、最快、最便宜的模型 Claude 3 Haiku。Anthropic 还有[其他两个模型](https://docs.anthropic.com/claude/docs/models-overview)：Claude 3 Sonnet 和 Claude 3 Opus，它们比 Haiku 更智能，其中 Opus 是最智能的。

*本教程也有[使用 Anthropic Claude for Sheets 扩展的 Google Sheets 版本](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)。我们推荐使用该版本，因为它更用户友好。*

当您准备开始时，请转到 `01_Basic Prompt Structure` 继续学习。

### 目录

每个章节都包含一堂课和一套练习。

#### 初级
- **第1章：** 基本提示词结构
- **第2章：** 清晰直接的表达
- **第3章：** 角色分配

#### 中级
- **第4章：** 将数据与指令分离
- **第5章：** 格式化输出和为 Claude 代言
- **第6章：** 预认知（逐步思考）
- **第7章：** 使用示例

#### 高级
- **第8章：** 避免幻觉
- **第9章：** 构建复杂提示词（行业用例）
  - 从零开始构建复杂提示词 - 聊天机器人
  - 法律服务的复杂提示词
  - **练习：** 金融服务的复杂提示词
  - **练习：** 编程的复杂提示词
  - 恭喜您完成课程 & 下一步

- **附录：** 超越标准提示
  - 链式提示
  - 工具使用
  - 搜索和检索

---

## 🚀 Getting Started / 开始使用

### English
When you are ready to begin, navigate to the `Anthropic 1P/` folder and start with `01_Basic_Prompt_Structure.ipynb`.

### 中文
当您准备开始时，请导航到 `Anthropic 1P/` 文件夹，从 `01_Basic_Prompt_Structure.ipynb` 开始学习。

---

## 📚 Additional Resources / 其他资源

### English
- [Anthropic Documentation](https://docs.anthropic.com/)
- [Claude Models Overview](https://docs.anthropic.com/claude/docs/models-overview)
- [Google Sheets Version](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)

### 中文
- [Anthropic 文档](https://docs.anthropic.com/)
- [Claude 模型概览](https://docs.anthropic.com/claude/docs/models-overview)
- [Google Sheets 版本](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)