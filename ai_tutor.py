"""
AI智能陪练模块
基于大语言模型的苏格拉底式教学引导
"""

from typing import List, Dict
import os
from loguru import logger

class AITutor:
    """AI陪练类"""
    
    def __init__(self):
        """初始化AI陪练"""
        self.api_key = os.getenv("DASHSCOPE_API_KEY")
        self.model = os.getenv("LLM_MODEL", "qwen-turbo")
        self.system_prompt = self._load_system_prompt()
        logger.info("AI陪练模块初始化完成")
    
    def _load_system_prompt(self) -> str:
        """加载系统提示词"""
        return """你是一位经验丰富的汽车维修实训指导教师，专注于红旗新能源汽车生产线的故障诊断与维修教学。

教学原则：
1. 采用苏格拉底式提问法，引导学生主动思考，不直接给出答案
2. 根据学生的回答，逐步深入，帮助建立系统化的问题分析框架
3. 强调标准操作流程（SOP）的重要性
4. 结合企业实际案例，确保教学内容符合行业标准

回答要求：
- 简洁明了，避免冗长
- 分步骤引导，每次提出1-2个关键问题
- 适时给予鼓励和肯定
- 必要时提供参考资料位置（如手册章节）
"""
    
    def ask(self, question: str, context: List[Dict] = None) -> str:
        """
        处理学生提问
        
        Args:
            question: 学生的问题
            context: 对话上下文
            
        Returns:
            AI的回答
        """
        try:
            # TODO: 调用实际的大模型API
            # 这里提供示例响应
            
            if "传感器" in question and "异常" in question:
                return """很好的观察！传感器显示异常时，我们需要系统地排查。

让我们一起思考几个关键问题：

1. **数值异常的具体表现**
   - 数值是持续异常还是间歇性的？
   - 异常数值是偏高还是偏低？

2. **基础检查**
   - 传感器的供电电压是否正常？（应为5V±0.5V）
   - 信号线路连接是否牢固？

3. **下一步操作**
   请先用万用表测量传感器的供电电压，然后告诉我测量结果。

💡 提示：可以参考《红旗新能源汽车维修手册》第3.2节"传感器故障诊断流程"。
"""
            
            elif "PLC" in question or "通信" in question:
                return """通信故障是生产线常见问题之一。让我们按照标准流程来分析：

**思考方向：**
1. 通信指示灯状态如何？（绿灯/红灯/闪烁）
2. 网络拓扑中哪个节点出现问题？
3. 是否有报警代码？

**建议操作：**
- 先检查物理连接（网线、接头）
- 查看PLC诊断缓冲区
- 使用诊断软件查看通信状态

你现在看到的具体现象是什么？我们可以针对性地分析。
"""
            
            else:
                return """我理解你的问题。在解决这个问题之前，让我们先明确几点：

1. 当前的具体现象是什么？
2. 你已经尝试过哪些操作？
3. 有没有相关的报警信息？

请详细描述一下现场情况，我会帮你一步步分析。

记住：**观察 → 分析 → 假设 → 验证** 是故障诊断的基本流程。
"""
        
        except Exception as e:
            logger.error(f"AI问答错误: {e}")
            return "抱歉，系统遇到了一些问题。请稍后再试或联系教师。"
    
    def evaluate_answer(self, student_answer: str, expected_keywords: List[str]) -> Dict:
        """
        评价学生的回答
        
        Args:
            student_answer: 学生的回答
            expected_keywords: 期望的关键词
            
        Returns:
            评价结果
        """
        score = 0
        matched_keywords = []
        
        for keyword in expected_keywords:
            if keyword in student_answer:
                score += 1
                matched_keywords.append(keyword)
        
        accuracy = score / len(expected_keywords) if expected_keywords else 0
        
        return {
            "score": score,
            "accuracy": accuracy,
            "matched_keywords": matched_keywords,
            "feedback": self._generate_feedback(accuracy)
        }
    
    def _generate_feedback(self, accuracy: float) -> str:
        """生成反馈"""
        if accuracy >= 0.8:
            return "非常好！你的分析很全面。"
        elif accuracy >= 0.6:
            return "不错，但还可以考虑得更全面一些。"
        elif accuracy >= 0.4:
            return "有一定思路，但需要更系统地分析。"
        else:
            return "让我们重新梳理一下思路。"


# 使用示例
if __name__ == "__main__":
    tutor = AITutor()
    
    # 测试问答
    question = "传感器显示数值异常，应该如何排查？"
    response = tutor.ask(question)
    print(f"学生提问：{question}")
    print(f"AI回答：\n{response}")
