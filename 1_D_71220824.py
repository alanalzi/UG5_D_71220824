def gaka(a, b, c):
    kalim_baru = ""
    kata = ""
    for i in range(len(a)):
        if a [i] == " ":
            if  kata == b:
                kalim_baru = kalim_baru + c + " "
            else:
                kalim_baru = kalim_baru + kata + " "
            kata = ""
        else:
            kata = kata + a [i]
    if kata == b :
        kalim_baru = kalim_baru + c
    else:
        kalim_baru = kalim_baru + kata
    return kalim_baru
a = input("Masukan kalimat: ")
b = input("Kata yang akan dicari: ")
c = input("Diubah menjadi: ")
gaka(a, b, c)