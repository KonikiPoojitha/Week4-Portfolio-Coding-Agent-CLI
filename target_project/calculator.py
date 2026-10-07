def average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate average of an empty list")

    return sum(numbers) / len(numbers)
