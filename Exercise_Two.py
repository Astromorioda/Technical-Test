from Exercise_One import max_number

def max_of_three(n1: int, n2: int, n3: int):
    
    n = max_number(n1, n2)
    n_total = max_number(n, n3)
    
    return n_total
