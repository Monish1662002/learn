# sets
s = {}
type(s)  # dict

s = set()
type(s)  # set

# non empty set
s = {1, 2, 3, 1, 2, 4, 5, 1}
print(s)  # {1, 2, 3, 4, 5}

s = set([1, 2, 3, 1, 2, 4, 5, 1])
print(s)  # {1, 2, 3, 4, 5}

s = "Monish"
s = set(s)
print(s)  # {'M', 'o', 'n', 'i', 's', 'h'}

s1 = set("Monish")
print(s)  # {'M', 'o', 'n', 'i', 's', 'h'}


#iteration
# s1[0]  # TypeError: 'set' object is not subscriptable
for i in s1:
    print(i) # M o n i s h (Any order)

len(s1)  # 6

# add
s1.add("A")
print(s1)  # {'M', 'o', 'n', 'i', 's', 'h', 'A'}    

#update
s1.update("B", "C")
print(s1)  # {'M', 'o', 'n', 'i', 's', 'h', 'A', 'B', 'C'}
s1.update("ram")
print(s1)  # {'M', 'o', 'n', 'i', 's', 'h', 'A', 'B', 'C', 'r', 'a', 'm'}
s1.update("Babu", "Cinnu")
print(s1)  # {'M', 'o', 'n', 'i', 's', 'h', 'A', 'B', 'C', 'r', 'a', 'm', 'b', 'u', 'c', 'i'}
s1.update(["somu", "jinnu"])
print(s1)  # {'b', 'n', 'h', 'i', 'C', 'A', 'o', 'B', 'somu', 'a', 'u', 'm', 's', 'r', 'M', 'jinnu'}

# pop
print(s1.pop())
# print(s1.pop('s')) #->TypeError: set.pop() takes no arguments (1 given)
print(s1)

print(s1.remove('n'))
print(s1) #{'u', 's', 'B', 'A', 'b', 'C', 'jinnu', 'm', 'i', 'a', 'r', 'somu', 'h', 'o'}