class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_ = []
        s = title.lower()
        string_list = s.split()
        for i in string_list:
            if len(i) <= 2:
                title_.append(i)
            else:
                title_.append(i.capitalize())
        return ' '.join(title_)