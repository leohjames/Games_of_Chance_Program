import random
import sys

money = 100000

def coin_flip (guess, bet):
    global money
    money_bet = 0
    money_bet = bet
    print('Coin Flip')
    act_guess = str.casefold(guess)
    x = act_guess.find('heads')
    y = act_guess.find('tails')
    if x == 0:
        guess = 'heads'
    if y == 0:
        guess = 'tails'
    if (x + y) == -2:
        print('Please give either "Heads" or "Tails" as a guess.')
        print('\n')
        sys.exit()
    if bet > money:
        print('You cannot bet more money than you have!')
        print('\n')
        sys.exit()
    if bet < 0:
        print('You cannot bet a negative amount of money!')
        print('\n')
        sys.exit()
    num = random.randint(0, 1)
    outcome = ""
    if num == 0:
        outcome = 'heads'
    else:
        outcome = 'tails'
    if outcome == str.casefold(guess):
        money = money + (money_bet * 2)
        print('Winner! Your winnings are now at $' + format(money, '.2f'))
        print('\n')
    else:
        money = (money - money_bet)
        print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
        print('\n')
    return money

def cho_han (guess, bet):
    global money
    money_bet = 0
    money_bet = bet
    print('Cho Han')
    act_guess = str.casefold(guess)
    x = act_guess.find('even')
    y = act_guess.find('odd')
    if (x + y) == -2:
        print('Please give either "Higher" or "Lower" as a guess.')
        print('\n')
        sys.exit()
    if x == 0:
        guess = 'even'
    if y == 0:
        guess = 'odd'
    if bet > money:
        print(' You cannot bet more money than you have!')
        print('\n')
        sys.exit()
    if bet < 0:
        print('You cannot bet a negative amount of money!')
        print('\n')
        sys.exit()
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num_combo = num1 + num2
    if num_combo % 2 == 0:
        num_outcome = 'even'
    elif num_combo % 2 == 1:
        num_outcome = 'odd'
    if num_outcome == str.casefold(guess):
        money = money + (money_bet * 2)
        print('Winner! Your winnings are now at $' + format(money, '.2f'))
        print('\n')
    else: 
        money = money - money_bet
        print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
        print('\n')
    return money

def draw_2_cards(guess, bet):
    global money
    money_bet = 0
    money_bet = bet
    print('Draw 2 Cards')
    act_guess = str.casefold(guess)
    x = act_guess.find('higher')
    y = act_guess.find('lower')
    if x == 0:
        guess = 'higher'
    if y == 0:
        guess = 'lower'
    if (x + y) == -2:
        print('Please give either "Heads" or "Tails" as a guess.')
        print('\n')
        sys.exit()
    if bet > money:
        print('You cannot bet more money than you have!')
        print('\n')
        sys.exit()
    if bet < 0:
        print('You cannot bet a negative amount of money!')
        print('\n')
        sys.exit()
    players = []
    total_cards = [[[1, 'Ace of Hearts'], [2, 'Hearts'], [3, 'Hearts'], [4, 'Hearts'], [5, 'Hearts'], [6, 'Hearts'], [7, 'Hearts'], [8, 'Hearts'], [9, 'Hearts'], [10, 'Hearts'], [11, 'Jack of Hearts'], [12, 'Queen of Hearts'], [13, 'King ofHearts']], [[1, 'Ace of Spades'], [2, 'Spades'], [3, 'Spades'], [4, 'SpadesS'], [5, 'SpadesS'], [6, 'Spades'], [7, 'Spades'], [8, 'Spades'], [9, 'Spades'], [10, 'Spades'], [11, 'Jack of Spades'], [12, 'Queen of Spades'], [13, 'King of Spades']], [[1, 'Ace of Diamonds'], [2, 'Diamonds'], [3, 'Diamonds'], [4, 'Diamonds'], [5, 'Diamonds'], [6, 'Diamonds'], [7, 'Diamonds'], [8, 'Diamonds'], [9, 'Diamonds'], [10, 'Diamonds'], [11, 'Jack of Diamonds'], [12, 'Queen of Diamonds'], [13, 'King of Diamonds']], [[1, 'Ace of Clubs'], [2, 'Clubs'], [3, 'Clubs'], [4, 'Clubs'], [5, 'Clubs'], [6, 'Clubs'], [7, 'Clubs'], [8, 'Clubs'], [9, 'Clubs'], [10, 'Clubs'], [11, 'Jack of Clubs'], [12, 'Queen of Clubs'], [13, 'King of Clubs']]]
    i = 0
    try:
        while i <= 1:
            card_suit = random.randint(0, 3)
            card_in_card_suit = random.randint(0, 12)
            card = total_cards[card_suit][card_in_card_suit]
            if i == 0:
                card1 = card
                players.append(('Player 1', card1))
            if i == 1:
                card2 = card
                players.append(('Player 2', card2))
            del total_cards[card_suit][card_in_card_suit]
            i += 1
    except ValueError:
        print('Cannot pick the same card, please run program again.')
        print('\n')
        sys.exit()
    except IndexError:
        print('Cannot pick the same card, please run program again.')
        print('\n')
        sys.exit()
    print(players)
    try:
        if card1[0] > card2[0]:
            outcome = 'higher'
        if card2[0] > card1[0]:
            outcome = 'lower'
        if card1[0] == card2[0]:
            outcome = 'Tie'
        if outcome == str.casefold(guess):
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 'Tie':
            print('The cards have the same value! No winner declared.')
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    except UnboundLocalError:
        print('Cannot pick the same card, please run program again.')
        print('\n')
        sys.exit()

def roulette_guesses():
    print('Your choices for bets are as follows: ')
    print('Row:')
    print('this is betting on both 0 and 00.')
    print()
    print('Top Line or Basket:')
    print('this is betting on 0, 00, 1, 2, 3.')
    print()
    print('Line _ and Line _:')
    print('this is betting on two consecutive rows, as in lines 3 and 4.')
    print()
    print('First, Middle, or Last Column:')
    print('this is betting on all the numbers in either the first, middle, or last columns.')
    print()
    print('Top, Middle, or Bottom Dozen:')
    print('this is betting on either the first 12, middle 12, or bottom 12 numbers.')
    print()
    print('Odd or Even:')
    print('this is betting on either all odd or even numbers.')
    print()
    print('Red or Black:')
    print('this is beting on either all red or black numbers.')
    print()
    print('1 to 18 or 19 to 36:')
    print('this is betting on either all the numbers from 1 to 18 or all the numbers from 19 to 36; the two halves of the board.')
    print()
    print('Corner:')
    print('this is betting on a group of 4 numbers that are all touching each other on the roulette board; ie. 4, 5, 7, 8.')
    print('For this bet, you must include your 4 chosen numbers in a list after your bet, formatted as ' + "('Corner', *bet amount*, [4, 5, 7, 8])")
    print()
    print('Street:')
    print('this is betting on 1 line of number; ie. 1, 2, 3.')
    print('For this bet, you must include your 3 chosen numbers in a list after your bet, formatted as ' + "('Street', *bet amount*, [1, 2, 3])")
    print()
    print('Split:')
    print('this is betting on 2 numbers that are touching either vertically or horizontally; ie 1, 2 or 4, 7.')
    print('For this bet, you must include your 2 chosen numbers in a list after your bet, formatted as ' + "('Split', *bet amount*, [4, 7])")
    print()
    print('Straight:')
    print('this is betting on a single number.')
    print('For this bet, you must include your chosen number after your bet, formatted as ' + "('Straight', *bet amount*, 7)")
    print()

def roulette(guess, bet, choice = 1):
    global money
    money_bet = 0
    money_bet = bet
    print('Roulette')
    act_guess = str.casefold(guess)
    a = act_guess.find('row')
    b = act_guess.find('top line or basket')
    c = act_guess.find('line 1 and line 2')
    d = act_guess.find('line 2 and line 3')
    e = act_guess.find('line 3 and line 4')
    f = act_guess.find('line 4 and line 5')
    g = act_guess.find('line 5 and line 6')
    h = act_guess.find('line 6 and line 7')
    i = act_guess.find('line 7 and line 8')
    j = act_guess.find('line 8 and line 9')
    k = act_guess.find('line 9 and line 10')
    l = act_guess.find('line 10 and line 11')
    m = act_guess.find('line 11 and line 12')
    n = act_guess.find('first column')
    o = act_guess.find('second column')
    p = act_guess.find('third column')
    q = act_guess.find('top dozen')
    r = act_guess.find('middle dozen')
    s = act_guess.find('bottom dozen')
    t = act_guess.find('odd')
    u = act_guess.find('even')
    v = act_guess.find('red')
    w = act_guess.find('black')
    x = act_guess.find('1 to 18')
    y = act_guess.find('19 to 36')
    z = act_guess.find('corner')
    aa = act_guess.find('street')
    ab = act_guess.find('split')
    ac = act_guess.find('straight')
    ad = act_guess.find('line1 and line2')
    ae = act_guess.find('line2 and line3')
    af = act_guess.find('line3 and line4')
    ag = act_guess.find('line4 and line5')
    ah = act_guess.find('line5 and line6')
    ai = act_guess.find('line6 and line7')
    aj = act_guess.find('line7 and line8')
    ak = act_guess.find('line8 and line9')
    al = act_guess.find('line9 and line10')
    am = act_guess.find('line10 and line11')
    an = act_guess.find('line11 and line12')
    if a == 0:
        guess = 'row'
    if b == 0:
        guess = 'top line or basket'
    if c == 0:
        guess = 'line 1 and line 2'
    if d == 0:
        guess = 'line 2 and line 3'
    if e == 0:
        guess = 'line 3 and line 4'
    if f == 0:
        guess = 'line 4 and line 5'
    if g == 0:
        guess = 'line 5 and line 6'
    if h == 0:
        guess = 'line 6 and line 7'
    if i == 0:
        guess = 'line 7 and line 8'
    if j == 0:
        guess = 'line 8 and line 9'
    if k == 0:
        guess = 'line 9 and line 10'
    if l == 0:
        guess = 'line 10 and line 11'
    if m == 0:
        guess = 'line 11 and line 12'
    if n == 0:
        guess = 'first column'
    if o == 0:
        guess = 'second column'
    if p == 0:
        guess = 'third column'
    if q == 0:
        guess = 'top dozen'
    if r == 0:
        guess = 'middle dozen'
    if s == 0:
        guess = 'bottom dozen'
    if t == 0:
        guess = 'odd'
    if u == 0:
        guess = 'even'
    if v == 0:
        guess = 'red'
    if w == 0:
        guess = 'black'
    if x == 0:
        guess = '1 to 18'
    if y == 0:
        guess = '19 to 36'
    if z == 0:
        guess = 'corner'
    if aa == 0:
        guess = 'street'
    if ab == 0:
        guess = 'split'
    if ac == 0:
        guess = 'straight'
    if ad == 0:
        guess = 'line 1 and line 2'
    if ae == 0:
        guess = 'line 2 and line 3'
    if af == 0:
        guess = 'line 3 and line 4'
    if ag == 0:
        guess = 'line 4 and line 5'
    if ah == 0:
        guess = 'line 5 and line 6'
    if ai == 0:
        guess = 'line 6 and line 7'
    if aj == 0:
        guess = 'line 7 and line 8'
    if ak == 0:
        guess = 'line 8 and line 9'
    if al == 0:
        guess = 'line 9 and line 10'
    if am == 0:
        guess = 'line 10 and line 11'
    if an == 0:
        guess = 'line 11 and line 12'
    if (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q+r+s+t+u+v+w+x+y+z+aa+ab+ac+ad+ae+af+ag+ah+ai+aj+ak+al+am+an) == -40:
        print('Please call "roulette_guesses" to see a list of possible quesses.')
        print('\n')
        sys.exit()
    if bet > money:
        print('You cannot bet more money than you have!')
        print('\n')
        sys.exit()
    if bet < 0:
        print('You cannot bet a negative amount of money!')
        print('\n')
        sys.exit()
    outcome = random.randint(1, 38)
    if outcome == 37:
        outcome = '0'
    if outcome == 38:
        outcome = '00'
    if guess == 'row':
        print('Row')
        print(outcome)
        if outcome == '0':
            money = money + (money_bet * 18)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == '00':
            money = money + (money_bet * 18)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'top line or basket':
        print('Top Line or Basket')
        print(outcome)    
        if outcome == '0':
            money = money + (money_bet * 7)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == '00':
            money = money + (money_bet * 7)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 1:
            money = money + (money_bet * 7)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 2:
            money = money + (money_bet * 7)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 3:
            money = money + (money_bet * 7)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 1 and line 2':
        print('Six Line (L1, L2)')
        print(outcome)
        if outcome == 1:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 2:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 3:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 4:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 5:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 6:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 2 and line 3':
        print('Six Line (L2, L3)')
        print(outcome)
        if outcome == 4:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 5:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 6:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 7:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 8:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 9:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 3 and line 4':
        print('Six Line (L3, L4)')
        print(outcome)
        if outcome == 7:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 8:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 9:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 10:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 11:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 12:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 4 and line 5':
        print('Six Line (L4, L5)')
        print(outcome)
        if outcome == 10:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 11:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 12:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 13:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 14:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 15:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 5 and line 6':
        print('Six Line (L5, L6)')
        print(outcome)
        if outcome == 13:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 14:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 15:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 16:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 17:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 18:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 6 and line 7':
        print('Six Line (L6, L7)')
        print(outcome)
        if outcome == 16:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
        elif outcome == 17:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 18:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 19:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 20:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 21:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 7 and line 8':
        print('Six Line (L7, L8)')
        print(outcome)
        if outcome == 19:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 20:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 21:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 22:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 23:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 24:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 8 and line 9':
        print('Six Line (L8, L9)')
        print(outcome)
        if outcome == 22:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 23:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 24:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 25:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 26:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 27:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 9 and line 10':
        print('Six Line (L9, L10)')
        print(outcome)
        if outcome == 25:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 26:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 27:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 28:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 29:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 30:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 10 and line 11':
        print('Six Line (L10, L11)')
        print(outcome)
        if outcome == 28:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 29:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 30:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 31:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 32:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 33:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'line 11 and line 12':
        print('Six Line (L11, L12)')
        print(outcome)
        if outcome == 31:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 32:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 33:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 34:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 35:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 36:
            money = money + (money_bet * 6)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'first column':
        print('First Column')
        print(outcome)
        if outcome == 1:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 4:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 7:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 10:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 13:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 16:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 19:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 22:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 25:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 28:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 31:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 34:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'second column':
        print('Second Column')
        print(outcome)
        if outcome == 2:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 5:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 8:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 11:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 14:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 17:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 20:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 23:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 26:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 29:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 32:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 35:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'third column':
        print('Third Column')
        print(outcome)
        if outcome == 3:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 6:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 9:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 12:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 15:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 18:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 21:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 24:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 27:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 30:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 33:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 36:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'top dozen':
        print('Top Dozen')
        print(outcome)
        if outcome == 1:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 2:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 3:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 4:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 5:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 6:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 7:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 8:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 9:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 10:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 11:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 12:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'middle dozen':
        print('Middle Dozen')
        print(outcome)
        if outcome == 13:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 14:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 15:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 16:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 17:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 18:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 19:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 20:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 21:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 22:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 23:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 24:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'bottom dozen':
        print('Bottom Dozen')
        print(outcome)
        if outcome == 25:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 26:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 27:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 28:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 29:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 30:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 31:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 32:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 33:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 34:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 35:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 36:
            money = money + (money_bet * 3)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'odd':
        print('Odd')
        print(outcome)
        if outcome == '0':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        if outcome == '00':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        if outcome % 2 != 0:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'even':
        print('Even')
        print(outcome)
        if outcome == '0':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        if outcome == '00':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        if outcome % 2 == 0:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'red':
        print('Red')
        print(outcome)
        if outcome == 1:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 3:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 5:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 7:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 9:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 12:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 14:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 16:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 18:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 19:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 21:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 23:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 25:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 27:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 30:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 32:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 34:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 36:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'black':
        print('Black')
        print(outcome)
        if outcome == 2:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 4:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 6:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 8:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 10:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 11:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 13:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 15:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 17:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 20:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 22:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 24:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 26:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 28:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 29:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 31:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 33:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == 35:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == '1 to 18':
        print('1 to 18')
        print(outcome)
        if outcome == '0':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        elif outcome == '00':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        elif (outcome - 19) <= -1:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == '19 to 36':
        print('19 to 36')
        print(outcome)
        if outcome == '0':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        elif outcome == '00':
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        elif (outcome - 19) > -1:
            money = money + (money_bet * 2)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'corner':
        print('Corner')
        print(outcome)
        if outcome == choice[0]:
            money = money + (money_bet * 9)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == choice[1]:
            money = money + (money_bet * 9)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == choice[2]:
            money = money + (money_bet * 9)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))#
            print('\n')
        elif outcome == choice[3]:
            money = money + (money_bet * 9)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        if outcome != (choice[0] and choice[1] and choice[2] and choice[3]):
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'street':
        print('Street')
        print(outcome)
        if outcome == choice[0]:
            money = money + (money_bet * 12)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
            sys.exit()
        if outcome == choice[1]:
            money = money + (money_bet * 12)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        if outcome == choice[2]:
            money = money + (money_bet * 12)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        if outcome != (choice[0] and choice[1] and choice[2]):
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'split':
        print('Split')
        print(outcome)
        if outcome == choice[0]:
            money = money + (money_bet * 18)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        elif outcome == choice[1]:
            money = money + (money_bet * 18)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')
    if guess == 'straight':
        print('Straight')
        print(outcome)
        if outcome == choice:
            money = money + (money_bet * 36)
            print('Winner! Your winnings are now at $' + format(money, '.2f'))
            print('\n')
        else:
            money = money - money_bet
            print('Unfortunately, this has not been your game. Your money is now at $' + format(money, '.2f'))
            print('\n')

print('\n')

#if you're unsure what roulette bets you can place, delete the '#' infront of the below text!
#roulette_guesses()

#Enter desired game function below!
roulette('first column', 5000.65)

if money > 0 :
    #Enter desired game function below!
    coin_flip('Heads', 4000.00)

    if money > 0:
        #Enter desired game function below!
        cho_han('Even', 3010.99)

        if money > 0:
            #Enter desired game function below!
            draw_2_cards('Higher', 25200.15)
                #Repeat this set up for as many games as desired!
        else:
            print('Unfortunately you have run out of money!')
            print('\n')
    else:
        print('Unfortunately you have run out of money!')
        print('\n')
else:
    print('Unfortunately you have run out of money!')
    print('\n')
