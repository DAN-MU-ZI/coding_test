from itertools import permutations

def solution(phone_book):
    answer = True
    
    hash_map = {k:1 for k in phone_book}
    
    for phone in phone_book:
        search = ''
        for p in phone:
            search+=p
            if search!=phone and search in hash_map:
                return False
    return answer