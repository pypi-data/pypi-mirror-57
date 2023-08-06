# -*- coding: utf-8 -*-
'''该模块提供一个名为print_lol的函数，用于输出列表中的各个元素，包含
   嵌套列表中的元素'''
def print_lol (the_list,indent=False,level=0):
    '''the_list为输入列表，indent选择是否对嵌套表元素进行缩进输出，
level选择整体缩进的程度，函数可将列表中的元素输出（包含嵌套表中的元素）'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            for tab_stop in range(level):
                if indent:
                    print("\t",end='')
            print(each_item)

