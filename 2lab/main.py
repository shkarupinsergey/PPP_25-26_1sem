

if __name__ == "__main__":
    pass # Ваш код здесь
def check_skobki(text):
    spisok = []
    pars = {')': '(', ']': '[', '}': '{'}
    a = 1
    for simvol in text:
        if simvol in '([{':
            spisok.append((simvol, a))
        elif simvol in ')]}':
            if len(spisok) == 0:
                return a
            last = spisok.pop()
            if pars[simvol] != last[0]:
                return a
        a += 1

    if len(spisok) > 0:
        return spisok[-1][1]

    return "ok"
print(check_skobki("(a)(b(c[d{e{r}f{g}s}w]r)tasd)"))
print(check_skobki("(a[b{c}]"))
print(check_skobki("a)b"))
print(check_skobki("({[)]}"))
