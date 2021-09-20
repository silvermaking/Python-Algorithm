'''
list.sort()로 문자열 정렬
stack으로 2개씩 짝짓기
"".join()
'''

T = int(input())
for tc in range(1, T+1):
    word = list(input())
    word.sort()  # 문자 정렬
    ST = []

    for w in word:
        if ST and ST[-1] == w:
            ST.pop()
        else:
            ST.append(w)

    if ST:
        print(f'#{tc} {"".join(ST)}')
    else:
        print(f'#{tc} Good')