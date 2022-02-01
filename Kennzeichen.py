import re


def validate(kennzeichen: str) -> bool:
    if re.search(r'[-]', kennzeichen) == None:
        return False
    splitted = kennzeichen.partition("-")
    A, B, C = splitted
    if A.isupper():
        if 3 >= re.search('[A-Z]+', A).span()[1] >= 2:
            pass
        else:
            return False
    else:
        return False
    if C.isupper():
        c_letters, c_numbers = re.findall(r'[A-Z]+|\d+', C)
        if 2 >= len(c_letters) >= 1:
            if 4 >= len(c_numbers) >= 1:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def get_city_ID(kennzeichen: str) -> str:
    return kennzeichen.partition("-")[0]


def match_to_city(l: list, d: dict) -> dict:
    result = {}
    for i in l:
        try:
            id = get_city_ID(i)
            result[i] = d[id]
        except:
            pass
    return result


def invert_dictionary(d: dict) -> dict:
    results = {}
    for i in d:
        try:
            results[d[i]] = [*results[d[i]], i]
            print(results)
        except:
            results[d[i]] = [i]
    return results
