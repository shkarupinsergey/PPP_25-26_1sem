

if __name__ == "__main__":
    pass 
def create_zal(ryads, mesta):
    zal = []
    for x in range(ryads):
        ryad = [0] * mesta
        zal.append(ryad)
    return zal
def show_zal(zal):
    print("Доступные места:")
    for ryad in zal:
        print(" ".join(str(seat) for seat in ryad))
    print()
def zabr_mest(zal, num_mesto):
    if num_mesto > len(zal[0]):
        print("Запрашиваемое количество мест больше, чем мест в ряду.")
        return False
    for ryad_index, ryad in enumerate(zal):
        free_mest = 0
        start_mest = 0
        for mest_index, mest in enumerate(ryad):
            if mest == 0:
                if free_mest == 0:
                    start_mest = mest_index
                free_mest += 1
                if free_mest == num_mesto:
                    for i in range(start_mest, start_mest + num_mesto):
                        ryad[i] = 1
                    print(f"Забронировано: ряд {ryad_index + 1}, места с {start_mest + 1} по {start_mest + num_mesto}")
                    return True
            else:
                free_mest = 0
                start_mest = 0
    print("Нет доступных подряд мест для бронирования.")
    return False
def main():
    zal = create_zal(5, 10)
    show_zal(zal)
    zabr_mest(zal, 4)
    show_zal(zal)
    zabr_mest(zal, 3)
    show_zal(zal)
    zabr_mest(zal, 5)
    show_zal(zal)
    zabr_mest(zal, 11)
    show_zal(zal)
