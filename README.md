# 待办事项管理器 (To-Do List Manager)

这是一个用 Python 编写的简单 **命令行待办事项管理器**，支持添加、查看、删除、标记完成和取消标记任务，并可以将任务数据保存到本地。

---

## 功能

- 添加待办事项
- 查看待办事项列表（显示已完成与未完成数量）
- 删除任务（支持单个或批量删除）
- 标记任务为已完成（支持批量操作）
- 取消已完成标记（支持批量操作）
- 自动保存任务数据到 `todo_data.json`
- 数据持久化，下次启动程序可继续使用

---

## 安装与运行

1. 克隆仓库：
   ```bash
   git clone https://github.com/GooHoYi/to_do_list_manager.git
   cd to_do_list_manager
2. 可选：创建虚拟环境并激活：
     ```bash
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # macOS/Linux
3. 运行程序：
     ```bash
   python to_do_list_manager.py
## 使用示例

=== 待办事项管理器 ===
1. 添加事项
2. 查看事项
3. 删除事项
4. 标记完成
5. 取消标记
6. 退出

按提示输入数字即可进行操作

## 注意
- todo_data.json 用于保存本地数据，已添加到 .gitignore，不会被上传到仓库。

- 请确保 Python 版本 >= 3.7。

## 开源协议
本项目采用 MIT 许可证，欢迎自由使用和修改。