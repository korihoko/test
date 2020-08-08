import pprint

theBoard = {}
theBoard = {'top-R': ' ', 'top-M': ' ','top-L': ' ',\
                'mid-R': ' ','mid-M': ' ','mid-L': ' ',\
                'bot-R': ' ','bot-M': ' ','bot-L': ' ',}

pprint.pprint(theBoard)


def tictactoe(posit):
        print(posit['top-L'] + '|' + posit['top-M'] + '|' + posit['top-R'])
        print('-----')
        print(posit['mid-L'] + '|' + posit['mid-M'] + '|' + posit['mid-R'])
        print('-----')
        print(posit['bot-L'] + '|' + posit['bot-M'] + '|' + posit['bot-R'])

print(tictactoe(theBoard))
