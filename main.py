class Node:

  def __init__(self, x, next=None):
    self.val = x
    self.next = next


class Solution:

  def printList(self, list: Node):
    node = list
    ans = []
    while node != None:
      if node.val != None:
        ans.append(node.val)

      node = node.next if node.next != None else None

    print('print', ans)

  def getMinNodeAndIterate(self, n1: Node, n2: Node) -> (Node, Node, Node):
    minNode = None

    if n1 != None:
      if n2 != None:
        if n1.val < n2.val:
          minNode = n1
          n1 = n1.next if n1.next != None else None
          # print('g1', minNode.val)
        else:
          minNode = n2
          n2 = n2.next if n2.next != None else None
          # print('g2', minNode.val)
      else:
        minNode = n1
        n1 = n1.next if n1.next != None else None
        # print('g3', minNode.val)
    else:
      if n2 != None:
        minNode = n2
        n2 = n2.next if n2.next != None else None
        # print('g4', minNode.val)

    return minNode, n1, n2

  def mergeTwoLists(self, n1: Node, n2: Node) -> Node:
    newList = None
    lastNode = None
    minNode = None

    while n1 != None or n2 != None:
      # with function - slower, but better for code style...
      # minNode, n1, n2 = self.getMinNodeAndIterate(n1, n2)
      if n1 != None:
        if n2 != None:
          if n1.val < n2.val:
            minNode = n1
            n1 = n1.next if n1.next != None else None
          else:
            minNode = n2
            n2 = n2.next if n2.next != None else None
        else:
          minNode = n1
          n1 = n1.next if n1.next != None else None
      else:
        if n2 != None:
          minNode = n2
          n2 = n2.next if n2.next != None else None

      if lastNode == None:
        newList = minNode
        lastNode = newList
      else:
        #- [1].next -> [2].next(Last)
        lastNode.next = minNode
        #> [1].next -> [2].next(Last).next -> [3]
        lastNode = lastNode.next
        #> [1].next -> [2].next -> [3].next(Last)

    return newList


my = Solution()

n1 = Node(1, Node(3, Node(5)))
n2 = Node(2, Node(4, Node(6, Node(7, Node(10)))))
# n1 = Node(2, Node(3))
# n2 = Node(1, Node(4))
# n1 = Node(5)
# n2 = Node(1, Node(2, Node(4)))

ansList = my.mergeTwoLists(n1, n2)

my.printList(ansList)

# Runtime: 32 ms, faster than 85.46% of Python3 online submissions for Merge Two Sorted Lists.
# Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.