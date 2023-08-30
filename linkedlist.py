# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertion_at_beginning(self,data):
#         nb=Node(data)
#         nb.next=self.head
#         self.head=nb

#     def insertion_at_end(self,data):
#         ne=Node(data)
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=ne

#     def insertion_at_pos(self,pos,data):
#         np=Node(data)
#         temp=self.head
#         for i in range(pos-1):
#             temp=temp.next
#         np.data=data
#         np.next=temp.next
#         temp.next=np

#     def deletion_at_beginning(self):
#         temp=self.head
#         self.head=temp.next
#         temp.next=None

#     def deletion_at_end(self):
#         prev=self.head
#         temp=self.head.next
#         while temp.next is not None:
#             temp=temp.next
#             prev=prev.next
#         prev.next=None

#     def deletion_at_position(self,pos):
#         prev=self.head
#         temp=self.head.next
#         for i in range(1,pos-1):
#             prev=prev.next
#             temp=temp.next
#         prev.next=temp.next
    

#     def display(self):
#         if self.head is None:
#             print("list is empty")
#         else:
#             temp=self.head
#             while temp:
#                print(temp.data,"-->",end="")
#                temp=temp.next

    
# l=LinkedList()
# n1=Node(10)
# l.head=n1
# n2=Node(20)
# n1.next=n2
# l.insertion_at_beginning(1)
# l.insertion_at_beginning(3)
# l.insertion_at_end(30)
# l.insertion_at_end(40)
# l.insertion_at_pos(2,15)
# l.deletion_at_beginning()
# l.deletion_at_end()
# l.deletion_at_position(3)
# l.display()



# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insertion_at_beginning(self,data):
#         nb=Node(data)
#         nb.next=self.head
#         self.head=nb

#     def insertion_at_end(self,data):
#         ne=Node(data)
#         temp=self.head
#         while temp.next:
#             temp=temp.next
#         temp.next=ne

#     def insertion_at_pos(self,pos,data):
#         np=Node(data)
#         if pos==0
#            nb.next=self.head
#            self.head=nb
#         else:   
#            temp=self.head
#            for i in range(pos-1):
#               temp=temp.next
#            np.data=data
#            np.next=temp.next
#            temp.next=np

#     def display(self):
#         if self.head is None:
#             print("list is empty")
#         else:
#             temp=self.head
#             while temp:
#                print(temp.data,"-->",end="")
#                temp=temp.next

# l=LinkedList()
# n1=Node(10)
# l.head=n1
# n2=Node(20)
# n1.next=n2
# l.insertion_at_beginning(1)
# l.insertion_at_beginning(3)
# l.insertion_at_beginning(4)
# l.insertion_at_end(30)
# l.insertion_at_end(40)
# l.insertion_at_end(50)
# l.insertion_at_pos(4,25)
# l.display()




# deletion in LinkedList

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# class LinkedList:
#     def __init__(self):
#         self.head=None

    

    # def deletion_at_beginning(self):
    #     if self.head is None:
    #         return
    #     temp=self.head
    #     self.head=temp.next
    #     temp.next=None

#     def deletion_at_end(self):
#         prev=self.head
#         temp=self.head.next
#         while temp.next is not None:
#             temp=temp.next
#             prev=prev.next
#         prev.next=None

#     def deletion_at_position(self,pos):
#         prev=self.head
#         temp=self.head.next
#         for i in range(1,pos-1):
#             prev=prev.next
#             temp=temp.next
#         prev.next=temp.next
    

#     def display(self):
#         if self.head is None:
#             print("list is empty")
#         else:
#             temp=self.head
#             while temp:
#                print(temp.data,"-->",end="")
#                temp=temp.next

    
# l=LinkedList()
# n1=Node(10)
# l.head=n1
# n2=Node(20)
# n1.next=n2
# n3=Node(30)
# n2.next=n3
# n4=Node(40)
# n3.next=n4
# l.deletion_at_beginning()
# l.deletion_at_end()
# l.deletion_at_position(3)
# l.display()
