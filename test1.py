n=1
def fun(s):
    global n
    if len(s)<=1:
        return
    elif int(s[-2]+s[-1])<=26:
        n+=1
        fun(s[:-2])
    fun(s[:-1])

s="115111"
fun(s)
print(n)