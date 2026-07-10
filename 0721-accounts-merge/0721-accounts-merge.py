class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        email_to_name={}
        connected_mails=defaultdict(set)
        visited=set()
        n=len(accounts)
        for i in range(n):
            name=accounts[i][0]
            email1=accounts[i][1]
            for j in range(2,len(accounts[i])):
                email_to_name[accounts[i][j]]=name
                connected_mails[email1].add(accounts[i][j])
                connected_mails[accounts[i][j]].add(email1)
            email_to_name[email1]=name
        def dfs(email,connected):
            visited.add(email)
            connected.append(email)
            for neigh in connected_mails[email]:
                if neigh not in visited:
                    dfs(neigh,connected)
        result=[]
        for email in email_to_name:
            if email not in visited:
                connected=[]
                dfs(email,connected)
                result.append([email_to_name[email]]+sorted(connected))
        return result