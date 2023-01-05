class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        filteredEmails = set()
        filteredEmail = ""
        
        for email in emails:
            
            for c in email:
                
                if c == ".":
                    continue;
                
                elif c == "+":
                    break;
                    
                elif c == "@":
                    break;
                
                else:
                    filteredEmail += c
            
            
            filteredEmail += "@" + email.split("@")[1]
            filteredEmails.add(filteredEmail)
            filteredEmail = ""
        
        #print(filteredEmails)
        return len(filteredEmails)