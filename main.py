class HashTable:
    def __init__(self):
        self.size = 26  # There are 26 possible slots (a-z)
        self.table = [None] * self.size  # Initialize all slots to "None"
        self.tombstone = "TOMBSTONE"  # Define a tombstone marker

    def hash_function(self, key):
        """Hash function based on the last character of the word."""
        return ord(key[-1]) - ord('a')  # Maps last character to index 0-25

    def search(self, key):
        """Search for the key and return its index, or where it can be inserted."""
        index = self.hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key:  # Key found
                return index
            index = (index + 1) % self.size
            if index == original_index:  # Full cycle, key not found
                break
        return -1  # Key not found

    def insert(self, key):
        """Insert the key if it does not exist."""
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None and self.table[index] != self.tombstone:
            if self.table[index] == key:  # Key already exists
                return
            index = (index + 1) % self.size
            if index == original_index:  # Full cycle, table full
                return

        # Insert the key in the first available slot
        self.table[index] = key

    def delete(self, key):
        """Delete the key if it exists."""
        index = self.search(key)
        if index != -1:
            self.table[index] = self.tombstone  # Mark slot as "TOMBSTONE"

    def output(self):
        """Output the non-empty slots (ignoring tombstones)."""
        return [key for key in self.table if key is not None and key != self.tombstone]

# Main input/output handling
def main():
    hash_table = HashTable()

    # Example input: "Aaaa Accc Abbb"
    input_commands = input().split()
    
    for command in input_commands:
        operation = command[0]
        word = command[1:]

        if operation == 'A':  # Insert
            hash_table.insert(word)
        elif operation == 'D':  # Delete
            hash_table.delete(word)

    # Output the current state of the hash table
    print(" ".join(hash_table.output()))

if __name__ == "__main__":
    main()
class HashTable:
    def __init__(self):
        self.size = 26  # There are 26 possible slots (a-z)
        self.table = [None] * self.size  # Initialize all slots to "None"
        self.tombstone = "TOMBSTONE"  # Define a tombstone marker

    def hash_function(self, key):
        """Hash function based on the last character of the word."""
        return ord(key[-1]) - ord('a')  # Maps last character to index 0-25

    def search(self, key):
        """Search for the key and return its index, or where it can be inserted."""
        index = self.hash_function(key)
        original_index = index
        
        while self.table[index] is not None:
            if self.table[index] == key:  # Key found
                return index
            index = (index + 1) % self.size
            if index == original_index:  # Full cycle, key not found
                break
        return -1  # Key not found

    def insert(self, key):
        """Insert the key if it does not exist."""
        index = self.hash_function(key)
        original_index = index

        while self.table[index] is not None and self.table[index] != self.tombstone:
            if self.table[index] == key:  # Key already exists
                return
            index = (index + 1) % self.size
            if index == original_index:  # Full cycle, table full
                return

        # Insert the key in the first available slot
        self.table[index] = key

    def delete(self, key):
        """Delete the key if it exists."""
        index = self.search(key)
        if index != -1:
            self.table[index] = self.tombstone  # Mark slot as "TOMBSTONE"

    def output(self):
        """Output the non-empty slots (ignoring tombstones)."""
        return [key for key in self.table if key is not None and key != self.tombstone]

# Main input/output handling
def main():
    hash_table = HashTable()

    # Example input: "Aaaa Accc Abbb"
    input_commands = input().split()
    
    for command in input_commands:
        operation = command[0]
        word = command[1:]

        if operation == 'A':  # Insert
            hash_table.insert(word)
        elif operation == 'D':  # Delete
            hash_table.delete(word)

    # Output the current state of the hash table
    print(" ".join(hash_table.output()))

if __name__ == "__main__":
    main()
