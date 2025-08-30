# TUPLE

1. tuple is similer to the list
2. Ordered collection of datas
3. unchangeable
4. iteratable
5. can be hetrogenous
   
# Why we use Tuples instead of List
1. mainly used for storing the uneditable datas like constents
   which is called as "Frozon datas"
2. indexing are used but only for the getting or showing the values 
   not for editing 
## Note: Tuples are immutable, meaning that once they are created, their elements cannot be changed, added, or removed.

**Note: [ ] is only thing which is used for indixing all list,string,tuple,etc...**
**"()" is used for creating the Tuple** 

# Error
> t4 = tuple(["Hello"],[1,2],3,"ram") 
 TypeError: tuple expected at most 1 argument, got 4

# Mutable in tuple([List]) by using List and the List's indesx tuple[][]=" "
![changing the list inside the tuple](/09_imgs/mutationtuple.png)

## Tuple Operations
1. count
2. index
3. concadination('+','*')
4. list to tuple ,tuple to list
5. iteration 
   
# Summary:
1. Tuples are similar to lists but are immutable,
    meaning their elements cannot be changed after creation,
2. Tuples are defined using parentheses (),
3. Tuples support indexing and slicing for accessing elements,
4. Tuples have methods like count() and index() for element operations,
5. Tuples can be concatenated and multiplied to create new tuples,
6. Tuples can contain elements of different data types,
7. Tuples are often used for fixed collections of related data,
8. Tuples are more memory efficient than lists,
9. Tuples can be used as keys in dictionaries due to their immutability,
10. Tuples support unpacking for assigning elements to variables.
11. Element addition is possible by concatenation
12. Tuples can contain mutable elements like lists, allowing modification of those elements even though the tuple itself is immutable. 