import time
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
wordDict = Trie()
import tracemalloc
tracemalloc.start()
common_words = {"a","'s","i","am","an","as","at",
                "be","by","do","go", "he","et"
                "if","in","is","it","me",
                "my","no","of","on","or",
                "so","to","up","us","we","dr",
                "st","nd","rd","s","misérables","villermé’s","de l’état","employés"}
start_trie = time.perf_counter()
for k in common_words :
    wordDict.insert(k)
with open('words_alpha.txt', 'r') as file:
    for line in file:
        word = line.strip().lower()
        if len(word) > 2 :
            wordDict.insert(word)
end_trie = time.perf_counter()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Current memory usage: {current / (1024 ** 2):.2f} MB")
print(f"Peak memory usage: {peak / (1024 ** 2):.2f} MB")
print(f"Initial dictionary construction time: {end_trie - start_trie:.6f} seconds")
def search(word):
    if len(word)== 1 and word.isalpha() == False :
        return 1
    elif wordDict.search(word) == 1 :
        return 1
    else :
        return 0

a = input("enter a string")
start_seg = time.perf_counter()
s = a.lower()
n = len(s)
from array import array
dp = array('i', [0] * (n + 1))
dp[0]=1
for i in range (n+1):
    for j in range(max(0,i-30),i):
        if dp[j] == 1 and search(s[j:i])==1 :
            dp[i]=1
            break
end_seg = time.perf_counter()

if dp[-1]==1:
    print("Yes, The string can be segmented into meaningful words")
else:
    print("No, The string cannot be segmented into meaningful words")
print(f"Word segmentation time: {end_seg - start_seg:.6f} seconds")
