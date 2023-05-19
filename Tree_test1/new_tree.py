import math
from random import randrange,choice
import getMail


class Node:
    def __init__(self):
        self.data = None
        self.mail=[]
        self.link_sec_tree = None
        self.store_sec_tree = None
        self.left = None
        self.right = None
node=Node()


def insert_data_to_tree(tree: Node, data: list):  # insert_tree_data
    if len(data) > 0:
        # mid=len(data)//2
        if len(data) % 2 == 0:
            mid = (len(data) // 2) - 1
            tree.data = data[mid]
            if len(data[:mid]) > 0:
                tree.left = Node()
                insert_data_to_tree(tree.left, data[:mid])
            if len(data[mid + 1:]) > 0:
                tree.right = Node()
                insert_data_to_tree(tree.right, data[mid + 1:])
        else:
            mid = len(data) // 2
            tree.data = data[mid]
            if len(data[:mid]) > 0:
                tree.left = Node()
                insert_data_to_tree(tree.left, data[:mid])
            if len(data[mid + 1:]) > 0:
                tree.right = Node()
                insert_data_to_tree(tree.right, data[mid + 1:])


def insert_sec_data(node: Node, name: str):
    # print(node.data, node.store_sec_tree)
    if node.data == len(name):
        print(node.store_sec_tree)
        if not node.store_sec_tree:
            node.store_sec_tree = []
        node.store_sec_tree.append(name)
        print(node.store_sec_tree)
    elif node.data < len(name):
        insert_sec_data(node.right, name)
    else:
        insert_sec_data(node.left, name)


# second tree
def insert_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link_sec_tree:
            node.link_sec_tree = create_sec_tree()
        insert_sec_data(node.link_sec_tree, name)
    elif node.data < name[0]:
        insert_data(node.right, name)
    else:
        insert_data(node.left, name)


def printing(tree: Node):
    if tree is not None:
        printing(tree.left)
        print(tree.data)
        printing(tree.right)


def tree_data():
    tree = []
    for i in range(97, 123):
        tree.append(chr(i))
    return tree


def sec_tree_data():
    sec_tree = []
    for x in range(1, 51):
        sec_tree.append(x)
    return sec_tree


def create_tree():
    data = tree_data()
    tree_node = Node()
    insert_data_to_tree(tree_node, data)
    # printing(tree_node)
    return tree_node


def create_sec_tree():
    sec_data = sec_tree_data()
    # print(sec_data)
    tree = Node()
    insert_data_to_tree(tree, sec_data)
    # print(sec_data)
    return tree


def search_data(node: Node, name: str):
    if node.data == name[0]:
        if not node.link_sec_tree:
            return None
        return search_sec_data(node.link_sec_tree, name)
    elif node.data < name[0]:
        return search_data(node.right, name)
    else:
        return search_data(node.left, name)


def search_sec_data(node: Node, name: str):
    if node.data == len(name):
        if not node.store_sec_tree:
            return None
        print(node.store_sec_tree)
        # return node.store_sec_tree[node.store_sec_tree.index(name)]
        return linear_search(node.store_sec_tree, name)
        print(node.store_sec_tree)
    elif node.data < len(name):
        return search_sec_data(node.right, name)
    else:
        return search_sec_data(node.left, name)
# def get_length():
#     irand = randrange(8, 22)
#     print(irand)
#     return irand
# main_tree_data = []
# main_tree_data=tree_data()
# print(main_tree_data)
# def print_mail():
#     a=get_length()
#     m=''
#     for i in range(a):
#         m += choice(main_tree_data)
#     return m


def linear_search(B, item):
    # print("\t Entering Linear Search")
    i = 0

    while i != len(B):
        if B[i] == item:
            return B[i]
        i += 1
    return "Not Found"


first_tree = create_tree()
second_tree=create_sec_tree()
# name = input("Enter your email: ")

# while True:



    # name = input("Enter your email: ")
# for i in range(10):
with open('mail.txt', 'r') as file:
    for x in file:
        y = x[:-1]
        insert_data(first_tree,y)
name=input('Enter email you want to search')
search_data(first_tree,name)






#     node.mail.append(c)
# print('Node is shi m shi',node.mail)



# print("The tree is",insert_data_to_tree(first_tree, c))
    # exe=input('Enter y or Y to exit')
    # if exe=='y' or exe=='Y':
    #     search_name = input("Enter the search name: ")
    #     print("We are searching ",search_data(first_tree, search_name))
    # else:
    #     continue
# insert_data(node,name)
