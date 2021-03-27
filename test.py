class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

def merge_two_ll(head1: Node, head2: Node):
    if head1 is None:
        return head2
    elif head2 is None:
        return head1
    else:
        temp = None
        if head1.value <= head2.value:
            temp = head1
            temp.next = merge_two_ll(head1.next, head2)
        else:
            temp = head2
            temp.next = merge_two_ll(head1, head2.next)
    return temp

def display(head: Node):
    current = head
    while current is not None:
        print(current.value, end=' ')
        if current.next is not None:
            print('-->', end=' ')
        current = current.next

head1 = Node(1)
left11 = Node(2)
left12 = Node(4)
head1.next = left11
left11.next = left12

display(head1)

head2 = Node(2)
head2.next = Node(5)

display(head2)

new_head = merge_two_ll(head1, head2)
display(new_head)
