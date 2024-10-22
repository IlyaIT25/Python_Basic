numbers = []
if len(numbers) % 2 == 0:
    step1 = (numbers[:len(numbers)//2])
    step2 = (numbers[len(numbers)//2:])
    print([step1] + [step2])
else:
    half = (len(numbers) + 1) // 2
    step1 = numbers[:half]
    step2 = numbers[half:]
    print([step1] + [step2])

