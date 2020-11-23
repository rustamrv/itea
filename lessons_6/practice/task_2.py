
class MyDict:

    def __init__(self, my_dict=dict()):
        self.my_dict = my_dict 

    def get(self, key):
        return self.my_dict[key]

    def insert(self, key, value):
        self.my_dict[key] = value

    def keys(self):
        return self.my_dict.keys()

    def values(self):
        return self.my_dict.values()

    def add_new_dict(self, dict_new):
        return MyDict(self.my_dict.update(dict_new))



mydict = MyDict() 
mydict.insert('x', 1)
mydict.insert('y', 2)
mydict.insert('z', 3)
print(mydict.my_dict)
print(mydict.get('x'))
print(mydict.get('xx'))