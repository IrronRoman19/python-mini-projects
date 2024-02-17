# Transorms decimal to binary (Base 10 -> Base 2)
def decimal_to_binary(dec_num):
    res_bin_num = ""

    while dec_num != 0:
        res_bin_num = str(dec_num % 2) + res_bin_num
        dec_num = dec_num // 2

    return res_bin_num

# Transorms binary to decimal (Base 2 -> Base 10)
# Option 1

def binary_to_decimal(bin_num):
    res_dec_num = 0
    pow_dec = 0

    for i in bin_num[::-1]:
        res_dec_num += (int(i) * (2 ** pow_dec))
        pow_dec += 1

    return res_dec_num

# Option 2

# def binary_to_decimal(bin_num):
#     res_dec_num = 0
#     res_len_bin = len(bin_num)

#     for i in bin_num:
#         if i == "0":
#             res_dec_num += 0 * (2 ** (res_len_bin - 1))

#         elif i == "1":
#             res_dec_num += 1 * (2 ** (res_len_bin - 1))

#         else:
#             print("Invalid value, use only '0' or '1'")
#             return

#         res_len_bin -= 1

#     print(f"Decimal (Base 10): {res_dec_num}")

# Main process and choosing options (Base 10 -> Base 2) or (Base 2 -> Base 10) or quit
def main():
    looping = True
    while looping == True:
        print("\nWelcome!")
        print("Convert from decimal to binary (Base 10 -> Base 2): please enter '1'")
        print("Convert from binary to decimal (Base 2 -> Base 10): please enter '2'")
        print("To quit from calculator: please enter 'q'")
        choice = input("Enter the choice: ")

        if choice == "1":
            print(decimal_to_binary(int(input("\nEnter the decimal number (Base 10): "))))
        elif choice == "2":
            print(binary_to_decimal(str(input("\nEnter the binary number (Base 2): "))))
        elif choice == "q".upper() or choice == "q".lower():
            print("Bye!")
            looping == False
            return
        else:
            print("Invalid values")

if __name__ == "__main__":
   main()
