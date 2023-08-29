'''
포켓몬 GO
'''

N = int(input()) # 포켓몬 마릿수
pokemons = []    # 이름, 진화횟수 리스트
total_evolve_count = 0 # 총 진화가능 횟수 

for _ in range(N):
    name = input().strip() # 이름
    K, M = map(int, input().split()) # 진화시 필요한 사탕 수, 가지고있는 사탕 수 
    evolve_count = 0 # 진화 횟수 count

    while M >= K: # 가지고 있는사탕이 같거나 더 많으면 진행
        M -= K # 진화시 필요한 사탕을 차감
        M += 2 # 돌려받는 사탕 +2
        evolve_count += 1 # 진화 횟수 +1

    total_evolve_count += evolve_count # 총 진화 가능횟수 += 진화횟수 
    pokemons.append((name, evolve_count)) # 이름과 횟수를 튜플로 저장

# 포켓 몬 중 'x[1]' 즉 튜플의 두번째에 들어있는 횟수 중 가장 높은 값을 찾고, '[1]' 두번째 값만 추출하여 값을 반환 
max_evolve = max(pokemons, key=lambda x: x[1])[1]

# if문 조건이 참일때, name을 반환
max_evolve_pokemon = next(name for name, count in pokemons if count == max_evolve)

print(total_evolve_count) # 총 진화가능 횟수
print(max_evolve_pokemon) # 가장많이 진화 할 수 있는 포키몬 이름
