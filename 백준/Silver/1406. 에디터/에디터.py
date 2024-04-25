#### gpt 코드 #####
### 다시 풀어 봐야함 ####

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None)  # 더미 헤드 노드
        self.tail = Node(None)  # 더미 테일 노드
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cursor = self.tail  # 커서는 초기에 테일에 위치

    def insert(self, char):
        new_node = Node(char)
        new_node.prev = self.cursor.prev
        new_node.next = self.cursor
        self.cursor.prev.next = new_node
        self.cursor.prev = new_node

    def delete(self):
        if self.cursor.prev != self.head:  # 헤드 노드의 다음 노드가 아닐 때만 삭제
            self.cursor.prev = self.cursor.prev.prev
            self.cursor.prev.next = self.cursor

    def move_left(self):
        if self.cursor.prev != self.head:  # 맨 앞이 아니면
            self.cursor = self.cursor.prev

    def move_right(self):
        if self.cursor != self.tail:  # 맨 끝이 아니면
            self.cursor = self.cursor.next

    def to_string(self):
        result = []
        current = self.head.next
        while current != self.tail:
            result.append(current.data)
            current = current.next
        return ''.join(result)

# 초기 문자열과 명령어 처리
editor = DoublyLinkedList()
initial_string = input()  # 초기 문자열 입력
for char in initial_string:
    editor.insert(char)

m = int(input())  # 명령어 수 입력
for _ in range(m):
    command = input().split()
    if command[0] == 'L':
        editor.move_left()
    elif command[0] == 'D':
        editor.move_right()
    elif command[0] == 'B':
        editor.delete()
    elif command[0] == 'P':
        editor.insert(command[1])

print(editor.to_string())
