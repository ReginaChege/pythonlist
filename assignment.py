# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numbers():
    y=1
    while y<50:
        y+=1
        if y%2==0:print(f"{y} is divisible by 2")
        continue
        print(y)

even_numbers()
# Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_number(numb):
    if numb==1:
         print("Not prime")
    elif numb==2:
          print("Prime")
    else:
        for i in range(2,numb):
            if numb%i==0:
                print("not prime")
            print("Prime")
            break
prime_number(23)
# Write a function that takes a list of integers as input and prints
#  the sum of all the even numbers in the list.
def sum_even_number(*numbs):
   add=0
   for r in numbs:
       if r%2==0: 
        add+=r
   print(add)
sum_even_number(12,34,55,67,86)  
# Write a function that takes any two integers as input, and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def divisible_by_three(d,e):
  x=range(d,e)
  add=0
  for i in x:
      if  i%3==0:
          add+=i
  print(add)
divisible_by_three(1,10)
