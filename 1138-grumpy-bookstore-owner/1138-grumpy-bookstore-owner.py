class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        
        # First calculate base satisfaction (when owner is not grumpy)
        base_satisfied = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfied += customers[i]
        
        # Calculate initial window of additional satisfied customers
        window_satisfied = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                window_satisfied += customers[i]
        
        # Initialize max_additional with initial window
        max_additional = window_satisfied
        
        # Slide the window
        for i in range(minutes, n):
            # Remove leftmost customer from window if owner was grumpy
            if grumpy[i - minutes] == 1:
                window_satisfied -= customers[i - minutes]
            # Add rightmost customer to window if owner was grumpy
            if grumpy[i] == 1:
                window_satisfied += customers[i]
            # Update maximum additional satisfied customers
            max_additional = max(max_additional, window_satisfied)
        
        return base_satisfied + max_additional
