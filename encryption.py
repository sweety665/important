#  THis will encrypt
#
# message= input("Enter the message to Decrypt: ")
# key= int(input("Enter the key: "))
# words= list(message)
# for i in range(len(words)):
#     ch= words[i]
#     # print(ch)
#     if (ch>'a') and (ch<'z'):
#         i-= key
#         if (ch<'a'):
#             i+= 'z'-'a'+1
#         words[i] =ch
#     elif (ch>='A') and (ch<='Z'):
#         i-= key
#         if(ch> 'a'):
#             i+='Z'-'A'+1
#         words[i]= ch
#
# for i in range(len(words)):
#     print(words[i],end='')


# message= input("Enter the message to encrypt: ")
# key= int(input("Enter the key: "))
# words= list(message)
# for i in range(len(words)):
#     ch= words[i]
#     # print(ch)
#     if (ch>'a') and (ch<'z'):
#         i+= key
#         if (ch>'z'):
#             i-= 'z'+'a'-1
#             print(i)
#         words[i] =ch
#     elif (ch>='A') and (ch<='Z'):
#         i+= key
#         if(ch> 'Z'):
#             i-='Z'+'A'-1
#         words[i]= ch
#
# for i in range(len(words)):
#     print(words[i],end='')