import copy
import os

current_dir = os.path.dirname(__file__)
input = os.path.join(current_dir, 'input.txt')
hands = []


class Hand:
    def __init__(self, bid, cards_str):
        self.cards = self.create_cards_from_str(cards_str)
        self.score = 0
        self.values = []
        self.bid = bid
        self.value = 0
    
    def create_cards_from_str(self, cards_str):
        """
        """
        cards = []
        for c in cards_str:
            if c == 'A':
                cards.append(hex(14))
            elif c == 'K':
                cards.append(hex(13))
            elif c == 'Q':
                cards.append(hex(12))
            elif c == 'J':
                cards.append(hex(1))
            elif c == 'T':
                cards.append(hex(10))
            else:
                cards.append(hex(int(c)))
        return cards
    
    def flatten_cards(self):
        """
        create a string from the cards, without 0x
        """
        cards = ''
        for card in self.cards:
            cards += str(card)[2:]
        return cards
    
    def calculate_score(self):
        """
        - Five of a kind
        - Four of a kind
        - Full house
        - Three of a kind
        - Two pair
        - One pair
        - High card
        """
        self.score = int(self.flatten_cards(), 16)
        # print(self.score)
        cards = copy.copy(self.cards)
        cards.sort(reverse=True)
        
        for card in cards:
            if card != hex(1):
                self.values.append((cards.count(card), card))

        # replace 1 with highest value and add to count
        for i in range(0, len(self.values)):
            if self.values[i][1] == hex(1):
                self.values[0] = (self.values[0][0] + 1, self.values[0][1])
        
        # remove duplicates
        self.values = list(set(self.values))
        # sort by count and value (first by count, then by value)
        self.values.sort(key=lambda x: (x[0], x[1]), reverse=True)
        # print(self.values)
        # check for five of a kind
        if len(self.values) == 0:
            self.score = self.score ** 10000
        else:
            if self.values[0][0] == 5:
                self.score = self.score ** 10000
        
            # check for four of a kind
            if self.values[0][0] == 4:
                self.score = self.score ** 1000
            # check for three of a kind
            if self.values[0][0] == 3:
                # check for full house
                if len(self.values) > 1:
                    if self.values[1][0] == 2:
                        self.score = self.score ** 500
                else:
                    # three of a kind
                    self.score = self.score ** 100
            # check for pair
            if self.values[0][0] == 2:
                # check for two pair
                if len(self.values) > 1:
                    if self.values[1][0] == 2:
                        self.score = self.score ** 50
                else:
                    # one pair
                    self.score = self.score ** 10
            # print(self.score)


def main():
    with open(input, 'r') as f:
        hands_str = f.readlines()

    hands = []
    for hand_str in hands_str:
        hand = hand_str.strip()
        cards_str, bid = hand.split(' ')
        hand = Hand(bid, cards_str)
        hand.calculate_score()
        hands.append(hand)

    # # sort hands by score
    hands.sort(key=lambda x: x.score)
    # calculate sum
    sum = 0
    for i in range(0, len(hands)):
        sum += int(hands[i].bid) * (i + 1)
    print(sum)


if __name__ == '__main__':
    main()