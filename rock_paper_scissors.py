def play():
    user = input("what is your choice?? 'r' for rock, 's' for scissors and 'p' for paper")
    computer = random.choice(['r', 's', 'p'])
    print(computer)
    if user == computer:
        return "it\'s a tie"

    if is_win(user, computer):
        return "You won"

    return 'you lost'

def is_win(user, computer):
    # r>s,s>p,p>r
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') \
        or (user == 'p' and computer == 'r'):
        return True
print(play())
