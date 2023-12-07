ranking = '23456789TJQKA'
ranking2 = 'J23456789TQKA'

class Character:
    def __init__(self, a):
        self.chr = a

    def __lt__(self, other):
        return ranking.index(other.chr) < ranking.index(self.chr)

    def __str__(self):
        return str(self.chr)

    def __eq__(self, other):
        return self.chr == other.chr
    
    def __hash__(self):
        return hash(self.chr)
    

class Character2:
    def __init__(self, a):
        self.chr = a

    def __lt__(self, other):
        return ranking2.index(other.chr) < ranking2.index(self.chr)

    def __str__(self):
        return str(self.chr)

    def __eq__(self, other):
        return self.chr == other.chr
    
    def __hash__(self):
        return hash(self.chr)

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)

        self.value = -1
        s = set(cards)    
        if len(s) == 1:
            self.value = 6
        elif len(s) == 2:
            self.value = 4 # Full House

            for i in list(s):
                if cards.count(i) == 4:
                    self.value = 5 # 4 of a kind
                    break
            
        elif len(s) == 3:
            self.value = 2 # two pair

            for i in list(s):
                if cards.count(i) == 3:
                    self.value = 3 # three of a kind
                    break
            
        elif len(s) == 4:
            self.value = 1 # one pair
        else:
            self.value = 0

    def __str__(self):
        string = ''
        for i in self.cards:
            string += str(i)
        return string + ' ' + str(self.bid) + ' ' + str(self.value)

    def __lt__(self, other):
        if other.value > self.value:
            return False
        elif other.value < self.value:
            return True
        else:
            for i, character in enumerate(other.cards):
                if character < self.cards[i]:
                    return False
                elif character > self.cards[i]:
                    return True
                
        print("fuck")

class Hand2:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)

        wilds = cards.count(Character2('J'))
        self.value = -1
        
        s = set(cards)    
        if len(s) == 1:
            self.value = 6 #five of a kind
        elif len(s) == 2:
            if wilds:
                self.value = 6 # five of a kind
                return

            max_count = 0
            for i in list(s):
                max_count = max(max_count, cards.count(i))
            
            if max_count == 4:
                self.value = 5 # 4 of a kind
                return
            
            self.value = 4 # Full house
            
        elif len(s) == 3:
            max_count = 0
            for i in list(s):
                max_count = max(max_count, cards.count(i))
            
            if max_count == 3:
                if wilds == 3:
                    self.value = 5 # 4 of a kind
                elif wilds == 2:
                    self.value = 6 # 5 of a kind (probably not possible)
                elif wilds == 1:
                    self.value = 5 # 4 of a kind
                else:
                    self.value = 3 # 3 of a kind
            elif max_count == 2:
                if wilds == 2:
                    self.value = 5 # 4 of a kind
                elif wilds == 1:
                    self.value = 4 # full house
                else:
                    self.value = 2 # 2 pair
        
        elif len(s) == 4:
            # max count is 2
            if wilds:
                self.value = 3 # 3 of a kind
            else:
                self.value = 1 # a pair

        elif len(s) == 5:
            if wilds:
                self.value = 1 #a pair
            else:
                self.value = 0 #high card

    def __str__(self):
        string = ''
        for i in self.cards:
            string += str(i)
        return string + ' ' + str(self.bid) + ' ' + str(self.value)

    def __lt__(self, other):
        if other.value > self.value:
            return False
        elif other.value < self.value:
            return True
        else:
            for i, character in enumerate(other.cards):
                if character < self.cards[i]:
                    return False
                elif character > self.cards[i]:
                    return True
                
        print("fuck")

def get_input():
    inp = []
    with open("input.txt") as f:
        for i in f.readlines():
            inp.append(i.strip())
            
    return inp


def main():
# Solution goes here

    inp = get_input()

    hands = []
    for hand in inp:
        a = [Character(i) for i in hand.split()[0]]
        
        hands.append(Hand(a, hand.split()[1]))
    
    hands.sort(reverse=True)

    total = 0
    for idx, hand in enumerate(hands):
        total += (idx + 1) * hand.bid

    print("1:", total)
    
    hands = []
    for hand in inp:
        a = [Character2(i) for i in hand.split()[0]]

        hands.append(Hand2(a, hand.split()[1]))
    
    hands.sort(reverse=True)

    total = 0
    for idx, hand in enumerate(hands):
        total += (idx + 1) * hand.bid
        print(hand)
    print(total) # 250544761 too low

    return

if __name__ == "__main__":
    main()