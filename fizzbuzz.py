def fizzBuzz(n):
    # Write your code here
    i=1
    end=n
    while(i>=end):
        if(i/3==0 and i/5==0):
            print("FizzBuzz")
        elif(i/3==0):
            print("Fizz")
        elif(i/5==0):
            print("Buzz")
        else:
            pass
        i = i+1
n = int(input("hi :"))

fizzBuzz(n)
