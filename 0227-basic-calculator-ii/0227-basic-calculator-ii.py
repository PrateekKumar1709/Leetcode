class Solution:
    def calculate(self, s: str) -> int:
        # Check for empty string
        if not s:
            return 0
        
        # Initialize variables
        currentNumber = 0  # Current number being processed
        lastNumber = 0    # Last number after applying operation
        result = 0        # Running result
        sign = '+'       # Current operation sign
        
        # Process each character
        for i in range(len(s)):
            currentChar = s[i]
            
            # If current character is digit, build number
            if currentChar.isdigit():
                currentNumber = (currentNumber * 10) + int(currentChar)
            
            # If current character is operator or last character, process operation
            if (not currentChar.isdigit() and not currentChar.isspace()) or i == len(s) - 1:
                # Process based on previous sign
                if sign == '+' or sign == '-':
                    result += lastNumber
                    lastNumber = currentNumber if sign == '+' else -currentNumber
                elif sign == '*':
                    lastNumber = lastNumber * currentNumber
                elif sign == '/':
                    # Handle division (ensure integer division matches C++)
                    lastNumber = int(lastNumber / currentNumber)
                
                # Update sign and reset currentNumber
                sign = currentChar
                currentNumber = 0
        
        # Add final number
        result += lastNumber
        return result