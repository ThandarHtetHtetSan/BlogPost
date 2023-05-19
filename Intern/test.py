class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printLinkedList(self):
        result=self.head
        while result is not None:
            print(result.item)
            result=result.next
if  __name__ == '__main__':
        linkedlist=LinkedList()
        linkedlist.head=Node(5)
        second=Node(10)
        third=Node(15)
        linkedlist.head.next=second
        second.next=third

    #Print LinkedList
while linkedlist.head != None:
    print(linkedlist.head.item,end=' ')
    linkedlist.head=linkedlist.head.next

    # user.data={}
    # for i in range(3):
    #     user_name=input("Enter your name")
    #     user_mail=input("Enter your email")
    #     user_pass=input("Enter your password")
    #     user_phone=input("Enter your phone")
    #     key=len(user_data)
    #     user_data.update({key:{"name":user_name,"mail":user_mail,
    #                            "password":user_pass,"phone":user_phone
    #                            }})
    #     linkedlist=LinkedList()
    #     linkedlist.head=None(user_data)





