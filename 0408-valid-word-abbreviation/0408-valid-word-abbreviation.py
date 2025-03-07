class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # Initialize pointers for word and abbreviation
        word_index = 0
        abbr_index = 0
        
        # Loop through the characters in the word
        while word_index < len(word):
            # Check if abbreviation index has become out of bounds
            if abbr_index >= len(abbr):
                return False
            
            # If current characters match, move to the next ones
            if word[word_index] == abbr[abbr_index]:
                word_index += 1
                abbr_index += 1
                continue
            
            # Check if abbreviation character is a digit
            if not abbr[abbr_index].isdigit():
                return False
            
            # Calculate the number representing the skipped characters
            num_start_index = abbr_index
            while abbr_index < len(abbr) and abbr[abbr_index].isdigit():
                abbr_index += 1
            num_str = abbr[num_start_index:abbr_index]
            
            # Leading zero or invalid number check
            if num_str == '0' or num_str.startswith('0'):
                return False
            
            # Move the word index forward by the number of skipped characters
            word_index += int(num_str)
        
        # If we've reached the end of both the word and the abbreviation, the abbreviation is valid
        return word_index == len(word) and abbr_index == len(abbr)
