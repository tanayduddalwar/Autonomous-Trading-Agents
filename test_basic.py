from accounts import Account
from market import get_share_price

# Test market data
print("Testing market data:")
try:
    price = get_share_price("AAPL")
    print(f"AAPL: ${price}")
except Exception as e:
    print(f"Market data error: {e}")

# Test trading
print("\nTesting Warren's account:")
try:
    warren = Account.get("warren")
    print(f"Balance: ${warren.balance}")
    result = warren.buy_shares("AAPL", 5, "Manual test")
    print("✅ Trade successful!")
except Exception as e:
    print(f"❌ Trade failed: {e}")

try:
    ray = Account.get("ray")
    print(f"Balance: ${ray.balance}")
    result = ray.buy_shares("AAPL", 5, "Manual test")
    print("✅ Trade successful!")
except Exception as e:
    print(f"❌ Trade failed: {e}")    