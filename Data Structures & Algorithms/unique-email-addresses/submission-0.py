class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uni = set()
        for e in emails:
            local , domain = e.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            uni.add((local,domain))
        return len(uni)