import os
import time

def GetTime(): #获取当前时间
    return time.strftime("%y-%m-%d %H:%M:%S", time.localtime())

#修改默认的提交信息
commit_msg=f" \"Code updated: {GetTime()}\" "
url=input("Please input url:")

#git提交命令
cmd_1 = "git init"
cmd_2 = "git add --all"
cmd_3 = "git commit -m"+commit_msg
cmd_4 = "git branch -M main"
cmd_5 = "git remote add origin "+url
cmd_6 = "git push -u origin main"


print("[开始] 执行git连接")

print('[CMD]',cmd_1)
os.system(cmd_1)#初始化
print('[CMD]',cmd_2)
os.system(cmd_2)#添加所有文件更改到工作区
print('[CMD]',cmd_3)
os.system(cmd_3)#自动commit
print('[CMD]',cmd_4)
os.system(cmd_4)#创建branch
print('[CMD]',cmd_5)
os.system(cmd_5)#建立连接
print('[CMD]',cmd_6)
os.system(cmd_6)#上传文件

print("[结束] 完成git连接及上传")
print("窗口将在5s后关闭...")
time.sleep(5)#休眠5秒可以看清楚结果