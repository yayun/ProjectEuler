s="73167176531330624919225119674426574742355349194934"
k=0
L=len(s)
max=0
for i in range(0,L,5):
    num=s[i:i+5]
    if int(num)>max:
        max=int(num)
print max

