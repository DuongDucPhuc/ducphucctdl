class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def remove_duplicates(head): # tạo hàm mới với giá trị là head
    if head is None:         # so sánh nếu head là none
        return head          # trả giá trị về head

    seen_values = set()      # dùng để lưu các giá trị đã thấy trong linklist
    current = head           # gán current = head
    previous = None          # gán previous = none

    while current is not None:         # vòng lặp while với điều kiện current không phải là none
        if current.value in seen_values:  # nếu giá trị current có trong seen_values
            previous.next = current.next # Loại bỏ nút hiện tại (bị trùng)
        else:
            seen_values.add(current.value) # ngược lại thì thêm giá trị vào 
            previous = current

        current = current.next

    return head

# Tạo danh sách liên kết không có thứ tự: 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next= ListNode(4)
head.next.next.next.next.next.next.next= ListNode(5)

a = remove_duplicates(head)
while a is not None:
    print(a.value, end=" -> ")
    a = a.next
print("None")
