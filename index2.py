#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgi
import cgitb
cgitb.enable()

from random import randint, choice
import os
import pypokedex
import mysql.connector
from class_mysql import *


# Get last form data
donnees = cgi.FieldStorage()
# Get if last form was pass of smash
if (donnees.getvalue('Smash2') is None):
    smash2 = 0
    passed2 = 1
else:
    smash2 = 1
    passed2 = 0

if (donnees.getvalue('Smash1') is None):
    smash1 = 0
    passed1 = 1
else:
    smash1 = 1
    passed1 = 0
# Get what fusion mons was last fusion.
last_fusion1 = donnees.getvalue('last_fusion1')
last_fusion2 = donnees.getvalue('last_fusion2')

sql = mySqlAccount("fusion_scores2")

leaderboard = sql.find_leaderboard()
if last_fusion1 is not None:
    sql.update_account(str(last_fusion1), smash1, passed1)

if last_fusion2 is not None:
    sql.update_account(str(last_fusion2), smash2, passed2)


number_of_fused_poke = 0
list_of_fused_poke = sql.load_less_viewed_Fusions()

"""
path = "/var/www/html/cgi-enabled/Smash_or_Pass_Pokemon_fusion/indexed/"
dir_list = os.listdir(path)
for dir in dir_list:
    path2 = path+dir
    dir_list2 = os.listdir(path2)
    for image in dir_list2:
        list_of_fused_poke.append(image)

number_of_fused_poke = len(list_of_fused_poke)
random_fuse_poke = choice(list_of_fused_poke)
"""

index1 = randint(0, 800)
index2 = randint(0, 800)
random_fuse_poke1 = list_of_fused_poke[index1][0]
list_of_fused_poke.pop(index1)
random_fuse_poke2 = list_of_fused_poke[index2][0]

defuse1 = random_fuse_poke1.split('.')
first1 = defuse1[0]
second1 = defuse1[1]

defuse2 = random_fuse_poke2.split('.')
first2 = defuse2[0]
second2 = defuse2[1]

for i in range(25):
    second1 = second1.split(chr(ord("a")+i))[0]

for i in range(25):
    second2 = second2.split(chr(ord("a")+i))[0]


print ("Content-Type: text/html")
print ("")


for i in range(1,40):
    print("""<img src="indexed/{}">""".format(str(leaderboard[i][0].split('.')[0])+"/"+leaderboard[i][0]))


print("""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>Pokemon Infinite Fusion Smash or Pass</title>
    <link rel="stylesheet" type="text/css" href="css2.css">
</head>
<body>""")
print("""
      <div class="box">
      <div class="poke1">
      <p class="fusion_name1"> Fusion between : </p>
      <parents class="parents1"><img class="parents_imgs1" src="pokemon/{}.png">
      <img class="parents_imgs1" src="pokemon/{}.png"></parents>
      <img class="fusion_img1" src="{}">
      <buttons class="buttons1">
      <form action ="index2.py" method="post">
          <input type="hidden" id="last_fusion1" name="last_fusion1" value="{}">
          <button type="submit" id="Smash1" name="Smash1" value="0"> Smash </button>
      </buttons>
      </div>
""".format(str(first1),str(second1),"indexed/"+first1+"/"+random_fuse_poke1, random_fuse_poke1))

print("""
      <div class="poke2">
      <p class="fusion_name2"> Fusion between : </p>
      <parents class="parents2"><img class="parents_imgs2" src="pokemon/{}.png">
      <img class="parents_imgs2" src="pokemon/{}.png"></parents>
      <img class="fusion_img2" src="{}">
      <buttons class="buttons2">
      <form action ="index2.py" method="post">
          <input type="hidden" id="last_fusion2" name="last_fusion2" value="{}">
          <button type="submit" id="Smash2" name="Smash2" value="0"> Smash </button>
      </buttons>
      </div>
      </div>
""".format(str(first2),str(second2),"indexed/"+first2+"/"+random_fuse_poke2, random_fuse_poke2))
print("""
      </body>
      </html>
      """)
