def num_ptb2us(str_number):
    try:
        number_to_return = float(str_number.upper().replace('R$ ','').replace('.','').replace(',','.'))
    except Exception as e:
        number_to_return = None
    return number_to_return