# utf-8

class SingleNode(object):
    """ 单链表的结点 """
    def __init__(self,item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None # 初始为空，不指向任何

class SingleLinkList(object):
    """单链表"""
    def __init__(self):
        self._head = None

    def is_empty(self):
        """判断链表是否为空"""
        return self._head == None

    def length(self):
        """链表长度"""
        # cur初始时指向头节点
        cur = self._head
        count = 0

        # 尾节点指向None
        # 当未到达尾部时:
        while cur != None:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        cur = self._head
        while cur != None:
            print(cur.item,end=",") # 不要打印一个元素换一行
            cur = cur.next

    def append(self,item):
        '''链表尾部添加元素'''
        node = SingleNode(item)
        # 为空的话 直接添加就是了
        if self.is_empty():
            self._head = node
        # 不空的话：一直往后指，和遍历很类似
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def add(self,item):
        '''指定头部添加元素'''
        node = SingleNode(item) # 新建node 产生一个新的节点
        node.next = self._head
        self._head = node

    def insert(self,pos,item):
        '''指定位置添加元素'''
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1
            # 初始从头节点开始移动到pos位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点(这一步勿忘！)
            pre.next = node

    def search(self,item):
        """链表查找节点是否存在，并返回True或者False"""
        cur = self._head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    def remove(self, item):
        """删除节点"""
        cur = self._head
        pre = None
        while cur != None:
            # 找到了指定元素
            if cur.item == item:
                # 如果第一个就是删除的节点
                if not pre:
                    # 将头指针指向头节点的后一个节点
                    self._head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next

'''测试'''
if __name__=="__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())
    print("\n")

    ll.append(2)
    ll.add(8)
    ll.insert(0,100)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.travel()

    print (ll.search(3))
    print (ll.search(5))
    ll.remove(1)

    print ("length:",ll.length())
    ll.travel()