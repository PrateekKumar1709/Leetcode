from collections import Counter
class Solution:
    def minimumKeypresses(self, s: str) -> int:
        """
        Calculates the minimum number of keypresses needed to type a string 's' using a 9-button keypad.

        Args:
            s (str): The input string containing lowercase English letters.

        Returns:
            int: The minimum number of keypresses required.
        """

        # 1. Count character frequencies using Counter.  This gives us a dictionary-like object
        # where each character is a key and its frequency in 's' is the value.  O(n) time complexity.
        char_counts = Counter(s)

        # 2. Sort the character frequencies in descending order.  We convert the Counter object
        # to a list of (character, count) tuples and then sort it based on the count in reverse order.
        # O(k log k) where k is the number of unique characters in s (at most 26).
        sorted_counts = sorted(char_counts.items(), key=lambda item: item[1], reverse=True)

        # 3. Calculate the total keypresses.  We iterate through the sorted character counts and
        # assign keypresses based on the character's position in the sorted list.
        # The first 9 characters require 1 press, the next 9 require 2, and the remaining require 3.
        # O(k) where k is the number of unique characters in s (at most 26).
        total_presses = 0
        for i, (char, count) in enumerate(sorted_counts):
            if i < 9:
                total_presses += count * 1
            elif i < 18:
                total_presses += count * 2
            else:
                total_presses += count * 3

        return total_presses


