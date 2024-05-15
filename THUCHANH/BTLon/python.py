class Meaning:
    def __init__(self, word_type, definition, example):
        self.word_type = word_type
        self.definition = definition
        self.example = example

class TreeNode:
    def __init__(self, word):
        self.word = word
        self.meanings = []
        self.left = None
        self.right = None

class EnglishDictionary:
    def __init__(self):
        self.root = None

    def insert(self, word, meaning):
        if not self.root:
            self.root = TreeNode(word)
            self.root.meanings.append(meaning)
        else:
            self._insert_recursive(self.root, word, meaning)

    def _insert_recursive(self, node, word, meaning):
        if word < node.word:
            if not node.left:
                node.left = TreeNode(word)
                node.left.meanings.append(meaning)
            else:
                self._insert_recursive(node.left, word, meaning)
        elif word > node.word:
            if not node.right:
                node.right = TreeNode(word)
                node.right.meanings.append(meaning)
            else:
                self._insert_recursive(node.right, word, meaning)
        else:
            node.meanings.append(meaning)

    def remove(self, word):
        if not self.root:
            return False
        self.root = self._remove_recursive(self.root, word)
        return True

    def _remove_recursive(self, node, word):
        if not node:
            return None

        if word < node.word:
            node.left = self._remove_recursive(node.left, word)
        elif word > node.word:
            node.right = self._remove_recursive(node.right, word)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.word = min_node.word
                node.meanings = min_node.meanings
                node.right = self._remove_recursive(node.right, min_node.word)
        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def search(self, word):
        return self._search_recursive(self.root, word)

    def _search_recursive(self, node, word):
        if not node:
            return None
        if word == node.word:
            return node.meanings
        elif word < node.word:
            return self._search_recursive(node.left, word)
        else:
            return self._search_recursive(node.right, word)
        
    def save_to_file(self, filename):
        with open(filename + '.txt', 'w') as f:
            self._save_to_file_recursive(self.root, f)
    
    def _save_to_file_recursive(self, node, f):
        if not node:
            return
        for meaning in node.meanings:
            f.write(node.word + '\n')
            f.write(meaning.word_type + '\n')
            f.write(meaning.definition + '\n')
            f.write(meaning.example + '\n')
        self._save_to_file_recursive(node.left, f)
        self._save_to_file_recursive(node.right, f)

    def _read_from_file_recursive(self, f):
        node = None
        while True:
            word = f.readline().strip()
            if not word:
                break
            word_type = f.readline().strip()
            definition = f.readline().strip()
            example = f.readline().strip()
            meaning = Meaning(word_type, definition, example)
            if not node:
                node = TreeNode(word)
            node.meanings.append(meaning)
        return node

    def read_from_file(self, filename):
        with open(filename + '.txt', 'r') as f:
            self.root = self._read_from_file_recursive(f)

def main():
    dictionary = EnglishDictionary()

    while True:
        print("\nMENU:")
        print("1. Thêm một mục từ mới")
        print("2. Loại bỏ một mục từ")
        print("3. Tra cứu các nghĩa của một mục từ")
        print("4. Lưu từ điển vào các tập tin")
        print("5. Nạp từ điển từ các tập tin")
        print("6. Kết thúc chương trình")

        choice = input("Lựa chọn của bạn: ")

        if choice == '1':
            word = input("Nhập từ mới: ")
            word_type = input("Nhập loại từ: ")
            definition = input("Nhập nghĩa: ")
            example = input("Nhập ví dụ: ")
            meaning = Meaning(word_type, definition, example)
            dictionary.insert(word, meaning)
        elif choice == '2':
            word = input("Nhập từ muốn loại bỏ: ")
            if dictionary.remove(word):
                print(f"Từ '{word}' đã được loại bỏ khỏi từ điển.")
            else:
                print(f"Từ '{word}' không tồn tại trong từ điển.")
        elif choice == '3':
            word = input("Nhập từ muốn tra cứu: ")
            meanings = dictionary.search(word)
            if meanings:
                print(f"Nghĩa của từ {word}:")
                for meaning in meanings:
                    print(f"Loại từ: {meaning.word_type}")
                    print(f"Định nghĩa: {meaning.definition}")
                    print(f"Ví dụ: {meaning.example}")
            else:
                print(f"Từ '{word}' không tồn tại trong từ điển.")
        elif choice == '4':
            filename = input("Nhập tên tập tin để lưu từ điển: ")
            dictionary.save_to_file(filename)
            print(f"Từ điển đã được lưu vào tập tin '{filename}.txt'.")
        elif choice == '5':
            filename = input("Nhập tên tập tin để nạp từ điển: ")
            dictionary.read_from_file(filename)
            print(f"Từ điển đã được nạp từ tập tin '{filename}.txt'.")
        elif choice == '6':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main()
