# TUPLES AS DICTIONARY KEYS
priority_index = {
    (1, "premier"): [1, 34, 12],
    (1, "mvp"): [84, 22, 24],
    (2, "standard"): [93, 81, 3]
}

print(list(priority_index.keys()))      # [(1, 'premier'), (1, 'mvp'), (2, 'standard')]

"""
this is usually done because is a great way to add some extra information to
the dictionary key

For example, following the above example, we can use those tuple keys to
indicate if they are courses of 1 or 2 parts, and using a loop we could select
only those items with 2 parts
"""



# MERGE LISTS IN ONE TUPLE -> zip()
# this is a way of combining data from different lists into one tuple
positions = ["2b", "3b", "ss", "dh"]
players = ["Altuve", "Bregman", "Correa", "Gattis"]

scoreboard = zip(positions, players)
print(scoreboard)                       # <zip object at 0x000001F282D9C300>
print(list(scoreboard))                 # [('2b', 'Altuve'), ('3b', 'Bregman'), ('ss', 'Correa'), ('dh', 'Gattis')]



# SETS (data type)
# they are like lists, but don't save duplicated element
tags = {"python", "coding", "tutorial", "coding"}
print(tags)                             # {'python', 'tutorial', 'coding'}

# ACCESS TO ELEMENTS
# print(tags[0]) -> nope
query_one = "python" in tags
query_two = "ruby" in tags
print(query_one)                        # True
print(query_two)                        # False
# we will have to check if the item is in the set and then print its name



# MERGE SETS -> we'll see they have unique items
tags_one = {
    "python",
    "coding",
    "tutorials",
    "coding"
}

tags_two = {
    "ruby",
    "coding",
    "tutorials",
    "development"
}

# merged tags -> takes all the elements in both sets and merges them into one single set
merged_tags = tags_one | tags_two           # | -> merges the two sets
print(merged_tags)                          # {'tutorials', 'ruby', 'development', 'python', 'coding'}

# tags in tags_one but not in tags_two
exclusive_to_tag_one = tags_one - tags_two  # select those elements in tags_one that are not in two
print(exclusive_to_tag_one)                 # {'python'}

# tags in tags_two but not in tags_one
exclusive_to_tag_two = tags_two - tags_one  # select those elements in two that are not in one
print(exclusive_to_tag_two)                 # {'development', 'ruby'}

# tags found in both tags_one and tags_two
universal_tags = tags_one & tags_two        # & -> takes elements that are in both sets
print(universal_tags)                       # {'coding', 'tutorials'}