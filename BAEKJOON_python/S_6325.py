a =[2,4,6,8,10]

def function(i,j):
    if i in j:
        print("%d => True" %i)
    else:
        print("%d => False" %i)
        
print(a)
function(5,a)
function(10,a)