#This method is study from the forum

numbles=[i for i in range(1,1000) if i%3==0 or i%5==0]
# also: if not n%3 or not n%5(can not delete the second not)
sum=sum(numbles)
#sum element in the list
print sum
#range(1,1000) means:1-999 we can also write:range(1000)
