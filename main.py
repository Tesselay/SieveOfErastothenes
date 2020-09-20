# This is a sample Python script.
def getMultiples(multiplied_value, max_value):
    multiples = []
    power = 1
    multiplied_value ^= power
    while( multiplied_value <= max_value ):
        multiples.append(multiplied_value)
        power += 1
        multiplied_value ^= power

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
