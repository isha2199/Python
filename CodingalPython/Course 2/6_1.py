# ── GAME SETTINGS ─────────────────────────────────────────────
secret       = 27      # Change this before distributing the boilerplate
max_attempts = 5

# ── SETUP ─────────────────────────────────────────────────────
count = 0
guess = 0

print("=" * 42)
print("        🎮  NUMBER GUESSING GAME")
print("=" * 42)
print("I have a secret number between 1 and 50.")
print("You have 5 attempts to guess it.")
print("After each wrong guess I will give you a hint.")
print()

# ── MAIN GAME LOOP ─────────────────────────────────────────────
while count < max_attempts and guess != secret:

    guess = int(input("Enter your guess: "))
    count = count + 1

    if guess == secret:
        print()
        print("🎉 Correct! You guessed it in", count, "attempt(s)!")
        print("Well done — you are a number wizard! 🧙")

    else:
        # Calculate distance without abs()
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        # Hint levels
        if diff >= 20:
            print("🧊 Ice cold!  You are very far away.")
        elif diff >= 10:
            print("🥶 Cold.      Still quite a distance to go.")
        elif diff >= 5:
            print("🌡️  Warm!      Getting closer...")
        else:
            print("🔥 Hot!       Almost there!")

        # Remaining lives
        remaining = max_attempts - count

        if remaining > 0:
            print("Lives left: ", end="")
            for i in range(remaining):
                print("❤️ ", end="")
            print()
        print()

# ── GAME OVER CHECK ────────────────────────────────────────────
if guess != secret:
    print("=" * 42)
    print("💀 Game over!  You used all 5 attempts.")
    print("   The secret number was:", secret)
    print("=" * 42)