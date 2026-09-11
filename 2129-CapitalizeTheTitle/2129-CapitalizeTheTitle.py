# Last updated: 9/11/2026, 9:30:27 AM
class Solution(object):
    def capitalizeTitle(self, title):
        cstr=""
        for i in title.split(" "):
            if len(i)>2:
                cstr=cstr+i.capitalize() +" "
            else:
                cstr=cstr+i.lower() +" "
        return cstr.strip()