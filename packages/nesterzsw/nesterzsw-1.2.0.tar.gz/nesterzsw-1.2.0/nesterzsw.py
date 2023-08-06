# -*- coding: utf-8 -*-
'''该模块提供一个名为print_lol的函数，用于输出列表中的各个元素，包含
   嵌套列表中的元素'''
def print_lol (the_list,level=0):
    '''该函数的输入值为任一列表，函数可将列表中的元素输出，包含嵌套表中的元素'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)
        else:
            for tab_stop in range(level):
                print("\t",end='')
            print(each_item)

