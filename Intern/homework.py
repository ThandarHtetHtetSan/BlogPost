class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def AddNode(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def printlinkedlist(self):
        result = self.head
        while result is not None:
            print(result.item)
            result = result.next


def getData():
    user = {}
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    user.update({"name": name, "email": email, "password": password})
    return user


if __name__ == '__main__':
    linkedlist = Linkedlist()
    for i in range(5):
        userdata = getData()

        if linkedlist.head is None:
            linkedlist.head = Node(userdata)


        else:
            res = linkedlist.head
            while res is not None:
                if res.item["email"] == userdata["email"]:
                    print("Your email have to be unique...Try Again!")

                    break
                res = res.next

            else:
                linkedlist.AddNode(userdata)
    linkedlist.printlinkedlist()
