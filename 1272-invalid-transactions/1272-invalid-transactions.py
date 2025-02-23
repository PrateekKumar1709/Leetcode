class Transaction:
    def __init__(self, transaction_str, index):
        name, time, amount, city = transaction_str.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        self.index = index
        self.is_invalid = False
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # If empty input, return empty list
        if not transactions:
            return []
        
        # Parse transactions
        parsed_transactions = []
        for i, t in enumerate(transactions):
            parsed_transactions.append(Transaction(t, i))
        
        # Group by name
        trans_by_name = {}
        for t in parsed_transactions:
            if t.name not in trans_by_name:
                trans_by_name[t.name] = []
            trans_by_name[t.name].append(t)
        
        # Check for invalid transactions
        invalid_indices = set()
        
        for name, trans_list in trans_by_name.items():
            # Sort by time for efficient comparison
            trans_list.sort(key=lambda x: x.time)
            
            # Check each transaction
            for i, t1 in enumerate(trans_list):
                # Check amount constraint
                if t1.amount > 1000:
                    invalid_indices.add(t1.index)
                
                # Check time and city constraint
                for j in range(len(trans_list)):
                    if i != j:
                        t2 = trans_list[j]
                        if abs(t1.time - t2.time) <= 60 and t1.city != t2.city:
                            invalid_indices.add(t1.index)
                            invalid_indices.add(t2.index)
        
        # Return invalid transactions in original order
        return [transactions[i] for i in invalid_indices]
