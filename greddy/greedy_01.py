def calculate_change(payment,cost):
    change = payment-cost
    coin_type=[50000,10000,5000,1000]
    money = 0
    for coin in coin_type:
        money = change // coin
        print(f"{change}원 잔돈으로 {coin}원{money}장 거슬러줌")
        change %= coin
        print(f"{change}원 잔돈 남았음")
        
    
    
calculate_change(100000,33000)