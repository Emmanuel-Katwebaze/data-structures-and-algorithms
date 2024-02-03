class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

# Time complexity - O(1)
# Space complexity - O(1)        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Time complexity - O(m) m is the number of characters to insert
    # Space complexity - O(m)    
    def insertString(self, word):
        current = self.root
        for i in word:
            ch = i
            # if it exists in the dictionary
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted") 
    
    # Time complexity - O(m) m is the number of characters to insert
    # Space complexity - O(1)     
    def searchString(self, word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endOfString == True:
            return True
        else:
            return False
        
def deleteString(root, word, index): # index is index of characters in the word
    ch = word[index]
    currentNode = root.children.get(ch)
    canThisNodeBeDeleted = False
    
    # Case 1: Some other prefix of string is same as the one that we want to delete. (API, APPLE)    
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index+1)
        return False
    
    # Case 2: The string is a prefix of another string. (API, APIS)
    if index == len(word) - 1:
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False    
        else:
            root.children.pop(ch)
            return True
        
    # Case 3: Other string is a prefix of this string. (APIS, AP)
    if currentNode.endOfString == True:
        deleteString(currentNode, word, index+1)
        return False
    
    canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
    
    # Case 4: Not any node depends on this String (K)
    if canThisNodeBeDeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
        
        

newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Apl")

print(" *** SEARCH STRING ***")
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))
print(newTrie.searchString("DCD"))

print(" *** DELETE STRING ***")
deleteString(newTrie, "App", 0)
print(newTrie.searchString("App"))