def collatz_sequence(n):
    if n <= 0:
        print("Please enter a positive integer.")
        return
    
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    
    return sequence

# Input from user
num = int(input("Enter a positive integer: "))
result = collatz_sequence(num)

if result:
    print("Collatz sequence:")
    print(result)
