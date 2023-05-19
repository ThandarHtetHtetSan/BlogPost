import own_db_tree
import sec_tree

def printing(node):

    if node is not None:
        printing(node.left)
        if node.sec_data!=None:
            print(node.sec_data)
        printing(node.right)

first_tree = own_db_tree.tree
sec__tree = sec_tree.tree

def connection_test(ftree,name):

    if ftree is not None:
        connection_test(ftree.left, name)
        if ftree.data == name[0]:
            sec_tree_con_test(sec__tree,len(name),name)
            return
        connection_test(ftree.right,name)

def sec_tree_con_test(sec__tre , length , name ):

    if sec__tre is not None:
        sec_tree_con_test(sec__tre.left,length,name)
        if sec__tre.data==length:
            sec__tre.sec_data = name
            print("We found for third tree")
            return

        sec_tree_con_test(sec__tre.right,length,name)
#def length(dat,f_tree,name):
#    if len(dat)==len(name) and f_tree.data==name[0] :
#        thr_data=dat

if __name__ == '__main__':

    name = input("Enter name")

    connection_test(first_tree,name)
    printing(sec__tree)



