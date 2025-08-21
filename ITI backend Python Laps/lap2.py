# def longest_alphabetical_substring(s):
#     longest = ""
#     current = ""
#     for i in range(len(s)):
#         if i == 0 or s[i] >= s[i - 1]:
#             current += s[i]
#         else:
#             current = s[i]
#         if len(current) > len(longest):
#             longest = current
#     print(f"Longest substring in alphabetical order is: {longest}")
# longest_alphabetical_substring("abcdefghijAmr")

# -------------------------------------------------------------------------------------

# total=0
# count=0
# while True:
#     numper=input("enter a numper: ")
#     if numper.lower()=="done":
#         break
#     else:
#         total +=int(numper)
#         count +=1
# if count!=0:
#     avr=total/count

# print(f"the count of numpers you entered is:{count}")
# print(f"the total of numpers you entered is:{total}")
# print(f"the avarege of numpers you entered is:{avr}")

#---------------------------------------------------------------------------------------
# import random
# words=["apple","orange","banana","watermelon"]
# name=input(f"enter your name: ")
# print(f"welcom {name} ready for play hangman game!")
# word=random.choice(words)
# guesses=''
# turns=7
# while turns>0:
#     guess=input(f"you have {turns} turns guess any alphabet: ").lower()
#     guesses += guess
#     missed=0
#     for char in word:
#         if char in guesses:
#             print(f"{char} ",end="")
#         else:
#             print("_ ",end="")
#             missed+=1
#     print()
#     if missed == 0:
#         print("congratulations you guessed the word")
#         break
#     if guess not in word:
#             turns -= 1
#             print("Wrong guess.")
#             print(f"You have {turns} turns left.")

#             if turns == 0:
#                 print(f"Game Over. The word was: {word}")
#                 break


#---------------------------------------------------------------------------------------


# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# print(twoSum([1,3,5,6],7))


#------------------------------------------------------------------------------------------


arr=[]
n=int(input("enter the numper of nums you want to in :"))
for i in range(n):
    arr+=input(f"write numper {i+1} in the array:")
x=0
for k in range(n):
    for j in range(k):
        if arr[k]==arr[j]:
            x+=1
if x==0:
    print("False")
else:
    print("true")
            