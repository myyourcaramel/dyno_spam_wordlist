default_banned_words = ["@everyone", "@here", "awordfordynoautomodtest", "CSGO", "CS:GO"]

nouns = ["nitro", "discord nitro", "gift", "giveaway", "airdrop", "case"]
adjs = ["free", "for free", "giving out", "giveaway", "distribution"]

banned_words = default_banned_words
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

print(list_for_dyno)

with open("README.MD","w") as text_file:
    text_file.write("> " + list_for_dyno)

