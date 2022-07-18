# -*- coding: utf-8 -*-
import datetime

default_banned_words = ["@everyone", "@here", "awordfordynoautomodtest"]
default_banned_words.extend(["CSGO", "CS:", "CS GO"])
# default_banned_words.extend(["discord nitro"])
# default_banned_words.extend(["giveaway", "give out", "gives out", "giving out"])

nouns = ["nitro", "discord nitro", "gift", "airdrop", "case", "giveaway", "subscription"] #promotion
premods = ["free", "distributed", "shared", "months of", "month of", "month", "months", "distribution of"]
postmods = ["free", "for free", "giveaway", "distribution", "from discord", "for 3 month", "for 1 month", "for a month", "from steam", "by steam", "with steam", "for you", "for u", "is for you", "is for u", "are for you", "are for u", "is handed", "are handed", "is distributed", "are distributed", "from Picsart"]
verbs = ["give out", "gives out", "giving out", "give away", "gives away", "giving away", "get", "gets", "getting", "got", "take", "give"]

banned_phrases = ["i am going to the army", "you can take all my skins", "steam gives away", "steam is giving away", "test my first game"]
banned_phrases.extend(["steam give", "steam is giving", "steam gave", "steam distribute", "steam is distributing"])
banned_phrases.extend(["activation key"])
banned_phrases.extend(["download link"])

banned_words = []
banned_words.extend(default_banned_words)
for noun in nouns:
    for modnoun in nouns:
        banned_word = noun + " " + modnoun
        banned_words.append(banned_word)
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
        banned_word = verb + " this " + noun
        banned_words.append(banned_word)
        banned_word = verb + " some " + noun
        banned_words.append(banned_word)
        banned_word = verb + " any " + noun
        banned_words.append(banned_word)

#for premod in premods:
#    for modpremod in premods:
#        banned_word = premod + " " + modpremod
#        banned_words.append(banned_word)

#for postmod in postmods:
#    for modpostmod in postmods:
#        banned_word = postmod + " " + modpostmod
#        banned_words.append(banned_word)
        
        
banned_words.extend(banned_phrases)

list_for_dyno = ""
for banned_word in banned_words:
    list_for_dyno = list_for_dyno + "," + banned_word
list_for_dyno = list_for_dyno[1:]

timestamp = datetime.datetime.now()
list_for_dyno = list_for_dyno + "," + "Last modified " + timestamp.strftime('%Y-%m-%d %H:%M:%S.%f')

# print(list_for_dyno)

readme_md = "単体禁止ワード\n>" + str(default_banned_words) + "\n\n疑惑名詞\n>" + str(nouns) + "\n\n疑惑修飾(前置)\n>" + str(premods) + "\n\n疑惑修飾(後置)\n>" + str(postmods) + "\n\n疑惑動詞\n>" + str(verbs)+ "\n\n単体禁止フレーズ\n>" + str(banned_phrases)+ "\n\nDyno向け禁止ワードリスト\n>" + list_for_dyno


with open("README.MD","w") as text_file:
    text_file.write(readme_md)
print(readme_md)
