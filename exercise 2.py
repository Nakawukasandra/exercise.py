#write a python function to find the maximum of three numbers
#a=70, b=80, c=63
def maximumvalue(a,b,c):
    if a>b and a>c:
        print(f"{a} is greaterthan {b}and{c}")
    elif b>c and b>c:
        print(f"{b} is greaterthan {a}and{c}")
    else:
        print(f"{c} is greaterthan{a}and{b}")
        maximumvalue(70,80,63)

#write a python function to multiply all numbers in alist[8,2,3,-1,7]
def product_of_all_list_numbers(a,b,c,d,e):
    output=[a*b*c*d*e]
    print(output)
product_of_all_list_numbers(8,2,3,-1,7)

#write apython program to reverse a string 1,2,3,4,a,b,c,d
def my_string(str):
    str="1234abcd"
    reversed_string=(str)
    for i in reversed(str):
        print(i)
my_string("1234abcd")

#write a python program to print the even number in a given list[1,2,3,4,5,6,7,8,9]
def even_number_in_list(a,b,c,d,e,f,g,j,k):
    even_list =[b,d,f,j]
    print(even_list)
even_number_in_list(1,2,3,4,5,6,7,8,9)



