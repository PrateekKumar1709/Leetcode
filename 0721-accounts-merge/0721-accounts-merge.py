class UnionFind:
    def __init__(self):
        # Initialize empty parent dictionary
        self.parent = {}
    
    def find(self, x):
        # If x is not in parent, add it as its own parent
        if x not in self.parent:
            self.parent[x] = x
        # Path compression: make all nodes point directly to root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        # Union by setting parent of one's root to other's root
        self.parent[self.find(x)] = self.find(y)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Initialize UnionFind data structure
        uf = UnionFind()
        
        # Map email to account name
        email_to_name = {}
        
        # Process each account
        for account in accounts:
            name = account[0]
            # Union all emails in the account
            for email in account[1:]:
                email_to_name[email] = name
                if len(account) > 2:  # If account has multiple emails
                    uf.union(account[1], email)
        
        # Group emails by their parent in UnionFind
        components = {}
        for email in email_to_name:
            parent = uf.find(email)
            if parent not in components:
                components[parent] = []
            components[parent].append(email)
        
        # Format result
        result = []
        for emails in components.values():
            # Sort emails and add name at beginning
            name = email_to_name[emails[0]]
            result.append([name] + sorted(emails))
        
        return result