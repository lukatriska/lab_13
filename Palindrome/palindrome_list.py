# Implementation of the Palindrome ADT using a singly linked list.

class Palindrome :
    # Creates an empty stack.
    def __init__( self ):
        self._top = None
        self._size = 0

    # Returns True if the stack is empty or False otherwise.
    def isEmpty( self ):
        return self._top is None

    # Returns the number of items in the stack.
    def __len__( self ):
        return self._size

    # Returns the top item on the stack without removing it.
    def peek( self ):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    # Removes and returns the top item on the stack.
    def pop( self ):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self._top = self._top.next
        self._size -= 1
        return node.item

    # Pushes an item onto the top of the stack.
    def push( self, item ) :
        self._top = _StackNode( item, self. _top )
        self._size += 1

    # Reads the dictionary from the given file
    def read_dict(self, file):
        """
        :param name: name of file (e. g. "file.txt")
        :type file: str
        """
        with open(file, 'r', encoding="utf8") as dictio:
            words = dictio.readlines()
            for i in range(len(words)): # deletes all the unknown symbols and pushes all words into this stack
                words[i] = words[i].split()[0]
                self.push(words[i])

    # Deletes all words from this stack and adds only polindromes
    def find_palindromes(self):
        curNode = self._top
        lst = []
        while curNode is not None:
            rev = "".join(reversed(list(curNode.item)))
            if rev == curNode.item:
                lst.append(curNode.item)
            self.pop()
            curNode = curNode.next
        for poli in lst:
            self.push(poli)

    # Write the words (polindromes if find_polindromes has been executed) to the given file
    def to_file(self, name):
        """
        :param name: name of file (e. g. "file.txt")
        :type name: str
        :return: None
        """
        curNode = self._top
        with open(name, 'w', encoding="utf8") as file:
            while curNode is not None:
                file.write(curNode.item)
                file.write('\n')
                curNode = curNode.next

        # def traverse(self):
    #     curNode = self._top
    #     while curNode is not None:
    #         print(curNode.item)
    #         curNode = curNode.next


# The private storage class for creating stack nodes.
class _StackNode :
    def __init__( self, item, link ) :
        self.item = item
        self.next = link