print("Hello! I am AI bot. What's your name?")

name = input()

print("Nice to meet you, " + name )

print("How are you feeling today? (good/bad)")
mood = input().lower()

if mood == "good":
    print("That's great to hear! Keep up the positive vibes!")
elif mood == "bad":
    print("I'm sorry to hear that. Remember, it's okay to have bad days. Take care of yourself!")
else:
    print("I didn't quite understand that. But I hope you have a good day regardless!")

print("It was nice chatting with you, " + name + "! Have a wonderful day!")
