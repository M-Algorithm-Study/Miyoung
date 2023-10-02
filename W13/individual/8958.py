t = int(input())

for _ in range(t):
    quiz_results = input().strip() 
    score = 0 
    count = 0 

    for result in quiz_results:
        if result == 'O': 
            count += 1
            score += count
        else:  
            count = 0
    
    print(score)
