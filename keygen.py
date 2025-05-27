# при запуске этот файл создаст новые уникальные ключи безопасности

import random
list_of_ready_keygens = []
repeat_count = 0
while True:
    random_list = [1,2]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','v','w','x','y','z']
    absolute_random_numera = ''
    for repeat in range(100):
        choice = random.choice(random_list)
        if choice == 1:
            absolute_random_numera += str(random.choice(numbers))
        if choice == 2:
            absolute_random_numera += random.choice(alphabet)
    if absolute_random_numera not in list_of_ready_keygens:
        list_of_ready_keygens.append(absolute_random_numera)
        repeat_count += 1
    if repeat_count >= 1000:
         break
with open('turmsek/turmsek_pochti_gotoviy/keys.txt', 'w', encoding='utf-8') as f:
        f.write(str(list_of_ready_keygens))
print(list_of_ready_keygens)