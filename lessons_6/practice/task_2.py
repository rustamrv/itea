
class MyDict:

    def __init__(self, my_dict=dict()):
        self.my_dict = my_dict 

    def get(self, key):
        return self.my_dict[key]

    def __add__(self, other): 
        new = dict() 
        for i in self.my_dict:
            new[i] = self.my_dict[i] 
        for i in other.my_dict:
            new[i] = other.my_dict[i]  
        return MyDict(new)

    def insert(self, key, value):
        self.my_dict[key] = value

    def keys(self):  
        return [k for k in self.my_dict]

    def values(self): 
        return [self.my_dict[k] for k in self.my_dict]


if __name__ == "__main__":

    first_dict = MyDict() 
    first_dict.insert('x', 1)
    first_dict.insert('y', 2)
    first_dict.insert('z', 3) 
    print(first_dict.my_dict, 'first dict') 
    second_dict = MyDict() 
    second_dict.insert('q', 4)
    # second_dict.insert('a', 3)
    # second_dict.insert('c', 35)  
    print(second_dict.my_dict, 'error second dict')  
    new = second_dict + first_dict
    print(new.my_dict, 'new')
    print(first_dict.my_dict, 'old')

    print(first_dict.values())
<<<<<<< HEAD
    print(first_dict.keys())
=======
    print(first_dict.keys())
>>>>>>> 37e92b13533a31b93b3fff00a339876955a86841
