Am = 13550 / (33 * 30)
Bm = 15960 / (35 * 24)
Cm = 11990 / (30 * 33)

cheapest = min(Am,Bm,Cm)

if cheapest == Am:
    print(f"A_market이 1m당 {Am:.2f}로  최저가이다")
elif cheapest == Bm:
    print(f"B_market이 1m당 {Bm:.2f}로  최저가이다")
else:
    print(f"C_market이 1m당 {Cm:.2f}로  최저가이다")
