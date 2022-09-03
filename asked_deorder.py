import sys
while True:
    try:

        asked_order = input('$ ')
        list_of_invalid = ['import' in asked_order,
        'from' in asked_order,
        'os' in asked_order,
        'sys' in asked_order,
        'subprocess' in asked_order]
        try:
            if any(list_of_invalid):
                print('Sike it\'s wrong command !!')
            else:
                exec(asked_order)
        except SyntaxError as erri:
            print('SyntaxError')
    except:
        pass