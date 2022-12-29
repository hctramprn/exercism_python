def encode(numbers):
    # defines the list that will hold the encoded values
    encoded_lst = []
    # loops through the passed values converting them into binary numbers
    # and extracting chunks of 7 characters lenght
    for num in numbers:
        bin_num = str(bin(num))[2:]
        chunks = []

        while bin_num:
            chunks.append(bin_num[-7:])
            bin_num = bin_num[:-7]
        
        len_chunk = [('000000' + chnk)[-7:] for chnk in chunks]

        # defines the list that will hold the chunks of each number
        # and adds the corresponding msb character
        bin_lst = []
        msb_status = False
        for chunk in len_chunk:
            if not msb_status:
                msb = '0'
                msb_status = True
            else:
                msb = '1'
            bin_lst.append(f'{msb}{chunk}')

        # encodes the chunks and adds them to the general list
        encoded_temp = [int(binary_num, 2) for binary_num in reversed(bin_lst)]
        encoded_lst += encoded_temp
    
    # returns the encoded list
    return encoded_lst


def decode(bytes_):
    # converts the given bytes to binary numbers of 8 characters length
    bin_lst = [str(bin(num))[2:] for num in bytes_]
    len_lst = [('0000000' + bin_num)[-8:] for bin_num in bin_lst]

    # defines the list that will hold the sublists of binary chunks
    sublists = []
    temp_lst = []
    for chunk in len_lst:
        temp_lst.append(chunk[-7:])

        if chunk[0] == '0':
            sublists.append(temp_lst)
            temp_lst = []

    # raise a ValueError if a sequence is incomplete (msb value)
    if not sublists:
        raise ValueError('incomplete sequence')
    
    # joins the chunks and decode each number
    decoded_lst = [int(''.join(sublst), 2) for sublst in sublists]

    # returns the decoded list
    return decoded_lst
