given_str = 'adn post act and cat will tac '

str_list = given_str.split()
print(str_list)


sorted_list = []
for word in str_list :
  word = ''.join(sorted(word))
  sorted_list.append(word)

# print(sorted_list)

ans_dict = {}
i = 0;
for word in sorted_list:
  if word in ans_dict.keys():
    # print(word + ' present in dict')
    ans_dict[word] = str(ans_dict[word])
    ans_dict[word] += str(i)
  else:
    ans_dict[word] = None
  i = i + 1
print(ans_dict)

for key, value in ans_dict.items():
  if value is not None:
    # print(value)
    # print(len(value))
    angr_list = key + ' '
    for i in range(4, len(value)):
      index = int(value[i])
      angr_list += str_list[index] + ' '
      # print('index is : {}'.format(index))
      # print(str_list[int(value[i])])
      # angr_list += str_list[int(value[i])] + ', '
    # print(angr_list  + ' are anagrams')
    print('Anangrams:- {}'.format(angr_list))
  

