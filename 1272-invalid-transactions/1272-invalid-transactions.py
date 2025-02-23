class Transaction:
    def __init__(self, transaction_str, index):
        # Parse transaction string and store original index
        name, time, amount, city = transaction_str.split(',')
        self.name = name
        self.time = int(time)
        self.amount = int(amount)
        self.city = city
        self.index = index  # Store original index for reconstruction
        self.transaction_str = transaction_str
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        # Edge case: empty input
        if not transactions:
            return []
        
        # Step 1: Parse and group transactions by name
        transaction_map = {}  # name -> list of Transaction objects
        for i, trans in enumerate(transactions):
            transaction = Transaction(trans, i)
            if transaction.name not in transaction_map:
                transaction_map[transaction.name] = []
            transaction_map[transaction.name].append(transaction)
        
        # Step 2: Find invalid transactions
        invalid_set = set()  # Use set to avoid duplicates
        
        for name, trans_list in transaction_map.items():
            # Check each transaction
            for i, trans in enumerate(trans_list):
                # Rule 1: Amount exceeds $1000
                if trans.amount > 1000:
                    invalid_set.add(trans.index)
                
                # Rule 2: Check time window violations
                for j, other_trans in enumerate(trans_list):
                    if i != j and abs(trans.time - other_trans.time) <= 60 and trans.city != other_trans.city:
                        invalid_set.add(trans.index)
                        invalid_set.add(other_trans.index)
        
        # Return invalid transactions in original format
        return [transactions[i] for i in invalid_set]
