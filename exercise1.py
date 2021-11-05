user_input=int(input("Please enter a number: "))
def sum_of_odd_numbers(x):
    sum = 0
    for i in range(1,x+1):
        if i%2==1:
            sum += i
    return sum
def avarage_of_even_numbers(x):
    even_numbers=0
    sum_evens=0
    for i in range(1,x+1):
        if i%2==0:
            even_numbers +=1
            sum_evens += i
    avarage = sum_evens/even_numbers
    return avarage
print(sum_of_odd_numbers(user_input),avarage_of_even_numbers(user_input) )
