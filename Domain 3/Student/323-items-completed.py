items = ["Rock", "Pogo Stick", "Wand", "Pogo Stick", "Wand", "Rock", "Pogo Stick"]
num = 0;
for i in range(len(items)):
    if (i) % 2 == 0 and num < 3:
        num += 1
    print(f"You can get a {items[i]} at level {num}.")