N = int(input())
pokemons = []
total_evolve_count = 0

for _ in range(N):
    name = input().strip()
    K, M = map(int, input().split())
    evolve_count = 0

    while M >= K:
        M -= K
        M += 2
        evolve_count += 1

    total_evolve_count += evolve_count
    pokemons.append((name, evolve_count))

# 모든 포켓몬 중에서 진화시킬 수 있는 최대 횟수를 찾습니다.
max_evolve = max(pokemons, key=lambda x: x[1])[1]

# 최대 횟수로 진화시킬 수 있는 포켓몬 중에서 처음으로 나오는 포켓몬을 선택합니다.
max_evolve_pokemon = next(name for name, count in pokemons if count == max_evolve)

print(total_evolve_count)
print(max_evolve_pokemon)
