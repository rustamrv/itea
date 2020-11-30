
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

    def __add__(self, other):
        return MyList(self.my_list + other.my_list)

    def add(self, x):
        self.my_list[len(self.my_list):] = [x]

    def insert(self, ind, x):
        if len(self.my_list) <= ind:
            self.add(x)
        else:
           self.my_list[ind] = x

    def remove(self, x):
        if x in self.my_list:
            self.my_list = [i for i in self.my_list if x!=i] 
        else:
            raise ValueError(f'{x} not in list')

    def clear(self):
        self.my_list = []
    
    def pop(self, x=None):
        if x == None: 
            last = self.my_list[len(self.my_list)-1:][0] 
            self.remove(last)
            return last
        self.remove(x)
        return x 


mylist = MyList()
mylist.add(5)
mylist.add(1)
mylist.add(2)
mylist.add(34)
print(mylist.my_list)
# mylist.remove(34)
# print(mylist.my_list) 
# mylist.insert(0, 21)
# print(mylist.my_list)
  
print(mylist.pop(5))
print(mylist.my_list)

# print(mylist.pop(0))
# print(mylist.my_list)
# for i in mylist:
#     print(i)

array = MyList([122,4,4,5,6,])

new_list = mylist + array
<<<<<<< HEAD
print(new_list.my_list)
=======
print(new_list.my_list)
>>>>>>> 37e92b13533a31b93b3fff00a339876955a86841
