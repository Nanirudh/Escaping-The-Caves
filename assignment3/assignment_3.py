##Using Extended Euclidean Algorithm
#a and p should be relatively prime
#Reference for the code www.geeksforgeeks.com

def gcdExtended(a, b): 
    if a == 0 :  
        return b,0,1  
    gcd,x1,y1 = gcdExtended(b%a, a) 
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd,x,y

def modInverse(a, p):
    g,x,y = gcdExtended(a, p);
    if(g != 1):
        print("Inverse doesn't exist")
    else:     
        res = (x % p + p) % p;
        print("Modular multiplicative inverse is ",res)
        

a = 431955503618234519808008749742
p = 455470209427676832372575348833
modInverse(a,p)




#Modular multiplication
x1 = 70749996790223471732904681640
x2 = 176325509039323911968355873643
res = (x1*x2)%p