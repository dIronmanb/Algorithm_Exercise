import sys
read = sys.stdin.readline

N = int(input())
words = []
for i in range(N):
    words.append(read().rstrip())

def is_group(word):
    '''
        :param word: 단어
        :return: group word가 맞는지 아닌지를 판단

        Q: 여기서 more tight coding은 불가능한 것인가???
    '''
    alphabet_list = dict()

    if word[0] not in alphabet_list.keys():
        alphabet_list[word[0]] = 0

    for idx in range(0, len(word)-1):
        if word[idx] not in alphabet_list.keys():
            alphabet_list[word[idx]] = 0
        else:
            # 속해있는 알파벳 && 이미 1이 된 상태이면
            if alphabet_list[word[idx]] == 1:
                return False

        # 다음 단어와 현재 단어가 다르면
        if word[idx] != word[idx+1]:
            alphabet_list[word[idx]] = 1

    # 마지막 단어까지 보고 확인
    if word[-1] not in alphabet_list.keys():
        alphabet_list[word[-1]] = 0

    if alphabet_list[word[len(word)-1]] == 1:
        return False

    return True

cnt = 0
for word in words:
    cnt += is_group(word=word)
    # print(word)

print(cnt)



