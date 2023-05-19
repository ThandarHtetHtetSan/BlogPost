
import sec_tree
import main
import own_db_tree
tree_1=own_db_tree.tree
tree_2=sec_tree.tree
class Node:
    def __init__(self,data):
        self.data= data
        self.thr_data=[]
        self.left: Node = None
        self.right: Node = None

def length(node,root_tree,name):
    if node is None:
        if node.data==len(name) and name[0]==root_tree.data:
            node.thr_data.append(name)




#k=20
#data=[]
#for i in range(len(name)):
#if len(name[i])==k and name[0]==:
#data[i]=name[i]
#def length(data,f_tree,name):
 #   if len(data)==len(name) and f_tree.data==name[0] :
  ##      thr_data.append(data)
    #    print("Your data is stored in length ",len(data))
#data=[]
#ata1=[]
#for i in range (5):
 #   name=input("Enter your name")
  #  data.append(name)
#for i in range (5):
 #  if len(data[i])==len(name) and data[i][0]==name[0]:
  #          thr_data.append(name)
   #         print(thr_data)







