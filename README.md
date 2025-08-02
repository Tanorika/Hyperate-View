# Hyperate-View

基于 Hyperate 的桌面心率实时显示工具，支持透明背景和鼠标点击穿透。

---

## 功能特点

- 显示来自 Hyperate 的心率监测网页  
- 支持透明窗口，背景不遮挡桌面或其他程序  
- 支持鼠标点击穿透，点击事件可穿过窗口传递到下层程序  
- 窗口大小和位置可通过配置文件灵活调整  
- 跨平台（基于 PyQt5，但穿透点击目前仅支持 Windows）

---

## 使用方法

1. 修改 `config.json` 文件中的 `url` 为你自己的 Hyperate 心率检测地址。  
2. 根据需要调整 `config.json` 中的 `x`, `y`, `width`, `height`，以调整窗口的位置和大小。  
3. 运行 `listen.py` 启动程序，心率窗口会显示在桌面。  

---

## 配置示例（config.json）

```json
{
  "url": "https://www.hyperate.io/pulse-dynamics-ecg?id=你的ID",
  "x": 100,
  "y": 100,
  "width": 500,
  "height": 200
}

    url：你的 Hyperate 心率网页链接

    x, y：窗口初始显示位置（屏幕坐标）

    width, height：窗口宽度和高度（像素）
```
依赖安装

确保 Python 环境安装了以下依赖：

pip install PyQt5 PyQtWebEngine pywin32

运行程序

python listen.py
