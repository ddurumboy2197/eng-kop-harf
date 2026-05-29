def eng_ko_p_qatnashgan_harf(matn):
    harflar = {}
    for harf in matn.lower():
        if harf.isalpha():
            harflar[harf] = harflar.get(harf, 0) + 1
    return max(harflar, key=harflar.get)

matn = input("Matnni kiriting: ")
print("Eng ko'p qatnashgan harf:", eng_ko_p_qatnashgan_harf(matn))
