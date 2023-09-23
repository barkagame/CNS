mass=[]
active=True
alfabet=["Not","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ы","Ь","Э","Ю","Я"]
num10=float(input("Введите число из деситеричной системы\n"))
numConv=float(input("Введите систему в, которую хотите перевести число(2-69)\n"))
if (numConv>69 or numConv<2):
    exit("Неправильный формат")
otv=num10
on=True
while (on):
    res=int(otv%numConv)
    mass.append(res)
    otv=int(otv//numConv)
    if(otv<numConv):
        on=False
        mass.append(otv)
        mass.reverse()
        for i in range(len(mass)):

            if (mass[i]>=10):
                x=mass[i]-9
                y=alfabet[x]
                mass[i]=y
            if (mass[i] == 0 and active==True):
                mass[i]=""
            print(mass[i], end='')
            active = False


