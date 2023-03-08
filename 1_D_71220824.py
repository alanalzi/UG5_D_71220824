def gaka(a, b, c):
    x = ""
    y = ""
    for i in range(len(a)):
        if a [i] == " ":
            if  y == b:
                x = x + c + " "
            else:
                x = x + y + " "
            y = ""
        else:
            y = y + a [i]
    if y == b :
        x = x + c
    else:
        x = x + kata
    return x
a = input("Masukan kalimat: ")
b = input("Kata yang akan dicari: ")
c = input("Diubah menjadi: ")
x = gaka(a, b, c)
print(x)