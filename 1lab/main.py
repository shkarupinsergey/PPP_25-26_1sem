

if __name__ == "__main__":
    pass # Ваш код здесь
zal = []
def sozdat_zal():
    global zal
    ryadov = 5
    mest = 10
    for r in range(ryadov):
        ryad = []
        for m in range(mest):
            ryad.append(0)
        zal.append(ryad)
def pokazat_zal():
    print("Схема зала:")
    for r in zal:
        stroka = ""
        for m in r:
            stroka += str(m) + " "
        print(stroka)
    print()
def zabronirovat_mesta(n):
    ok = False
    for i in range(len(zal)):
        ryad = zal[i]
        podryad = 0
        start = -1
        for j in range(len(ryad)):
            if ryad[j] == 0:
                if podryad == 0:
                    start = j
                podryad += 1
            else:
                podryad = 0
                start = -1
            if podryad == n:
                for k in range(start, start + n):
                    zal[i][k] = 1
                print(f"Забронировано! Ряд {i+1}, места {start+1}-{start+n}")
                ok = True
                return True
    if not ok:
        print("Нет подходящих мест :(")
        return False
sozdat_zal()
pokazat_zal()

zabronirovat_mesta(4)
pokazat_zal()

zabronirovat_mesta(3)
pokazat_zal()

zabronirovat_mesta(5)
pokazat_zal()

zabronirovat_mesta(11)
pokazat_zal()
