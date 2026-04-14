import math

# 1-misol: Sonning 3-darajasini hisoblash
def powerA3(a):
    return a**3

print("1-misol natijalari:")
print(powerA3(20))
print(powerA3(5.5))

# 2-misol: Sonning 2, 3 va 4-darajalarini chiqarish
def powerA234(a):
    print(f"{a} ning kvadrati: {a**2}")
    print(f"{a} ning kubi: {a**3}")
    print(f"{a} ning 4-darajasi: {a**4}")

# 3-misol: Arifmetik va geometrik o'rtachani hisoblash
def MEAN(x, y):
    am = (x + y) / 2
    gm = math.sqrt(x * y)
    return am, gm

# 4-misol: Teng tomonli uchburchak perimetri va yuzasi
def Triangle(a):
    P = 3 * a
    S = (math.sqrt(3) / 4) * a**2
    return P, S

# 5-misol: To'g'ri to'rtburchak yuzasi va perimetri
def RectPS(x1, y1, x2, y2):
    a = abs(x2 - x1)
    b = abs(y2 - y1)
    S = a * b
    P = 2 * (a + b)
    return P, S

# 6-misol: Raqamlar soni va yig'indisini topish
def DigitCountSum(n):
    s = str(abs(n))
    return len(s), sum(map(int, s))

# 7-misol: Sonni teskarisiga o'girish
def InvertDigit(n):
    res = 0
    temp_n = abs(n)
    while temp_n > 0:
        res = res * 10 + temp_n % 10
        temp_n //= 10
    return res

# 8-misol: Sonning o'ng tomoniga raqam qo'shish
def AddRightDigit(son, raqam):
    return son * 10 + raqam

# --- Sinov qismi (Inputlar) ---
print("\n--- Ma'lumotlarni kiritish ---")
k = int(input("8-misol uchun son kiriting: "))
r = int(input("Qo'shmoqchi bo'lgan raqamingizni kiriting: "))
print(f"Natija: {AddRightDigit(k, r)}")
import math

# FunSimple9: Songa chapdan raqam qo'shish
def add_left_digit(k, r):
    return int(str(r) + str(k))

# FunSimple10: Qiymatlarni almashtirish (Swap)
def swap(x, y):
    return y, x

# FunSimple11: Minmax (Kichigini x ga, kattasini y ga yozish)
def minmax(x, y):
    if x < y:
        return x, y
    return y, x

# FunSimple12: SortInc3 (O'sish tartibida saralash)
def sort_inc3(a, b, c):
    res = sorted([a, b, c])
    return res[0], res[1], res[2]

# FunSimple13: SortDec3 (Kamayish tartibida saralash)
def sort_dec3(a, b, c):
    res = sorted([a, b, c], reverse=True)
    return res[0], res[1], res[2]

# FunSimple14: ShiftRight3 (O'ngga siklik siljitish)
def shift_right3(a, b, c):
    return c, a, b

# FunSimple15: ShiftLeft3 (Chapga siklik siljitish)
def shift_left3(a, b, c):
    return b, c, a

# FunSimple16: Ishora funksiyasi
def ishora(n):
    if n < 0: return -1
    if n > 0: return 1
    return 0

# FunSimple17: Kvadrat tenglama ildizlar soni
def ildizlar_soni(a, b, c):
    d = b**2 - 4*a*c
    if d > 0: return 2
    if d == 0: return 1
    return 0

# FunSimple18: Doira yuzini hisoblash
def doira_yuzi(r):
    pi = 3.1415
    return pi * (r**2)

# --- ISHLATISH NAMUNALARI ---

print("--- FunSimple9 ---")
print(add_left_digit(123, 5)) # 5123

print("\n--- FunSimple10 ---")
a, b, c, d = 1, 2, 3, 4
a, b = swap(a, b)
c, d = swap(c, d)
print(f"A={a}, B={b}, C={c}, D={d}")

print("\n--- FunSimple11 ---")
a, b, c, d = 10, 5, 20, 3
x1, y1 = minmax(a, b)
x2, y2 = minmax(c, d)
mini, _ = minmax(x1, x2)
_, maxi = minmax(y1, y2)
print(f"Eng kichigi: {mini}, Eng kattasi: {maxi}")

print("\n--- FunSimple12 ---")
a1, b1, c1 = 10, 2, 5
a1, b1, c1 = sort_inc3(a1, b1, c1)
print(f"O'sish tartibi: {a1, b1, c1}")

print("\n--- FunSimple13 ---")
a2, b2, c2 = 5, 12, 8
a2, b2, c2 = sort_dec3(a2, b2, c2)
print(f"Kamayish tartibi: {a2, b2, c2}")

print("\n--- FunSimple14 ---")
a3, b3, c3 = 1, 2, 3
a3, b3, c3 = shift_right3(a3, b3, c3)
print(f"ShiftRight: {a3, b3, c3}")

print("\n--- FunSimple15 ---")
a4, b4, c4 = 1, 2, 3
a4, b4, c4 = shift_left3(a4, b4, c4)
print(f"ShiftLeft: {a4, b4, c4}")

print("\n--- FunSimple16 ---")
print(f"ishora(-5) + ishora(10) = {ishora(-5) + ishora(10)}")

print("\n--- FunSimple17 ---")
print(f"x^2 - 5x + 6 ildizlar soni: {ildizlar_soni(1, -5, 6)}")

print("\n--- FunSimple18 ---")
for r in [2, 5, 10]:
    print(f"R={r} bo'lsa, Yuza={doira_yuzi(r)}")

