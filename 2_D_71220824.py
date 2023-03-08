def hitung_mobil ():
    a = 0
    sur = 0
    sol = 0
    jog = 0
    mag = 0 
    while a == 0:
        y = input("Masukan asal mobil (ketik done kalau udah ga masukin asalnya): ")
        if y == "solo":
            sol = sol + 1
        elif y == "surabaya":
            sur = sur + 1
        elif y == "jogja":
            jog = jog + 1
        elif y == "magelang":
            mag = mag + 1
        elif y == "done":
            break
        else:
            print("Asal mobil belum ada masbro!")         
    print("Jumlah mobil asal jogja      : ", jog)
    print("Jumlah mobil asal magelang   : ", mag)
    print("Jummlah mobil asal solo      : ", sol)
    print("Jumlah mobil asal surabaya   : ", sur)

hitung_mobil()