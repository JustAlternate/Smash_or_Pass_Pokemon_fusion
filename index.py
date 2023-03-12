#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgi
import cgitb
cgitb.enable()

from random import randint, choice
import os
import mysql.connector
from class_mysql import *


# Get last form data
donnees = cgi.FieldStorage()
smash = 0
# Get if last form was pass of smash
if (donnees.getvalue('Smash') is None):
    smash = 0
    passed = 1
else:
    smash = 1
    passed = 0
# Get what fusion mons was last fusion.
last_fusion = donnees.getvalue('last_fusion')

sql = mySqlAccount("fusion_scores2")

leaderboard = sql.find_leaderboard()
if last_fusion is not None:
    sql.update_account(str(last_fusion), smash, passed)


list_of_fused_poke = sql.load_all_less_viewed_Fusions()

"""
path = "/var/www/html/cgi-enabled/Smash_or_Pass_Pokemon_fusion/indexed/"
dir_list = os.listdir(path)
for dir in dir_list:
    path2 = path+dir
    dir_list2 = os.listdir(path2)
    for image in dir_list2:
        sql.maj_account(str(image), 0, 0)
        list_of_fused_poke.append(image)
number_of_fused_poke = len(list_of_fused_poke)
random_fuse_poke = choice(list_of_fused_poke)
"""

random_fuse_poke = choice(list_of_fused_poke)[0]
defuse = random_fuse_poke.split('.')
first = defuse[0]
second = defuse[1]

for i in range(25):
    second = second.split(chr(ord("a")+i))[0]

print ("Content-Type: text/html")
print ("")

print("""
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8" />
    <title>Pokemon Infinite Fusion Smash or Pass</title>
    <link rel="stylesheet" type="text/css" href="css.css">
</head>
<body>""")
print("""
      <div>
      <p class="fusion_name"> Fusion between : </p>
      <parents><img class="parents_imgs" src="pokemon/{}.png">
      <img class="parents_imgs" src="pokemon/{}.png"></parents>
      <img class="fusion_img" src="{}">
      <buttons>
      <form action ="index.py" method="post">
          <input type="hidden" id="last_fusion" name="last_fusion" value="{}">
          <button type="submit" id="Pass" name="Pass" value="1"> Pass </button>
          <button type="submit" id="Smash" name="Smash" value="0"> Smash </button>
      </buttons>
      </div>
      <p> Leaderboard </p>
""".format(str(first),str(second),"indexed/"+first+"/"+random_fuse_poke, random_fuse_poke))
for i in range(1,1):
    print("""
          <img src="indexed/{}">""".format(str(leaderboard[i][0].split('.')[0])+"/"+leaderboard[i][0]))

print("""
      </body>
      </html>
      """)
