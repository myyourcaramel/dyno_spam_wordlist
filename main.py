# -*- coding: utf-8 -*-

default_banned_words = ["@everyone", "@here", "awordfordynoautomodtest"]
default_banned_words.extend(["CSGO", "CS:GO"])
# default_banned_words.extend(["discord nitro"])
# default_banned_words.extend(["giveaway", "give out", "gives out", "giving out"])

nouns = ["nitro", "discord nitro", "gift", "airdrop", "case", "giveaway"]
premods = ["free", "distributed"]
postmods = ["free", "for free", "giveaway"]
verbs = ["give out", "gives out", "giving out", "give away", "gives away", "giving away"]

banned_words = []
banned_words.extend(default_banned_words)
for noun in nouns:
    for premod in premods:
        banned_word = premod + " " + noun 
        banned_words.append(banned_word)
    for postmod in postmods:
        banned_word = noun + " " + postmod
        banned_words.append(banned_word)
        banned_word = noun + "s " + postmod
        banned_words.append(banned_word)
    for verb in verbs:
        banned_word = verb + " " + noun
        banned_words.append(banned_word)
        banned_word = verb + " the " + noun
        banned_words.append(banned_word)

list_for_dyno = ""
for banned_word in banned_words:
    list_for_dyno = list_for_dyno + "," + banned_word
list_for_dyno = list_for_dyno[1:]

# print(list_for_dyno)

readme_md = "単体禁止ワード\n>" + str(default_banned_words) + "\n\n疑惑名詞\n>" + str(nouns) + "\n\n疑惑修飾(前置)\n>" + str(premods) + "\n\n疑惑修飾(後置)\n>" + str(postmods) + "\n\n疑惑動詞\n>" + str(verbs)+ "\n\nDyno向け禁止ワードリスト\n>" + list_for_dyno


with open("README.MD","w") as text_file:
    text_file.write(readme_md)
print(readme_md)
