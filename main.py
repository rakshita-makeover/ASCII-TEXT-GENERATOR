from art import text2art

print("=" * 45)
print("       ASCII ART GENERATOR")
print("=" * 45)

while True:
    text = input("\nEnter text (or 'exit' to quit): ")

    if text.lower() == "exit":
        break

    print()
    print(text2art(text, font="standard"))
