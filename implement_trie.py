from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.is_word=False
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current=self.root
        for letter in word:
            current=current.children[letter]
        #在最后一个字母的位置，is_word变为True
        current.is_word=True          

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current=self.root
        for letter in word:
            current=current.children.get(letter)
            #如果不存在这个键
            if current==None:
                return False
        #如果不是一个完整的单词，那么也是返回False,比如，树中存在"abc"但是word="ab"的情况
        return current.is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current=self.root
        for letter in prefix:
            current=current.children.get(letter)
            if current==None:
                return False
        return True
