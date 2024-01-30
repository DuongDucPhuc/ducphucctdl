def are_anagrams(tuso1, tuso2):
    lower_tuso1 = tuso1.lower()
    lower_tuso2 = tuso2.lower()
    if len(lower_tuso1) != len(lower_tuso2):
        return False
    sorted_tuso1 = sorted(lower_tuso1)
    sorted_tuso2 = sorted(lower_tuso2)
    return sorted_tuso1 == sorted_tuso2
n = are_anagrams("ducphuc", "pduchuc")
print(n)
