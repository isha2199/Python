total    = 560       # total harvest in kg
bag_size = 24        # each bag holds 24 kg

bags     = total // bag_size  # 560 // 24 = 23 full bags
leftover = total % bag_size   # 560 % 24  = 8 kg left over

print("Full bags:", bags)      # Output: 23
print("Leftover:", leftover)   # Output: 10