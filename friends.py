# ask user for a list of three friends
# For each friend we'll tell the user whether they are nearby
# for each nearby friend, we'll save them to the nearby_friend.text file

friends = input("Enter the name of three friends, separated by commas (no spaces please): ").split(',')

people = open('people.txt', 'r')
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)
friends_nearby_set = friends_set.intersection(people_nearby)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby! Meet up with them.')
    nearby_friends_file.write(f'{friend}\n')


nearby_friends_file.close()