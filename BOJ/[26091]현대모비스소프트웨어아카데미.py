#현대모비스 소프트웨어 아카데미 [Silver 1]
import sys
I = sys.stdin.readline

# 1. 오름 차순 정렬 한다
# 2. 양 끝에 포인터를 둔다
# 3. 만약 두 포인터의 학생이 m을 못넘긴다? => 작은 쪽의 학생은 누구와 팀을 이루어도 절대 통과하지 못하기 떄문에 버린다
# 4. 넘기면 팀을 이루도록 한다.
# 5. 4번은 항상 옳다.
# ex) 1 2 3 4 5 8 있고 m = 8 일 때,
#  1과8은 팀을 이루어 통과 => 다음 포인터 2와 5, 이 둘은 통과x
# 만약 이를 위해 2와 8을 팀을 이룬다면? 앞의 1은 누구와도 통과 못함 => 결국 4번과 같은 결과를 낸다.

def main():
    result = 0
    n, m = map(int, I().split())
    a = list(map(int, I().split()))
    a.sort()

    left, right = 0,len(a)-1

    while (left < right):
        if a[left]+a[right] >= m:
            left += 1
            right -= 1
            result += 1

        else:
            left += 1

    return result

print(main())