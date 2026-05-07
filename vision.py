"""
视觉识别模块
基于YOLOv8的截图智能分析
"""

import cv2
import numpy as np
from typing import List, Dict, Tuple
from loguru import logger
import os

class ScreenshotAnalyzer:
    """截图分析器"""
    
    def __init__(self):
        """初始化分析器"""
        self.model_path = os.getenv("YOLO_MODEL_PATH", "./models/yolov8n.pt")
        self.confidence_threshold = 0.5
        logger.info("视觉识别模块初始化完成")
        
        # 定义识别类别
        self.classes = {
            0: "仪表盘",
            1: "报警灯",
            2: "按钮",
            3: "开关",
            4: "传感器",
            5: "显示屏"
        }
        
        # 定义异常判断规则
        self.anomaly_rules = {
            "仪表盘": self._check_gauge_anomaly,
            "报警灯": self._check_alarm_anomaly,
            "显示屏": self._check_display_anomaly
        }
    
    def analyze(self, image_path: str) -> Dict:
        """
        分析截图
        
        Args:
            image_path: 图片路径
            
        Returns:
            分析结果
        """
        try:
            # 读取图片
            image = cv2.imread(image_path)
            if image is None:
                raise ValueError(f"无法读取图片: {image_path}")
            
            # TODO: 调用实际的YOLOv8模型
            # 这里提供示例结果
            objects = self._detect_objects(image)
            anomalies = self._detect_anomalies(objects, image)
            suggestions = self._generate_suggestions(anomalies)
            analysis = self._generate_analysis(objects, anomalies)
            
            return {
                "objects": objects,
                "anomalies": anomalies,
                "suggestions": suggestions,
                "analysis": analysis,
                "image_size": image.shape[:2]
            }
        
        except Exception as e:
            logger.error(f"截图分析错误: {e}")
            return {
                "error": str(e),
                "objects": [],
                "anomalies": [],
                "suggestions": []
            }
    
    def _detect_objects(self, image: np.ndarray) -> List[Dict]:
        """
        检测图片中的对象
        
        Args:
            image: 图片数组
            
        Returns:
            检测到的对象列表
        """
        # TODO: 实际的YOLOv8推理
        # 这里返回示例数据
        return [
            {
                "name": "仪表盘",
                "confidence": 0.95,
                "bbox": [100, 100, 300, 300],
                "value": "125.6",  # 识别到的数值
                "unit": "°C"
            },
            {
                "name": "报警灯",
                "confidence": 0.88,
                "bbox": [350, 150, 400, 200],
                "status": "亮起",
                "color": "红色"
            },
            {
                "name": "显示屏",
                "confidence": 0.92,
                "bbox": [50, 400, 250, 500],
                "text": "ERROR 0x1234"
            }
        ]
    
    def _detect_anomalies(self, objects: List[Dict], image: np.ndarray) -> List[str]:
        """
        检测异常状态
        
        Args:
            objects: 检测到的对象
            image: 原始图片
            
        Returns:
            异常列表
        """
        anomalies = []
        
        for obj in objects:
            obj_type = obj["name"]
            if obj_type in self.anomaly_rules:
                anomaly = self.anomaly_rules[obj_type](obj)
                if anomaly:
                    anomalies.append(anomaly)
        
        return anomalies
    
    def _check_gauge_anomaly(self, obj: Dict) -> str:
        """检查仪表异常"""
        if "value" in obj:
            try:
                value = float(obj["value"])
                # 假设正常范围是 80-120
                if value > 120:
                    return f"仪表数值过高：{value}{obj.get('unit', '')}"
                elif value < 80:
                    return f"仪表数值过低：{value}{obj.get('unit', '')}"
            except:
                pass
        return None
    
    def _check_alarm_anomaly(self, obj: Dict) -> str:
        """检查报警灯异常"""
        if obj.get("status") == "亮起":
            color = obj.get("color", "未知")
            return f"{color}报警灯亮起"
        return None
    
    def _check_display_anomaly(self, obj: Dict) -> str:
        """检查显示屏异常"""
        text = obj.get("text", "")
        if "ERROR" in text or "FAULT" in text:
            return f"显示屏显示错误信息：{text}"
        return None
    
    def _generate_suggestions(self, anomalies: List[str]) -> List[str]:
        """
        根据异常生成建议
        
        Args:
            anomalies: 异常列表
            
        Returns:
            建议列表
        """
        suggestions = []
        
        for anomaly in anomalies:
            if "仪表数值" in anomaly:
                suggestions.append("检查传感器连接和供电")
                suggestions.append("使用万用表测量传感器输出电压")
                suggestions.append("参考维修手册第3.2节")
            
            elif "报警灯" in anomaly:
                suggestions.append("查看PLC诊断缓冲区")
                suggestions.append("记录故障代码")
                suggestions.append("按照故障代码手册排查")
            
            elif "错误信息" in anomaly:
                suggestions.append("记录完整的错误代码")
                suggestions.append("查询错误代码含义")
                suggestions.append("检查相关设备状态")
        
        # 去重
        return list(set(suggestions))
    
    def _generate_analysis(self, objects: List[Dict], anomalies: List[str]) -> str:
        """
        生成综合分析
        
        Args:
            objects: 检测到的对象
            anomalies: 异常列表
            
        Returns:
            分析文本
        """
        if not anomalies:
            return "系统运行正常，未检测到明显异常。"
        
        analysis = f"检测到 {len(anomalies)} 处异常：\n"
        for i, anomaly in enumerate(anomalies, 1):
            analysis += f"{i}. {anomaly}\n"
        
        analysis += "\n建议按照标准故障诊断流程进行排查。"
        
        return analysis


# 使用示例
if __name__ == "__main__":
    analyzer = ScreenshotAnalyzer()
    
    # 测试分析
    result = analyzer.analyze("test_screenshot.jpg")
    print("识别结果：")
    for obj in result["objects"]:
        print(f"  - {obj['name']}: {obj['confidence']:.2f}")
    
    print("\n异常状态：")
    for anomaly in result["anomalies"]:
        print(f"  - {anomaly}")
    
    print("\n建议操作：")
    for suggestion in result["suggestions"]:
        print(f"  - {suggestion}")
