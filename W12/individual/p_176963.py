def solution(name, yearning, photo):
    yearning_dict = dict(zip(name, yearning))

    result = []

    for p in photo:
        memory_score = 0

        for person in p:
            memory_score += yearning_dict.get(person, 0)

        result.append(memory_score)

    return result
