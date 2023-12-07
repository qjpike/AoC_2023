ranking = '23456789TJQKA'
ranking2 = 'J23456789TQKA'

class Character:
    def __init__(self, a, part2 = False):
        self.chr = a
        if part2:
            self.ranking = ranking2
        else:
            self.ranking = ranking
    def __lt__(self, other):
        return other.ranking.index(other.chr) < self.ranking.index(self.chr)

    def __str__(self):
        return str(self.chr)

    def __eq__(self, other):
        return self.chr == other.chr
    
    def __hash__(self):
        return hash(self.chr)
    
class Hand:
    def __init__(self, cards, bid, part2=False):
        self.cards = cards
        self.bid = int(bid)

        self.value = -1
        
        if not part2:
            self.set_value_1()
        else:
            self.set_value_2()

    def set_value_1(self):
        s = set(self.cards)    
        if len(s) == 1:
            self.value = 6
        elif len(s) == 2:
            self.value = 4 # Full House

            for i in list(s):
                if self.cards.count(i) == 4:
                    self.value = 5 # 4 of a kind
                    break
            
        elif len(s) == 3:
            self.value = 2 # two pair

            for i in list(s):
                if self.cards.count(i) == 3:
                    self.value = 3 # three of a kind
                    break
            
        elif len(s) == 4:
            self.value = 1 # one pair
        else:
            self.value = 0
        
    def set_value_2(self):
        wilds = self.cards.count(Character('J'))
        s = set(self.cards)    
        if len(s) == 1:
            self.value = 6 #five of a kind
        elif len(s) == 2:
            if wilds:
                self.value = 6 # five of a kind
                return

            max_count = 0
            for i in list(s):
                max_count = max(max_count, self.cards.count(i))
            
            if max_count == 4:
                self.value = 5 # 4 of a kind
                return
            
            self.value = 4 # Full house
            
        elif len(s) == 3:
            max_count = 0
            for i in list(s):
                max_count = max(max_count, self.cards.count(i))
            
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
        a = [Character(i, True) for i in hand.split()[0]]

        hands.append(Hand(a, hand.split()[1], True))
    
    hands.sort(reverse=True)

    total = 0
    for idx, hand in enumerate(hands):
        total += (idx + 1) * hand.bid
        
    print("2:", total)

if __name__ == "__main__":
    main()