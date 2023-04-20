# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numbers():
    y=1
    while y<50:
        y+=1
        if y%2==0:
            print(f"{y} is divisible by 2")
            continue
        print(y)


# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_number():
    y=0
    while y<50:
        y+=1
        if y%y==1:
            print(f"{y} Prime")
        else:
            print(f"{y} Not prime")

# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_number():
    d=range(50)
    for r in d:
        if r%2==0:
          print(r)
   
# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
# def divisible_by_three():
#     e=0
#     sum=0
#     while e%3==0:
#         print(f"{}")


