import decimal_binary

# Transorms ip decimal address to its binary form
def ip_decimal_to_binary(ip_address):
    ip_address_list = ip_to_list(ip_address)
    result = ""
    for octet in ip_address_list:
        if result != "":
            result = result + "." + decimal_to_8bit_binary(int(octet))
        else:
            result += decimal_to_8bit_binary(int(octet))


    return result
        
    
# Splits ip into ocats
def ip_to_list(ip_address):
    ip_list = list(ip_address.split("."))
    return ip_list

# Transoform decimal octate to binary octate
def decimal_to_8bit_binary(dec_num):
    if 0 <= dec_num <= 255:

        bin_num = decimal_binary.decimal_to_binary(dec_num)

        while len(bin_num) < 8:
            bin_num = "0" + bin_num

        return bin_num


    elif 0 > dec_num:
        print("Error! Too smaller!")
    
    elif 255 < dec_num:
        print("Error! Too bigger!")
  

    return bin_num

# Main process
if __name__ == "__main__":
    print(ip_decimal_to_binary("192.168.1.1"))
    # print(decimal_to_8bit_binary(125))