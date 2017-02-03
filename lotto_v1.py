import random
import datetime
from time import gmtime, strftime

# TODO добавить ID для транзакции сквозное по всем записям
# TODO получаем баланс банка
# TODO списание средств с баланса банка в случае выигрыша

print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')
print('$ ---           ------    ___________  ___________    ______  $')
print('$ | |          | ---- |   |___    ___| |___    ___|  | ____ | $')
print('$ | |          ||    ||       |  |         |  |      ||    || $')
print('$ | |          ||    ||       |  |         |  |      ||    || $')
print('$ | |          ||    ||       |  |         |  |      ||    || $')
print('$ | |          ||    ||       |  |         |  |      ||    || $')
print('$ | |------|   ||____||       |  |         |  |      ||____|| $')
print('$ |________|   |______|       |__|         |__|      |______| $')
print('$                                                             $')
print('$              BECOME A MILLIONAIR JUST IN MINUTE!            $')
print('$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $\n')

variants = []
steak = 0
bank = 0
tirage_res = []
matching = []
wallet = 0
coef=0
nums=[]
d=datetime.date.today()
transaction_id =1

#генератор ID для транзакции
def id_generator():
    global transaction_id
    transaction_id+=1
    return transaction_id

#пополняем кошелёк
def refill_wallet():
    global wallet
    print('This is ', wallet, ' in your wallet')
    refill = int(input("Input the money ammount you would like to play on: "))
    wallet+=refill
    return wallet

#пополняем баланс, делаем запись в файл о транзакции
def income(steak, bank):
    global wallet
    bank+=steak
    if wallet<steak:
        print("There is not enaught money in your wallet :(")
        decision = input("Press \"Y\" to refill wallet, or \"N\" to leave ")
        if decision == "Y" or decision == "y":
            refill_wallet()
        else:
            quit()
    else:
        wallet=wallet-steak
    return wallet

#выбираем шары для игры5
def chose_balls():
    print('Time to chose the balls!\nPlease, input balls number from 1 to 20')
    while len(variants)!=8:
        ball = int(input('Input number '))
        while ball > 20:
            ball=int(input('Input another number ')) 
        while ball in variants:
            ball=int(input('Input another number ')) 
        else:
            variants.append(ball)
    return print('This is the balls that you\'ve been chose!\n', variants[0], variants[1], variants[2], variants[3], variants[4], variants[5], variants[6], variants[7], sep=' | ')
            
#розыгрышь тиража            
def tirage():
    povtorka = []    
    while len(tirage_res)!=8:
        rnum = random.randint(1,20)
        while rnum in tirage_res:
            rnum = random.randint(1,20)
        else:
            tirage_res.append(rnum)
    return print('Here is current tirage results! \n', tirage_res[0], tirage_res[1], tirage_res[2], tirage_res[3], tirage_res[4], tirage_res[5], tirage_res[6], tirage_res[7],sep=' | ')

#сравниваем выбранные шары игрока с тиражем
def matching_balls(variants, tirage_res):
    for i in variants:
        if i in tirage_res:
            print ('Winning ball',i, sep=', ')
            matching.append(i)

#определяем коэфициент при выигрыше       
def win_coef(matching):
    global coef
    if len(matching)<3:
        return('\nYou lose, you will be more lucky next time!')
    if len(matching)==3:
        coef=3
        return coef
    if len(matching)==4:
        coef=6
        return coef
    if len(matching)==5:
        coef=18
        return coef
    if len(matching)==6:
        coef=60
        return coef
    if len(matching)==7:
        coef=100
        return coef
    if len(matching)==8:
        coef = 1000
        return coef

# TODO определяем сумму выигрыша    
def prize(coef, steak):
    prize=steak*coef
    return prize

# TODO получение баланса банка
#def get_bank_ballance():
    
# TODO списание средств с баланса банка в случае выигрыша
#def withdrew():
    

#очищаем данные прошедшей игры
def clear_last_data(coef, matching, variants):
    matching.clear()
    variants.clear()
    tirage_res.clear()
    coef=0

#принимаем решение можем ли играть дальше
def after_game(matching, t_prize):
    global wallet
    if len(matching)>2:
        print('Your prize is: $', t_prize)
        wallet+=t_prize
        print("You have increased your monney ammount up to: $", wallet)
    else:
        print('You lose, you will be more lucky next time!')
        print('Current wallet is ', wallet)
        if wallet>0:
            print("You still have $", wallet, " for the game. Next time you will win!")
        else:
            print("Your wallet is empty. Would you like to refill it?")
            decision = input("Press \"Y\" to refill wallet, or \"N\" to leave")
            if decision == "Y" or decision == "y":
                refill_wallet()
                print("There is $", wallet, "in your walet! Let\'s win a million dollars!")
            else:
                quit()
                
def store_to_file(variants, tirage_res, steak, d):
    file = open('transaction.txt', 'a+')
    file.write('transactionDate:')
    file.write(str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))+',')
    file.write('\n')
    file.write('transactionID:')
    file.write(str(transaction_id)+',')
    file.write('\n')
    file.write('transactionStake:')
    file.write(str(steak)+',')
    file.write('\n')
    file.write('userVariant:')
    file.write(str(variants)+',')
    file.write('\n')
    file.write('tirage:')
    file.write(str(tirage_res))
    file.write('\n\n')
    file.close()

#главная функция игры                
def main():
    refill_wallet()
    while wallet>0: 
        chose_balls()
        #global wallet
        global steak
        print('You have ', wallet, ' in your wallet')
        steak = int(input("Input your steak: $"))
        print('Your steak is ', steak)
        income(steak, bank)
        id_generator()
        print('id ', transaction_id)
        print("Your wallet ammount after steak: $", wallet)
        print('\n GOOD LUCK!\n')
        tirage()
        matching_balls(variants, tirage_res)
        win_coef(matching)
        prize(coef, steak)
        global t_prize
        t_prize=prize(coef, steak)
        store_to_file(variants, tirage_res, steak, d)
        after_game(matching, t_prize)
        clear_last_data(coef, matching, variants)
main()


