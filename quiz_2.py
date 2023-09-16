exchange_rates={'달러':1320,'엔':920,'위안':182}
money=[13,200,13]
total_money=(exchange_rates['달러']*money[0]+exchange_rates['엔']*money[1]+exchange_rates['위안']*money[2])
print('철수가 가지고 있는 돈의 원화 가치는 '+ str(total_money) +'원 입니다.')
