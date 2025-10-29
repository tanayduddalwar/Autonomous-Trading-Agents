from accounts import Account

for name in ["Warren", "George", "Ray", "Cathie"]:
    account = Account.get(name)
    print(f"\n{'='*50}")
    print(f"{name.upper()}")
    print(f"{'='*50}")
    print(f"Balance: ${account.balance:,.2f}")
    print(f"Strategy exists: {len(account.strategy) > 0}")
    print(f"Holdings: {account.holdings}")
    print(f"Total transactions: {len(account.transactions)}")
    if account.transactions:
        print(f"Last 3 transactions:")
        for tx in account.transactions[-3:]:
            print(f"  {tx.timestamp}: {tx.quantity:+d} {tx.symbol} @ ${tx.price:.2f}")