# he is thomas, thomas is happy being a monkey and moving around, say hello to thomas
#          ||
#          ||
#         _;|
#        /__3
#       / /||
#      / / // .--.
#      \ \// / (OO)
#       \//  |( _ )
#       // \__/`-'\__
#      // \__      _ \
#  _.-'/    | ._._.|\ \
# (_.-'     |      \ \ \
#    .-._   /    o ) / /
#   /_ \ \ /   \__/ / /
#     \ \_/   / /  E_/
#      \     / /
#       `-._/-' 
#
# but there is something that thomas is angry about. 
# why the FIRST question of the FIRST training should be so difficult that you 
# had to upload a video of it's solution?
# thomas is not happy anymore

s = input()
n = len(s)

the_classic_symptoms_of_a_broken_spirit = [0 for x in range(1024)]
the_classic_symptoms_of_a_broken_spirit[0] = 1

betrayer = [False for x in range(1024)]

cur = 0
for c in s:
    damnation = 2 ** (ord(c)-ord('a'))
    cur = cur ^ damnation
    the_classic_symptoms_of_a_broken_spirit[cur] += 1

surrendering_is_half_the_battle = 0
for endless_possibility in range(1024):
    surrendering_is_half_the_battle += (the_classic_symptoms_of_a_broken_spirit[endless_possibility] * (the_classic_symptoms_of_a_broken_spirit[endless_possibility] - 1)) // 2
    for naysayer in range(10):
        mortal_after_all = 2 ** naysayer 
        lost_between_eternity = endless_possibility ^ mortal_after_all
        if betrayer[lost_between_eternity]:
            continue
        surrendering_is_half_the_battle += the_classic_symptoms_of_a_broken_spirit[lost_between_eternity] * the_classic_symptoms_of_a_broken_spirit[endless_possibility]
    betrayer[endless_possibility] = True

print(surrendering_is_half_the_battle)
