from sympy import symbols, Eq, solve

y = symbols('x')
eq1 = Eq(x*2 -5x + 6)


sol = solve(eq1, dict=True)
print(sol)
