calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    count_calls()
    tuple_info = (len(string), string.lower(), string.upper())
    print(tuple_info)
    return tuple_info


def is_contains(string, list_to_search):
    count_calls()
    string = string.lower()
    for x in list_to_search:
        if x.lower() == string:
            print(True)
            return True
    print(False)
    return False


string_info('Donisimo')
string_info('Moscow')
is_contains('BananA', ['pop', 'France', 'banaNA'])
is_contains('don', ['Baksan', 'CS2', 'DONN'])
print(calls)
