import math

data = input("Enter data: ")
parity = input("Enter odd/even parity: ")

def get_bits(n):
    for i in range(n):
        if(2 ** i >= n + i + 1):
            return i

def data_plus_parity(data, bits):
    new_data = ''
    k = 1
    j = 0
    for i in range(1, len(data) + bits + 1):
        if i == 2 ** j:
            new_data += '0'
            j += 1
        else:
            new_data += data[-1 * k]
            k += 1
    return new_data[::-1]

def get_parity_bits(data, bits):
    result = data[:]
    for i in range(bits):
        xor = 0 if parity == "even" else 1
        val = 2 ** i
        for j in range(1, len(data) + 1):
            if (j & val) == val:
               xor = xor ^ int(data[len(data) - j])
        result = result[:len(data) - val] + str(xor) + result[len(data) - val + 1:]
    return result

def detect(rec_data, data):
    xor = int(rec_data, 2) ^ int(data, 2)
    if xor != 0:
        pos = int(math.log2(xor))+ 1
        print(f"Error detected at position {pos}.")
        print(f"Corrected data: {data}")
    else:
        print("No error detected.")

bits = get_bits(len(data))
new_data = data_plus_parity(data, bits)
hamming_code = get_parity_bits(new_data, bits)
print("Hamming Code generated:", hamming_code)
received_data = input("Enter received data: ")
detect(received_data, hamming_code)