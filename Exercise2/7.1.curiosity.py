import operator


# A class called Poll that represents a survey
class Poll:
    # The initialization operation will receive as a parameter the poll question,
    # and as an additional parameter an iterable with all voting options for the poll
    def __init__(self, question, iterable):
        self.question = question
        self.iterable = iterable
        self.votes = {vote: 0 for vote in iterable}

    # Accepts as a parameter a voting option for the poll and increases the number of votes in it by 1
    def vote(self, vote):
        if vote in self.votes:
            self.votes[vote] += 1
            return True
        return False  # Voting for an option that doesn't exist

    # Accepts as a parameter a voting option for the poll and adds it
    def add_option(self, vote):
        if vote in self.votes:  # Adding an option that already exists
            return False
        self.votes[vote] = 0
        return True

    # Accepts as a parameter a voting option for the poll and deletes it
    def remove_option(self, vote):
        if vote in self.votes:
            self.votes.pop(vote, None)
            return True
        return False  # Deleting an option that does not exist

    # Returns all options as a list of tuples, ordered by the number of votes
    def get_votes(self):
        dic = dict(sorted(self.votes.items(), key=operator.itemgetter(1), reverse=True))
        return [(i, dic.get(i)) for i in dic]

    # Returns the name of the option that received the most votes
    def get_winner(self):
        return max(self.votes, key=self.votes.get)


# -------------------------------- Checking that everything is working well -------------------------------------------

def cast_multiple_votes(poll, votes):
    for vote in votes:
        poll.vote(vote)


bridge_question = Poll('What is your favourite colour?', ['Blue', 'Yellow'])
cast_multiple_votes(bridge_question, ['Blue', 'Blue', 'Yellow'])
print(bridge_question.get_winner() == 'Blue')
cast_multiple_votes(bridge_question, ['Yellow', 'Yellow'])
print(bridge_question.get_winner() == 'Yellow')
print(bridge_question.get_votes() == [('Yellow', 3), ('Blue', 2)])
bridge_question.remove_option('Yellow')
print(bridge_question.get_winner() == 'Blue')
print(bridge_question.get_votes() == [('Blue', 2)])
bridge_question.add_option('Yellow')
print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])
print(not bridge_question.add_option('Blue'))
print(bridge_question.get_votes() == [('Blue', 2), ('Yellow', 0)])
