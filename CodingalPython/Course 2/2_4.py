# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))

# ---------- PART 2: the running total ----------
# starts at 1 because multiplying by 1 changes nothing,
# the way adding 0 changes nothing
result = 1

# ---------- PART 3 + 4: the loop that multiplies ----------
for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, ": result =", result)

# ---------- PART 5: the answer ----------
print("\nAnswer:", base, "to the power", exponent, "=", result)