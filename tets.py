log:float=[]
for i in range(300):
    log.append(i)    


print(sum(log[-1:-(5*60):-1])/(5*60))