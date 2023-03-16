def currencycal(INR,curr):
    if curr=="Euro":
        print("Amount", INR*0.01417)
    elif curr=="British Pound":
        print("Amount", INR*0.0100)
    elif curr=="Australian Dollar":
        print("Amount", INR*0.02140)
    elif curr=="Canadian Dollar":
        print("Amount", INR*0.02027)
    else:
        print(-1)
currencycal(300,"Euro")
currencycal(300,"British Pound")
currencycal(300,"Australian Dollar")
currencycal(300,"Canadian Dollar")

