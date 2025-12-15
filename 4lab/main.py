

if __name__ == "__main__":
    pass # Ваш код здесь
import math

class Figura:
    def ploshad(self):
        return 0

    def perimetr(self):
        return 0

    def vershiny(self):
        return 0

class Triugolnik(Figura):
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def dlina(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def perimetr(self):
        a = self.dlina(self.x1, self.y1, self.x2, self.y2)
        b = self.dlina(self.x2, self.y2, self.x3, self.y3)
        c = self.dlina(self.x3, self.y3, self.x1, self.y1)
        return a + b + c

    def ploshad(self):
        return abs(
            (self.x1 * (self.y2 - self.y3) +
             self.x2 * (self.y3 - self.y1) +
             self.x3 * (self.y1 - self.y2)) / 2
        )

    def vershiny(self):
        return 3

class Prymougolnik(Figura):
    def __init__(self, x1, y1, x2, y2):
        self.shirina = abs(x2 - x1)
        self.visota = abs(y2 - y1)

    def ploshad(self):
        return self.shirina * self.visota

    def perimetr(self):
        return 2 * (self.shirina + self.visota)

    def vershiny(self):
        return 4

class Krug(Figura):
    def __init__(self, x, y, r):
        self.r = r

    def ploshad(self):
        return math.pi * self.r * self.r

    def perimetr(self):
        return 2 * math.pi * self.r

    def vershiny(self):
        return 0

stroki = [
    "triugolnik 0 0 1 0 0 1",
    "prymougolnik 0 0 3 2",
    "krug 1 1 5"
]

figuri = []

for stroka in stroki:
    parts = stroka.split()

    if parts[0] == "triugolnik":
        figuri.append(
            Triugolnik(
                float(parts[1]), float(parts[2]),
                float(parts[3]), float(parts[4]),
                float(parts[5]), float(parts[6])
            )
        )

    elif parts[0] == "prymougolnik":
        figuri.append(
            Prymougolnik(
                float(parts[1]), float(parts[2]),
                float(parts[3]), float(parts[4])
            )
        )

    elif parts[0] == "krug":
        figuri.append(
            Krug(
                float(parts[1]), float(parts[2]),
                float(parts[3])
            )
        )

komanda = "ploshad"   

if komanda == "ploshad":
    summa = 0
    for figura in figuri:
        summa += figura.ploshad()
    print("Total ploshad:", round(summa, 2))

elif komanda == "perimetr":
    summa = 0
    for figura in figuri:
        summa += figura.perimetr()
    print("Total perimetr:", round(summa, 2))

elif komanda == "vershiny":
    summa = 0
    for figura in figuri:
        summa += figura.vershiny()
    print("Total vershiny:", summa)
