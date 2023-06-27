def repeat_string(N, S):


N = int(input())
S = input()

short_hair = repeat_string(N, S)
return '\n'.join([S] * N)
print(short_hair)
