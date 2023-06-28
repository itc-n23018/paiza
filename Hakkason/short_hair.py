def repeat_string(N, S):
    return "\n".join([S] * 3)


N = int(input())
S = input()

short_hair = repeat_string(N, S)
print(short_hair)
