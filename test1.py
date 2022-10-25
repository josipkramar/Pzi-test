def zlatnici(mase, m):
    mase.sort()
    ukupna_masa= 0
    uzeto_zlatnika = 0
    for masa in mase:
        if ukupna_masa + masa <= m:
            ukupna_masa += masa
            uzeto_zlatnika += 1
        else:
            break
    return uzeto_zlatnika

lista = [4, 10, 5, 1]

m = 10
print(zlatnici(lista, m))
