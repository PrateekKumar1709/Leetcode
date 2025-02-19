class TextEditor:
    def __init__(self):
        # Initialize two empty strings to store text before and after cursor
        self.left = []   # characters to left of cursor
        self.right = []  # characters to right of cursor
    
    def addText(self, text: str) -> None:
        # Add each character to the left of cursor
        for char in text:
            self.left.append(char)
    
    def deleteText(self, k: int) -> int:
        # Delete k characters to the left of cursor
        # Return actual number of characters deleted
        delete_count = min(k, len(self.left))
        for _ in range(delete_count):
            self.left.pop()
        return delete_count
    
    def cursorLeft(self, k: int) -> str:
        # Move cursor left by k positions
        move_count = min(k, len(self.left))
        for _ in range(move_count):
            self.right.append(self.left.pop())
        # Return last min(10, len) characters to left of cursor
        return self._getLeftString()
    
    def cursorRight(self, k: int) -> str:
        # Move cursor right by k positions
        move_count = min(k, len(self.right))
        for _ in range(move_count):
            self.left.append(self.right.pop())
        # Return last min(10, len) characters to left of cursor
        return self._getLeftString()
    
    def _getLeftString(self) -> str:
        # Helper method to get last 10 characters to left of cursor
        start = max(0, len(self.left) - 10)
        return ''.join(self.left[start:])