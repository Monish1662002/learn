#sinlgle line string
str1="Apple"#normal string
str2="123"#string with numbers
str3="Hello@123"#string with special characters 
type(str1)

# single line string for printing multiple lines
print("This is line 1.\nThis is line 2.\nThis is line 3.")

#miltiple line string
str4="""This is a  
multiline string
example"""
multiline_string = """This is the first line.
This is the second line.
    This line is indented.
"""
print(multiline_string)

#if multiline string is packed in single or double quotes it will give error
#str5='''This is a  
#multiline string
#example'''-> valid
#str6="This is a    
#multiline string
#example"-> syntax error

# ord() and chr() functions
#ord() function returns the Unicode code point for a given character.
char = 'A'
unicode = ord('A')
# Output: 65
unicode = ord("Z")
# Output: 90
unicode = ord("a")
# Output: 97
unicode = ord("z")     
# Output: 122
unicode = ord("0")  
# Output: 48
unicode = ord("9")
# Output: 57
unicode = ord("@")  
# Output: 64

#chr() function returns the character that corresponds to a given Unicode code point.
char = chr(65)  
# Output: 'A'
char = chr(90)  
# Output: 'Z'
char = chr(97) 
# Output: 'a'
char = chr(122)
# Output: 'z'
char = chr(48)
# Output: '0'
char = chr(57)
# Output: '9'
char = chr(64)
# Output: '@'
char = chr(8364)
# Output: '€' (Euro sign)
char = chr(128512)
# Output: '😀' (Grinning Face emoji)

# indexing and slicing
str5="Hello, World!"
#index of H: 0
#index of e: 1
#index of l: 2
#index of o: 4
#index of ,: 5
#index of  : 6
#index of W: 7
#index of r: 8
#index of d: 10
#index of !: 12
first_char = str5[0]  # 'H' from start ,from start 0 is the begining index
last_char = str5[-1]  # '!' from end,but in end -1 is the begining index
substring = str5[0:5]  # 'Hello' from index 0 to 4,5th index not included
substring2 = str5[7:]  # 'World!' from index 7 to end ,7th index also included
substring3 = str5[:5]  # 'Hello' from start to index 4,5th index not included
substring4 = str5[-6:-1]  # 'World' from index -6 to -2,-1th index not included
substring5 = str5[-6:]  # 'World!' from index -6 to end,-6th index also included  
#jumping index
substring6 = str5[0:12:2]  # 'Hlo ol!' from index 0 to 11 with a step of 2
substring7 = str5[::3]  # 'Hl r!' from start to end with a step of 3
substring8 = str5[:] # 'Hello, World!' from start to end
substring = str5[::] # 'Hello, World!' from start to end
substring9 = str5[::-1] # '!dlroW ,olleH' from end to start with a step of -1 (reversing the string) 

substring10 = str5[1:-2:-1] #output: '' empty string,as -2 is before 1 and step is -1
substring11 = str5[-1:0] #output: '' empty string,as 0 is before -1 and step is +1 by default
substring12 = str5[-1:0:-1] #output: '!dlroW ,olle' from end to start with a step of -1 (reversing the string) ,0th index not included
#length of string
str1="Hello"
size=len(str1)# len function to get length of string #output: 5,length is counted from 1
name="Hello"
print(name[-size]) #output: H
print(name[size-1]) #output: o
name[-1:(len(name)+1):-1] #output: 'olleH' ,reversing the whole string using len function
