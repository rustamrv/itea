
class MyList:

    def __init__(self, array=[]):
        self.my_list = array
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < len(self.my_list): 
            x = self.my_list[self.count]
            self.count +=1
            return x
        raise StopIteration

    def add(self, x):
        self.my_list.append(x)

    def insert(self, ind, x):
        if len(self.my_list) <= ind:
            self.add(x)
        else:
           self.my_list[ind] = x

    def remove(self, x):
        if x in self.my_list:
            self.my_list.remove(x)
        else:
            raise ValueError(f'{x} not in list')

    def clear(self):
        self.my_list.clear()
    
    def pop(self, x=None):
        if x == None:
           return self.my_list.pop()
        return self.my_list.pop(x)

    def add_new_list(self, array):
        return MyList(self.my_list+array)



mylist = MyList()
mylist.add(5)
mylist.add(1)
mylist.add(2)
mylist.add(34)
print(mylist.my_list)
mylist.insert(3, 6)
print(mylist.my_list)
mylist.insert(4, 6)
print(mylist.my_list)
mylist.insert(0, 21)
print(mylist.my_list)
  
print(mylist.pop())
print(mylist.my_list)

print(mylist.pop(0))
print(mylist.my_list)
for i in mylist:
    print(i)

new_list = mylist.add_new_list([122,4,4,5,6,])
print(new_list.my_list)