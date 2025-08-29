## Note:
* print function has default seperator as space=" "
* and End has="\n" for moves to the next Line
* To change the seperator "Use sep=" "(operator) value"
* also supports sep="\n" to give the things row by row or line by line
* * To change the end "Use end=" "(operator),end="->" value"

 # single value
> print("Hello world!")
__output:Hello world!__

# multiple values
> print("Raman","Flower",23,1.05,"12",'susee','0.23') 
__output:Raman Flower 23 1.05 12 susee 0.23__

# Seperators
> print("Raman","Flower",sep='-') # separator
__output:Raman-Flower__

> print("Raman","Flower",sep='') # no space
__output:Raman Flower__

# Concatenation
> print("Raman"+"Flower") # concatenation
__output:RamanFlower__
* No Default Seperator

# Seperator ANd End
>print("Raman",24,sep='\n',end="->") # mixed values
print("abc",24)
__output:Raman__
__24->abc 24__