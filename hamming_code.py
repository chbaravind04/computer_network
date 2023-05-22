def add_parity_bits(data):
    n = len(data)
    r = 1
    while 2 ** r < n + r + 1:
        r += 1

    # Initialize the encoded data with placeholders for parity bits
    encoded_data = [None] * (n + r)

    j = 0
    for i in range(n + r):
        # Check if the current position is a power of 2 (parity bit position)
        if i + 1 == 2 ** j:
            encoded_data[i] = 0  # Placeholder for the parity bit
            j += 1
        else:
            encoded_data[i] = int(data[j - 1])
            j += 1

    return encoded_data


def calculate_parity_bits(encoded_data):
    r = 1
    while 2 ** r < len(encoded_data):
        r += 1

    # Calculate parity bits
    for i in range(r):
        parity_bit_index = 2 ** i - 1
        parity_bit = 0

        for j in range(len(encoded_data)):
            if (j + 1) & (2 ** i) == (2 ** i):
                parity_bit ^= encoded_data[j]

        encoded_data[parity_bit_index] = parity_bit

    return encoded_data


def detect_error(encoded_data):
    r = 1
    while 2 ** r < len(encoded_data):
        r += 1

    error_position = 0

    # Calculate the position of the error
    for i in range(r):
        parity_bit_index = 2 ** i - 1
        parity_bit = 0

        for j in range(len(encoded_data)):
            if (j + 1) & (2 ** i) == (2 ** i):
                parity_bit ^= encoded_data[j]

        if parity_bit != encoded_data[parity_bit_index]:
            error_position += parity_bit_index + 1

    return error_position


def correct_error(encoded_data, error_position):
    if error_position == 0:
        return encoded_data

    encoded_data[error_position - 1] = 1 - encoded_data[error_position - 1]

    return encoded_data


def remove_parity_bits(encoded_data):
    r = 1
    while 2 ** r < len(encoded_data):
        r += 1

    decoded_data = []
    j = 0
    for i in range(len(encoded_data)):
        if i + 1 == 2 ** j:
            j += 1
        else:
            decoded_data.append(encoded_data[i])

    return decoded_data


# Example usage
data = "1011"  # Data to be encoded

encoded_data = add_parity_bits(data)
print("Encoded data:", encoded_data)

encoded_data_with_parity = calculate_parity_bits(encoded_data)
print("Encoded data with parity bits:", encoded_data_with_parity)

error_position = detect_error(encoded_data_with_parity)
print("Detected error at position:", error_position)

corrected_data = correct_error(encoded_data_with_parity, error_position)
print("Corrected data:", corrected_data)

decoded_data = remove_parity_bits(corrected_data)
print("Decoded data:", decoded_data)
