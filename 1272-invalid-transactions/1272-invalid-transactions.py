class Transaction:
    def __init__(self, transaction_str, index):
        name, time, amount, city = transaction_str.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        self.index = index
        self.transaction_str = transaction_str
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        if not transactions:
            return []
        
        # Step 1: Parse transactions and group by name
        transaction_map = {}
        for i, trans in enumerate(transactions):
            t = Transaction(trans, i)
            if t.name not in transaction_map:
                transaction_map[t.name] = []
            transaction_map[t.name].append(t)
        
        invalid_set = set()
        
        # Step 2: Process each name group
        for name, trans_list in transaction_map.items():
            # Sort transactions by time for sliding window
            trans_list.sort(key=lambda x: x.time)
            
            # Use sliding window to check time violations
            left = 0
            for right in range(len(trans_list)):
                # Check amount violation
                if trans_list[right].amount > 1000:
                    invalid_set.add(trans_list[right].index)
                
                # Slide left pointer while maintaining 60-minute window
                while left < right and trans_list[right].time - trans_list[left].time > 60:
                    left += 1
                
                # Check all transactions in current window for city violations
                for i in range(left, right + 1):
                    if i != right and trans_list[i].city != trans_list[right].city:
                        invalid_set.add(trans_list[i].index)
                        invalid_set.add(trans_list[right].index)
        
        return [transactions[i] for i in invalid_set]
