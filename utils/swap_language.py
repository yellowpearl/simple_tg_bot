def swp_lng(lst):
    """
    :param lng: rus or lat
    :param lst: massage from user
    :return: swp lst on other lng
    """
    rus = 'йцукенгшщзхъфывапролджячсмитьбю,'
    capital_rus = "ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,"
    lat = 'qwertyuiop[]asdfghjkl;zxcvbnm,.?'
    capital_lat = "QWERTYUIOP[]ASDFGHJKL;'ZXCVBNM,.?"
    answer = ''
    if not lst:
        return 'Error'

    if lst[0] in rus or lst[0] in capital_rus:
        lng = 'lat'
    else:
        lng = 'rus'

    if lng == 'rus':
        letters = rus
        capital_letters = capital_rus
        other_letters = lat
        capital_other_letters = capital_lat
    else:
        letters = lat
        capital_letters = capital_lat
        other_letters = rus
        capital_other_letters = capital_rus

    for i in range(0, len(lst)):
        if lst[i] in other_letters:
            answer += letters[other_letters.index(lst[i])]
        elif lst[i] in capital_other_letters:
            answer += capital_letters[capital_other_letters.index(lst[i])]
        else:
            answer += lst[i]

    return answer