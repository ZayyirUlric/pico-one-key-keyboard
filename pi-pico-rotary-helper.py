f = open("out2.txt","w")
x = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
chars = 51+len(x)
for i in range(51,chars,1):
    print(i)
    out = "\t("+str(i)+"): ([Keycode."+x[i-51]+"]),\n"
    f.write(out)
