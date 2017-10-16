
# Words that work:
# accomodation
# similitudinary
# accomodation


#Haiku rules (from https://www.howmanysyllables.com/english_grammar/poetry/haiku_rules)

#The lines must follow the 5-7-5 format:
#The first line must have 5 syllables.
#The second line must have 7 syllables.
#The third line must have 5 syllables.

#A haiku must express a mood, thought, or feeling.
#A haiku does not have to rhyme.
# ________________________________________________________________________________________

from textstat.textstat import textstat
import math
import os


def haiku_friend():
    haiku = []
    while True:
        line1 = raw_input("Enter the first line (5 syllables!) ")
        if math.ceil(textstat.syllable_count(line1)) == 5:
            haiku.append(line1)
            break
        else:
            print "Your line should contain exactly 5 syllables!"

    while True:
        line2 = raw_input("Enter the second line (7 syllables!) ")
        if math.ceil(textstat.syllable_count(line2)) == 7:
            haiku.append(line2)
            break
        else:
            print "Your line should contain exactly 7 syllables!"

    while True:
        line3 = raw_input("Enter the first line (5 syllables again!) ")
        if math.ceil(textstat.syllable_count(line3)) == 5:
            haiku.append(line3)
            break
        else:
            print "Your line should contain exactly 5 syllables!"

    os.system('clear')
    print "Here is your haiku:\n"
    print '\n'''.join(haiku)

    do_over = raw_input("\nPress any key to make another haiku, or press 'n' to leave :'( ")
    if do_over == 'n':
        quit()
    else:
        haiku_friend()


haiku_friend()
