#!/usr/bin/env python
# -*- coding: utf-8 -*-
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

'''合并字符串'''
first_name = "朱"
last_name = "毅骏"
full_name = first_name + " " + last_name
print(full_name)
print('hello,' + full_name.title() + '!')
'''拼接来创建消'''
message = "Hello, " + full_name.title() + "!"
print(message)
'''字符串中添加制表符，可使用字符组合\t'''
print("\tPython\n")
print('输出语言')
'''字符串中添加换行符，可使用字符组合\n'''
# print("Languages:\nPython\nC\nJavaScript")
'''，删除用户输入的数据中的多余的空白'''
favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())
