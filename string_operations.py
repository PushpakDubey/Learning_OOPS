
class StringOperations:
    def __init__(self):
        self.s = "This world is awesome and has 7 wonders"
    def reverse_string(self):

        s = list(self.s)
        l = len(s)
        start, end = 0, l-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1
        print("".join(s))

    def duplicate_alphabet(self):
        s = self.s.lower()
        count = {}
        numbers = [char for char in s if char.isnumeric()]
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        duplicate = [char for char in count if count[char] > 1]
        print(duplicate, numbers)


a = StringOperations()
a.reverse_string()
a.duplicate_alphabet()

