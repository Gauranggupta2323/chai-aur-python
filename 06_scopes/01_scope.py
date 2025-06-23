username = "chaiaurcode"

def func():
     username = "chai"
    print(username)        # chaiaurcode aaega kyuki vo global hi

print(username)   # ismai chai aaega kyuki niche function call kr diya 
func()


x = 99 
# def func2(y):
#     z = x + y
#     return z

# result = func2(1)      // isko result maii store kiya
# print(result)       // x ko 99 lenge  aur y ko 1

# def func3():
#     global x       // avoid krna ise use krne ka
#     x = 12
    
# func3()
# print(x)



def f1():
    x = 88
    def f2():
        print(x)
    return f2         // f2 ka pura definition bheja hai return ke through  // bina f1 ke bulaye 99 aaega
myResult = f1()
myResult()           // 88


def chaicoder(num):
    def actual(x):              // Closure or  factor function
        return x ** num
    return actual



f = chaicoder(2)    // ye square calculate karega 
g = chaicoder(3)    // ye cube calculate karega 

print(f(3))
print(g(3))
