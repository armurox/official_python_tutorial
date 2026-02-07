#!/usr/bin/env python3
users = {'Arman': 'active', 'Bob': 'inactive', 'Jill': 'active'}

# Strategy 1: Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# Strategy 2: Generate a new copy
users = {'Arman': 'active', 'Bob': 'inactive', 'Jill': 'active'}
active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)