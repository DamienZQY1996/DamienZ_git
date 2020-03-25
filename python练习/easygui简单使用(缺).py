import easygui as g
import sys

###对于所有函数而言，前两个参数是消息和标题。绝大部分的函数都有默认参数，几乎所有的组件都会显示一个消息和标题（标题默认是空字符串，消息有一个简单的默认值）

# msgbox
g.msgbox('hello','title')

# choicebox
choices_argum=('Yes','No')
reply=g.choicebox('Yes or No','reply',choices=choices_argum)
print(reply)


# msgbox中修改按键值
g.msgbox('我一定要学会编程！',ok_button='加油！')


# ccbox
if g.ccbox('try again?',choices=['yes','no']):
    g.msgbox('you can\'t try again')
else:
    sys.exit(0)


# ynbox
g,ynbox('yse or no?',choices=('yes','no'))


# buttonbox返回按钮的文本内容
g.buttonbox('你喜欢以下哪一种水果？','选择题',['草莓','西瓜','芒果'])


# indexbox返回序号0，1，2……
g.indexbox('yes or no?',choices=['yes','no'])


# boolbox(如果第一个按钮被选中返回1，否则返回0)
g.boolbox('你喜欢以下哪一种水果？','选择题',['草莓','西瓜','芒果'])


# 显示图片（仅支持GIF格式）
g.msgbox('handsome','DamienZ',image='2.gif')


# multchoicebox
g.multchoicebox('你喜欢以下哪些水果？',choices=['草莓','西瓜','芒果'])


## 用户输入信息
# enterbox
g.enterbox('please say something')


# integerbox要求用户只能输入范围内的整型数值，否则会要求用户重新输入
g.integerbox('please input a number',lowerbound=0,upperbound=9)


# multenterbox(①如果用户输入的值比选项少，返回列表中的值用空字符串填充②如果用户输入的值比选项多，返回列表中的值将截断为选项的数量③如果用户取消操作，则返回域中的列表值或None值)
list1=['用户名：','密码：']
g.multenterbox('请输入用户名和密码','登录',fields=(list1))
##


## 用户输入密码（*********）
# passwordbox
g.passwordbox('请输入密码：')


# multpasswordbox(最后一个输入框显示为*********)
g.multpasswordbox('请输入用户名和密码','登录',fields=(list1))
##


## 显示文本
# textbox
g.textbox('文件内容如下：','显示文件内容',['1\n','2\n','3\n'])
g.textbox('文件内容如下：','显示文件内容',text=open('C:\\Users\\DamienZ\\Desktop\\python练习\\文件读写操作例子.txt'))


# codebox相当于textbox(codebox=1)
g.codebox('文件内容如下：','显示文件内容',['1\n','2\n','3\n'])
##


## 目录与文件
# diropenbox（返回用户选择的目录名，带完整路径）
g.diropenbox(default='C:\\')


# fileopenbox（返回用户选择的文件名，带完整路径）
g.fileopenbox(default='C:/Users/DamienZ/Desktop/python练习/*.py',filetypes=['*.py',['*.txt','*.py']])


# filesavebox（用于选择文件需要保存的路径，带完整路径）
g.filesavebox(default='C:/Users/DamienZ/Desktop/python练习/2.gif',filetypes=['*.txt','*.gif','*.py'])
##


## 记住用户的设置
# EgStore

# -------------------------------------
# creat "setting",a persistent setting object.
# note that the "filename" argument is required.
# the directory for the persistent file must already exist.
# --------------------------------------
settingsFilename=os.path.join('C:','Users/DamienZ/Desktop/python练习','settings.txt')
settings=g.EgStore(settingsFilename)

#缺少

##


## 捕获异常
# exceptionbox（异常出现时，显示堆栈追踪在一个codebox()中并且允许你做进一步的处理）
try:
    print('I love you.')
    int('abc')
except:
    g.exceptionbox()
##
