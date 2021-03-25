word = input("Введите текст: ")
vowel = 'aouiey'
vowel_counter = {}

for char in word:
  if char in vowel:
    vowel_counter[char] = vowel_counter.setdefault(char,0)+1

sorted_result = sorted(vowel_counter.items(), reverse=True,key=lambda x : x[1])

for key,val in sorted_result:
  print(key,val)