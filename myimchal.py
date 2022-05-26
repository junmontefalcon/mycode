#!/usr/bin/env python3
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]
print(challenge)
print("My", challenge[2][1], "! The", challenge[2][0],"do",challenge[3],"!" )
print(" ")

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]
print(trial)
print(trial[2].values())

print("My", trial[2].get("goggles"), "! The", trial[2].get("eyes"),"do",trial[3],"!" )
print(" ")

#My eyes! The goggles do nothing!
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 16, "d": "nothing"}]

print(nightmare)
print(nightmare[0]["user"]["name"]["first"])
print(nightmare[0]["kumquat"])
print(nightmare[0]["d"])
print(nightmare[0].get("d"))

a= nightmare[0]["user"]["name"]["first"]
b= nightmare[0]["kumquat"]
c= nightmare[0]["d"]

print("My", a, "! The", b, "do",nightmare[0].get("d"),"!" )
