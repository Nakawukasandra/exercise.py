#write a python program that counts the total number of even and odd number in this tuple
def count_even_and_odd_numbers(numbers_tuple):
    even_count = 0
    odd_count = 0
    for x in numbers_tuple:
        if x % 2 ==0:
            even_count += 1
        else:
         odd_count += 1
numbers = (1,2,3,4,5,6,7,8,9)
even_count = (2,4,6,8)
odd_count =(1,3,5,9)
print("even_numbers{even_count} and {odd_count}")

#create aprogram that returns the output of the multiple of seven and multiples of five.
#ultiple_of_seven = [7,35,49]
#multiple_of_five = [20,35,50] 
def sum_multiples_seven_and_five(numbers):
    total_sum = 0
    for x in numbers:
        if x % 7 ==0 or x % 5 ==0:
            total_sum += 1
    return total_sum
numbers = [1,7,20,35,49,50]
sumseven = 7+35+49
sumfive = 20+35+50
print(f"sum of multiples of seven and five is{sumseven} and {sumfive}")



        