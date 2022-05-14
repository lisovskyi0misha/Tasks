class WordEditor():
    def __init__(self, word):
        self.word = word
        self.list = [',', '(', ')', '/', '!', '?', '.']

    def clean(self):
        for i in self.word:
            if i in self.list:
                self.word = self.word.replace(i, '')
        return self.word


class DictSort():
    def __init__(self, dict):
        self.dict = dict

    def dict_sort(self):
        sorted_dict = sorted(self.dict.values(), reverse=True)
        final_dict = {}
        for i in sorted_dict:
            for obj in self.dict.keys():
                if self.dict[obj] == i:
                    final_dict[obj] = i
            # print(i)
            # final_dict[i] = self.dict[i]
        return final_dict
