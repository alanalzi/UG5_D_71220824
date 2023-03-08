import math
x = 0
while x == 0:
    j_awal = input("Masukan jarak awal (dalam meter): ")
    
    if j_awal == "berhenti" or j_awal == "stop":
        print("program dihentikan masbro")
        break

    s_1 = int(input("Masukan sudut elevasi di menit ke-5 (dalam derajat): "))
    s_2 = int(input("Masukan sudut elevasi di menit ke-6 (dalam derajat): "))

    s_1 = math.radians(float(s_1))
    s_2 = math.radians(float(s_2))
    j_awal = float(j_awal)

    ta = j_awal * math.tan(s_1)
    print("ketinggian drone saat menit ke-5 adalah", round(ta,2), "meter.")
    j_akh = j_awal * math.tan(s_2) - j_awal * math.tan(s_1)
    sel_ket = j_akh *math.tan(s_2)  
    
    if j_awal == "berhenti" or j_awal == "stop":
        a = 1
        for i in range(a):
            print("program dihentikan masbro")
        break
    
    print("selisih ketinggian drone saat menit ke-5 dan ke-8 adalah ", round(sel_ket,2), "meter.")