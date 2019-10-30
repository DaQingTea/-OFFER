#从尾到头打印链表

 class Solution:

 	def printListFormTaulToHead(self, listNode):
 		#把链表复制进列表，倒着打印
 		#V2,直接通过insert方法插入到头部
 		list1 = []
 		while listNode:
 			list1.insert[0,listNode.val]
 			listNode = liseNode.next
 		return list1