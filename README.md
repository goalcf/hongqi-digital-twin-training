# 基于多模态AI的红旗产线数字孪生智能训练系统

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Unity](https://img.shields.io/badge/Unity-2021.3+-green.svg)](https://unity.com/)

> 面向新能源汽车技术专业的智能实训系统，融合数字孪生与多模态AI技术

## 📋 项目简介

本系统针对职业教育实训环节设备不足、故障场景复现困难、个性化指导覆盖面窄等问题，开发了基于多模态AI的红旗产线数字孪生智能训练系统。

### 核心特性

- 🎮 **数字孪生仿真**：Unity3D引擎1:1还原红旗新能源汽车生产线
- 🤖 **多模态AI陪练**：支持文字问答、截图智能识别、实时操作纠偏
- 📊 **智能评价系统**：自动生成多维度操作报告，支持学习轨迹追踪
- 🎯 **故障模拟训练**：20余类典型故障场景，安全可复现

### 应用效果

- ⚡ 任务完成效率提升 **31.4%**（35分钟 → 24分钟）
- 👍 学生满意度达 **89%-92%**
- 📈 考核成绩提升 **9.8%**（78.5分 → 86.2分）
- 🎓 优秀率提升 **15个百分点**

## 🏗️ 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    用户层（学生/教师）                      │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  表现层：Unity3D仿真界面 | 对话窗口 | 评价报告展示        │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  业务逻辑层：操作监听 | 截图识别 | 对话管理 | 评价生成   │
└─────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────┐
│  AI能力层：Qwen3.5 | 豆包1.8 | YOLOv8 | 知识库检索       │
└─────────────────────────────────────────────────────────┘
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Unity 2021.3+
- CUDA 11.0+（可选，用于GPU加速）

### 安装步骤

1. **克隆仓库**
```bash
git clone https://github.com/your-username/hongqi-digital-twin-training.git
cd hongqi-digital-twin-training
```

2. **安装依赖**
```bash
pip install -r requirements.txt
```

3. **配置环境变量**
```bash
cp .env.example .env
# 编辑 .env 文件，填入API密钥
```

4. **启动后端服务**
```bash
python backend/main.py
```

5. **运行Unity仿真端**
- 使用Unity打开 `unity-project` 文件夹
- 点击运行按钮启动仿真环境

## 📚 功能模块

### 1. 仿真训练模块
- 红旗生产线工位还原（焊装、涂装、总装）
- 传感器故障、通信异常、机械故障等场景模拟
- 交互式操作训练

### 2. 智能陪练模块
- **文字问答**：基于专业知识库的智能对话
- **截图分析**：YOLOv8识别仪表、报警灯、操作异常
- **实时提示**：操作偏差自动触发分级提示

### 3. 分析评价模块
- 操作规范性评分
- 故障诊断准确性分析
- 处理时效性统计
- 学习轨迹可视化

### 4. 教师管理模块
- 故障案例配置
- 提示词内容审核
- 班级学习情况统计
- 个性化学习路径推荐

## 📖 使用示例

### 截图智能识别

```python
from backend.vision import ScreenshotAnalyzer

analyzer = ScreenshotAnalyzer()
result = analyzer.analyze("screenshot.jpg")

print(f"识别结果：{result['objects']}")
print(f"异常状态：{result['anomalies']}")
print(f"建议操作：{result['suggestions']}")
```

### AI对话问答

```python
from backend.ai_tutor import AITutor

tutor = AITutor()
response = tutor.ask("传感器显示数值异常，应该如何排查？")

print(response)
# 输出：首先请观察传感器的具体数值范围，然后思考：
# 1. 数值是否超出正常工作范围？
# 2. 传感器供电是否正常？
# 3. 信号线路是否存在接触不良？
```

## 📊 数据统计

系统应用于长春汽车职业技术大学智能机器人技术专业2024级72名学生：

| 指标 | 使用前 | 使用后 | 提升幅度 |
|------|--------|--------|----------|
| 任务完成时长 | 35分钟 | 24分钟 | ↓31.4% |
| 截图功能满意度 | - | 89% | - |
| 自主使用意愿 | - | 92% | - |
| 期末考核平均分 | 78.5分 | 86.2分 | ↑9.8% |
| 优秀率（≥90分） | - | - | ↑15个百分点 |

## 🛠️ 技术栈

- **前端仿真**：Unity3D 2021.3
- **后端框架**：FastAPI
- **大语言模型**：阿里通义千问 Qwen3.5、字节豆包1.8
- **视觉识别**：YOLOv8
- **数据库**：SQLite
- **向量检索**：FAISS

## 📁 项目结构

```
hongqi-digital-twin-training/
├── backend/                 # 后端服务
│   ├── main.py             # 主入口
│   ├── ai_tutor.py         # AI陪练模块
│   ├── vision.py           # 视觉识别模块
│   ├── evaluator.py        # 评价模块
│   └── knowledge_base/     # 知识库
├── unity-project/          # Unity仿真项目
│   ├── Assets/
│   ├── Scenes/
│   └── Scripts/
├── docs/                   # 文档
│   ├── 使用手册.md
│   ├── 安装指南.md
│   └── API文档.md
├── data/                   # 数据文件
│   ├── prompts/           # 提示词库
│   ├── fault_cases/       # 故障案例
│   └── knowledge/         # 专业知识
├── requirements.txt        # Python依赖
├── .env.example           # 环境变量示例
└── README.md              # 项目说明
```

## 🤝 贡献指南

欢迎提交Issue和Pull Request！

1. Fork本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 提交Pull Request

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。




## 🙏 致谢

感谢以下单位和个人的支持：
- 长春汽车职业技术大学
- 中国第一汽车集团有限公司
- 阿里云通义千问团队
- 字节跳动豆包团队

## 📸 系统截图

### 仿真训练界面
![仿真界面](docs/images/simulation.png)

### AI陪练对话
![AI对话](docs/images/ai-chat.png)

### 评价报告
![评价报告](docs/images/evaluation.png)

---

⭐ 如果这个项目对您有帮助，请给我们一个Star！
