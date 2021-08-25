# -*- coding: utf-8 -*-

default_banned_words = ["@everyone", "@here", "awordfordynoautomodtest"]
default_banned_words.extend(["discord nitro", "for free", "CSGO", "CS:GO" ])
default_banned_words.extend(["giveaway", "give out", "gives out", "giving out"])

nouns = ["nitro", "gift", "airdrop", "case"]
adjs = ["free", "distribution"]

banned_words = []
banned_words.extend(default_banned_words)
for noun in nouns:
    for adj in adjs:
        banned_word = noun + " " + adj
        banned_words.append(banned_word)
        banned_word = noun + "s " + adj
        banned_words.append(banned_word)
        banned_word = adj + " " + noun
        banned_words.append(banned_word)

list_for_dyno = ""
for banned_word in banned_words:
    list_for_dyno = list_for_dyno + "," + banned_word
list_for_dyno = list_for_dyno[1:]

 # print(list_for_dyno)

readme_md = "単体禁止ワード\n>" + str(default_banned_words) + "疑惑名詞\n>" + str(nouns) + "疑惑修飾\n>" + str(adjs) + "Dyno向け禁止ワードリスト\n>" + list_for_dyno


with open("README.MD","w") as text_file:
    text_file.write(readme_md)
print(readme_md)
