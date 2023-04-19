# Se o nome começar com R ou r, você toca o banjo!

def are_you_playing_banjo(name):
    return name + " plays banjo" if name[0] in "Rr" else name + " does not play banjo"


print(are_you_playing_banjo("Rafael"))
print(are_you_playing_banjo("rafael"))
print(are_you_playing_banjo("Jafa"))
print(are_you_playing_banjo("Jafa"))
