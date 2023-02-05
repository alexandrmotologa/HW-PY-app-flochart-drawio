service_price        = 100
client_cash_amount   = int(input('enter cash amount: '))

if client_cash_amount >= service_price:
    print("CASH Payment success!!!")
else:
    print("CASH Payment FAILURE!!!")
    client_card_amount = int(input('enter card amount: '))

    if client_card_amount >= service_price:
        print("CARD Payment success!!!")
    else:
        print("CARD Payment FAILURE!!!")
        client_crypto_amount = int(input('enter crypto amount: '))

        if client_crypto_amount >= service_price:
            print("CRYPTO Payment success!!!")
        else:
            print("CRYPTO Payment FAILURE!!!")