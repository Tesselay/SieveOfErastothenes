# This is a sample Python script.
def getMultiples(multiplied_value, max_value):
    multiples = []
    multiplicative = 1
    powered_multiplied_value = multiplied_value * multiplicative
    while powered_multiplied_value <= max_value:
        multiples.append(powered_multiplied_value)
        multiplicative += 1
        powered_multiplied_value = multiplied_value * multiplicative

    return multiples


if __name__ == '__main__':
    max_value = 50
    start_value = 2
    crossed_out_values = []
    prime_numbers = []

    while start_value <= max_value:
        try:
            crossed_out_values.index(start_value)
        except ValueError as e:
            prime_numbers.append(start_value)
            new_crossed_out_values = getMultiples(start_value, max_value)
            crossed_out_values.extend(new_crossed_out_values)

        start_value += 1

    print(crossed_out_values)
    print(prime_numbers)