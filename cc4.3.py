"""
---------------------------------------------------------------------------
Day04: Randomisation and Python Lists[Beginner]
Code Challenge 4.2: Treasure Map
Things to learn:
    - Variable, input()
    - List Method: list() - to convert string to list
    - String reverse by slice notation [::-1]
---------------------------------------------------------------------------
"""
row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']
treasure_map = [row1, row2, row3]
print(f'{row1}\n{row2}\n{row3}\n')

position = input('Where do you wanna put the treasure?\n')
new_position = position[::-1]

rc_pos = list(new_position)
treasure_map[int(rc_pos[0])-1][int(rc_pos[1])-1] = 'X'
# print(rc_pos)
# print(treasure_map[int(rc_pos[0])-1][int(rc_pos[1])-1])

print(f'{row1}\n{row2}\n{row3}\n')
