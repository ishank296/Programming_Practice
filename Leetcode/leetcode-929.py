# unique email addresses
# email address consists of two parts local name and domain name
# Given list of email addresses find then unique email addresses
# condition : if period(.) is present in local name, then it will be same as email
# without period in local name
# If + symbol is present in local name, then anything after + will be ignored in local name

class Solution:

    def numuniqueemails(self,emails: list[str]):
        res= set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:email.index('+')]
            local = local.replace(r'.', '')
            res.add(f'{local}@{domain}')
        return res


if __name__ == '__main__':
    s = Solution()
    emails = ['test.email+alice@leetcode.com',
              'test.e.mail+bob@leetcode.com',
              'testemail+david@lee.tcode.com']
    print(s.numuniqueemails(emails))