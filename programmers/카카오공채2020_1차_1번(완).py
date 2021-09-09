def solution(new_id):
    # 1
    new_id = new_id.lower()
    # 2
    remove_id = '~!@#$%^&*()=+[{]}:?,<>/'
    new2_id = ''
    for a in new_id:
        if a not in remove_id:
            new2_id += a
    if new2_id == '':
        new2_id = new_id
    # 3
    # 이런식으로 간단히 구현가능능    # while '..' in answer:
    #     answer = answer.replace('..', '.')
    # new3_id = ''
    i = 0
    while i < len(new2_id):
        if new2_id[i] == '.':
            while i < (len(new2_id) - 1) and new2_id[i + 1] == '.':
                i += 1

            new3_id += '.'
        else:
            new3_id += new2_id[i]
        i += 1

    # 4
    # if answer[0] == '.':
    #     answer = answer[1:] if len(answer) > 1 else '.'
    # if answer[-1] == '.':
    #     answer = answer[:-1]
    new4_id = ''
    if new3_id[0] == '.':
        new4_id += new3_id[1:-1]
    else:
        new4_id += new3_id[:-1]
    if new3_id[-1] != '.':
        new4_id += new3_id[-1]

    # 5
    if len(new4_id):
        new5_id = new4_id
    else:
        new5_id = 'a'
    # 6
    new6_id = ''
    if len(new5_id) >= 16:
        new6_id += new5_id[:14]
        if new5_id[14] != '.':
            new6_id += new5_id[14]
    else:
        new6_id = new5_id

    # 7
    # while len(answer) < 3:
    #     answer += answer[-1]
    new7_id = ''
    if len(new6_id) <= 2:
        new7_id += new6_id
        while len(new7_id) < 3:
            new7_id += new6_id[-1]
    else:
        new7_id = new6_id

    answer = new7_id
    return answer
