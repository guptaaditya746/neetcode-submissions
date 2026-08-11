class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        def _filter(email: str) -> str:
            user_name, domain = email.split('@')

            user_name = user_name.split('+')[0]
            user_name = user_name.replace('.', '')

            return user_name + '@' + domain

        unique_emails = set()

        for email in emails:
            unique_emails.add(_filter(email))

        return len(unique_emails)