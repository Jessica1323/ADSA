class HashTable:
    def __init__(self):
        self.size = 26  
        self.table = [None] * self.size  
        self.tombstone = "TOMBSTONE"  

    def char_to_index(self, char):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(alphabet)):
            if alphabet[i] == char:
                return i
        return -1  

    def hash_function(self, key):
        return self.char_to_index(key[-1])  

    def search(self, key):
        index = self.hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key: 
                return index
            index = (index + 1) % self.size
            if index == original_index:  
                break
        return -1  

    def insert(self, key):
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None and self.table[index] != self.tombstone:
            if self.table[index] == key:  
                return
            index = (index + 1) % self.size
            if index == original_index:  
                return

        
        self.table[index] = key

    def delete(self, key):
        index = self.search(key)
        if index != -1:
            self.table[index] = self.tombstone  

    def output(self):
        return [key for key in self.table if key is not None and key != self.tombstone]


def main():
    hash_table = HashTable()

    
    input_commands = input().split()
    
    for command in input_commands:
        operation = command[0]
        word = command[1:]

        if operation == 'A':  
            hash_table.insert(word)
        elif operation == 'D': 
            hash_table.delete(word)

    print(" ".join(hash_table.output()))

if __name__ == "__main__":
    main()
