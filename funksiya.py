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
