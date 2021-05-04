rating = [10, 7, 7, 3, 3, 3, 2, 1]

num = int(input("Enter number: "))

position = 0
for element in rating:
    if element < num:
        rating.insert(position, num)
        break

    position += 1

if position == len(rating):
    rating.append(num)

print(f"User entered number: {num}. Result: {rating}")
