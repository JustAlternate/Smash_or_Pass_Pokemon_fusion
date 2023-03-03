from random import randint, choice
import os

number_of_fused_poke = 0
list_of_fused_poke = []

path = "/home/justalternate/Projects/Tinder_Poke_Fusion/indexed/"
dir_list = os.listdir(path)

for dir in dir_list:
    path2 = path+dir
    dir_list2 = os.listdir(path2)
    for image in dir_list2:
        list_of_fused_poke.append(image)

number_of_fused_poke = len(list_of_fused_poke)

random_fuse_poke = choice(list_of_fused_poke)

defuse = random_fuse_poke.split('.')
first = defuse[0]
second = defuse[1]
second = second.split("a")[0]
second = second.split("b")[0]
second = second.split("c")[0]

print(random_fuse_poke)
print(first, second)
