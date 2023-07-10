
# 슬라이딩 윈도우 알고리즘을 사용하여 문제를 해결. 
def solution(sequence, k):
    start = 0  # 시작index 저장
    end = 0    # 끝index 저장
    current_sum = sequence[0]  # 원소들의 합을 저장
    result = [0, len(sequence)-1]  # 가장 짧은 수열 부분의 시작과 끝 인덱스

    while end < len(sequence):  # end 인덱스가 수열 끝에 도달 할 때까지 실행!
        if current_sum == k:  # current_sum이 우리가 찾는 합 'k'와 같은지 확인
            if end - start < result[1] - result[0]:  # 현재 찾은 수열의 시작과 끝이 기존 수열의 길이보다 짧은지 확인 (end - start) 
                result = [start, end]  # 짧으면 값을 갱신
            current_sum -= sequence[start]  # strat 인덱스에 있는 값을 빼준다.
            start += 1  # 윈도우의 start값이 오른쪽으로 이동 (윈도우 축소)
        elif current_sum < k:  # current_sum이 우리가 찾는 합 'k'보다 작을때
            end += 1  # 윈도우의 end값을 오른쪽으로 이동 (윈도우 확대)
            if end < len(sequence):  # 수열의 총 길이보다 작으면
                current_sum += sequence[end]  # 원소들의 합에 추가
        else:  # current_sum이 우리가 찾는 합 'k'보다 큰 경우
            current_sum -= sequence[start]  # start 인덱스에 있는 값을 빼준다.
            start += 1  # start 값을 오른쪽으로 이동
            
    return result

