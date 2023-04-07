def overlap(list1: list, list2: list):
    for element1 in list1:
        for element2 in list2:
            if element1 == element2:
                return True
            
    return False
