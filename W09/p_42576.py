from collections import Counter

def solution(participant, completion):
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    
    not_completed = participant_count - completion_count
    
    return list(not_completed.keys())[0]
