def getCPF(CPF):
    """
    Function to validade the inputed CPF. It can validade CPF's inputed as just numbers or
    as xxx.xxx.xxx-xx. The function returns the CPF as a eleven digit interger number.
    """
    while True:
        user_input = str(input(CPF))
        if len(user_input) != 11 and len(user_input) != 14:
            print('Invalid CPF')
        else:
            if len(user_input) == 11:
                try:
                    user_input = int(user_input)
                    return user_input
                except ValueError:
                    print('Invalid CPF')
            elif len(user_input) == 14:
                user_input = f"{user_input[0:3]}{user_input[4:7]}{user_input[8:11]}{user_input[12:14]}"
                try:
                    user_input = int(user_input)
                    return user_input
                except ValueError:
                    print('Invalid CPF')