#-*-coding:utf8-*-
import itchat
itchat.auto_login(hotReload=True)
users = itchat.search_friends(name='张雨晴')
print(users)
userName = users[0]['UserName']
itchat.send("我最帅",toUserName = userName)
print('succeed')
