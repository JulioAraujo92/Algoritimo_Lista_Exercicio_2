x = float(input("\nDigite valor de x: "))
fx = 0

if x > 4 or x < (-4):
    fx = (5*x+3) / ((x**2-16)**0.5)
    print(f"\nf(x)= {fx:.2f}")
else:
    print("\nNão pode ser feita\n")

