

def camel_case_to_snake_case(string: str) -> str:
    '''
    >>> camel_case_to_snake_case('SomeSDK')
    'some_sdk'

    >>> camel_case_to_snake_case('RServoDrive')
    'r_servo_drive'

    '''
    res = []
    flag = 0
    
    for c_ind, char in enumerate(string):
        if c_ind and char.isupper():
            if not flag:
                res.append('_')
                res.append(char.lower())
                flag = 1
            else:
                res.append(char.lower())
        else:
            res.append(char.lower())
            flag = 0

    return ''.join(res)
