# Last updated: 8/11/2026, 6:35:51 PM
class Solution(object):
    def capitalizeTitle(self, title):
        cstr=""
        for i in title.split(" "):
            if len(i)>2:
                cstr=cstr+i.capitalize() +" "
            else:
                cstr=cstr+i.lower() +" "
        return cstr.strip()