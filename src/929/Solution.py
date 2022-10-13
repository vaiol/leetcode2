class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parseEmail(email: str) -> str:
            local, domain = email.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            return f'{local}@{domain}'
        
        unique_emails = set()
        for email in emails:
            unique_emails.add(parseEmail(email))
        return len(unique_emails)
        