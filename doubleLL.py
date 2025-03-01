# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:26:01 2025

@author: swath
"""
#double LL
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

    head=None
    tail=None
one=Node(10)
two=Node(20)
three=Node(30)
four=Node(40)
five=Node("swathi")

one.next=two
two.previous=one

two.next=three
three.previous=two

three.next=four
four.previous=three

four.next=five
five.previous=four

five.next=None
five.previous=four

head=one
tail=four

one.next=two
two.next=three
three.next=four
four.next=five
five.next=None

temp=head
while temp!=None:
    print(temp.data)
    temp=temp.next
    
    
temp=tail
while temp!=None:
    print(temp.data)
    temp=temp.previous