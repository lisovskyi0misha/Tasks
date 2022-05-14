from classes import WordEditor
from classes import DictSort


text = input('Write your text here: ')


new_list = []
list = text.split()
for word in list:
    word = word.lower()
    obj = WordEditor(word)
    new_list.append(obj.clean())
dict = {}
for word in new_list:
    dict[word] = new_list.count(word)
obj = DictSort(dict)
final = obj.dict_sort()


n = 0
result = []
if len(final.values()) < 3:
    pass
else:
    for i in final:
        if n == 3:
            break
        else:
            result.append(i)
            n += 1
print(result)
