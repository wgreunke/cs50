#Find Prime Numbers Brute Force

#Algorithim
#Take a number, then check to see if it can be devised by the list of other prime numbers
#If yes, then break, if not, then add the new prime to the list of primes and go to the next number
print("")
print("")
prime_list=[]
#prime_list.append(2) #Add the trivial numbers to get things started
prime_list.append(3)
#start counting up
for i in range(5,20):
    #print("i",i)
    half_prime=round(len(prime_list))+2
    print("half prime", half_prime)
    counter=0
    for prime in prime_list:
        counter=counter+1
        print("i",i,"Prime", prime, "counter", counter)
        #print("mod",i%prime)
        if(counter>half_prime):
            prime_list.append(i)
        if(counter>half_prime):
                break
        if(i%prime)==0:
            break
        #if(prime==prime_list[-1]):  #You made it to the end of the list so add the number to the list
        #    prime_list.append(i)
        #    print(i)
        #If you get to the end, then add the new prime that you have found


print("The list of primes is ", prime_list)



