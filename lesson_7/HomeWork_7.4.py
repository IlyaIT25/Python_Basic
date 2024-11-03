def common_elements():
    # кратние 3
    multiples_of_3 = {x for x in range(100) if x % 3 == 0}

    # кратные 5
    multiples_of_5 = {x for x in range(100) if x % 5 == 0}

    #  & - пересечение величин
    intersection = multiples_of_3 & multiples_of_5
    return intersection

print(common_elements())