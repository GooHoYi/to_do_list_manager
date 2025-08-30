import json
from sys import flags

to_do_list=[]
nub_finished=0

def save_data():
    data = {
        "to_do_list": to_do_list,
        "nub_finished": nub_finished
    }
    with open("todo_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

def load_data():
    global to_do_list, nub_finished
    try:
        with open("todo_data.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            to_do_list = data.get("to_do_list", [])
            nub_finished = data.get("nub_finished", 0)
    except (FileNotFoundError,json.JSONDecodeError):
        to_do_list = []
        nub_finished = 0


def append_to_do_list():
    user_input = str(input("请输入待办事项："))
    if user_input == "":
        print("不要添加空任务")
    elif user_input in to_do_list:
        print("不要重复添加任务")
    else:
        to_do_list.append(user_input)
        save_data()
        print("事项已添加！")

def print_to_do_list():
    if len(to_do_list) == 0:
        print("暂无待办事项")
        return False
    else:
        a = 1
        print("总项目数：" + str(len(to_do_list)))
        print("未完成项目数" + str(len(to_do_list) - nub_finished))
        print("已完成项目数" + str(nub_finished))
        for i in to_do_list:
            print(str(a) + "." + i)
            a = a + 1
        return True
def delete_from_do_list():
    global nub_finished
    user_input = input("请输入要删除的编号(按0删除全部,以空格分开多个)：")
    if user_input == "0":
        user_input = input("确定清空所有任务吗？(y/n): ")
        if user_input == "y":
            to_do_list.clear()
            nub_finished = 0
            save_data()
        return
    else:
        user_input = user_input.split()
        for i in sorted(user_input,reverse=True):
            if i.isdigit():
                try:
                    if "✅" in to_do_list[int(i) - 1]:
                        nub_finished -= 1
                    to_do_list.pop(int(i) - 1)
                    save_data()
                except IndexError:
                    print("输入的编号不存在！")
            else:
                print("请输入数字！")

def finished_list():
    global nub_finished
    user_input = input("请输入要标记完成的编号(以空格分开多个)：")
    user_input = user_input.split()
    for i in user_input:
        if i.isdigit():
            try:
                if "✅" in to_do_list[int(i) - 1]:
                    print("该项目已完成")
                else:
                    to_do_list[int(i) - 1] = "✅" + to_do_list[int(i) - 1]
                    nub_finished += 1
                    save_data()
                    print("标记成功")
            except IndexError:
                print("输入的编号不存在！")
        else:
            print("请输入数字！")

def unfinished_list():
    global nub_finished
    user_input = input("请输入要取消标记的编号(以空格分开多个)：")
    user_input = user_input.split()
    for i in user_input:
        if i.isdigit():
            try:
                if "✅" in to_do_list[int(i) - 1]:
                    to_do_list[int(i) - 1] = str(to_do_list[int(i) - 1]).replace("✅", "")
                    nub_finished -= 1
                    save_data()
                    print("标记已取消")
                else:
                    print("你还没有完成该项目")
            except IndexError:
                print("输入的编号不存在！")
        else:
            print("请输入数字！")

load_data()
while True:
    try:
        print("=== 待办事项管理器 ===\n1. 添加事项\n2. 查看事项\n3. 删除事项\n4. 标记完成\n5. 取消标记\n6.退出")
        user_input=input("请输入选项：")
        if user_input=="1":
            append_to_do_list()
        elif user_input=="2":
            print_to_do_list()
            input("请按回车继续")
        elif user_input=="3":
            if print_to_do_list():
                delete_from_do_list()
        elif user_input=="4":
            if print_to_do_list():
                finished_list()
        elif user_input=="5":
            if print_to_do_list():
                unfinished_list()
        elif user_input=="6":
            save_data()
            print("再见")
            break
        else:
            print("请输入正确的数字！")
    except KeyboardInterrupt:
        save_data()
        print()
        print("程序被手动终止，正常退出")
        exit()