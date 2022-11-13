
# low=int(input("Enter lower bound: "))
# high=int(input("Enter upper bound: "))
low=2
high=90
for num in range(low, high + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)