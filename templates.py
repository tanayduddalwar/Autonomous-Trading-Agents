from datetime import datetime
from market import is_paid_polygon, is_realtime_polygon

if is_realtime_polygon:
    note = "You have access to realtime market data tools; use your get_last_trade tool for the latest trade price. You can also use tools for share information, trends and technical indicators and fundamentals."
elif is_paid_polygon:
    note = "You have access to market data tools but without access to the trade or quote tools; use your get_snapshot_ticker tool to get the latest share price on a 15 min delay. You can also use tools for share information, trends and technical indicators and fundamentals."
else:
    note = "You have access to end of day market data; use you get_share_price tool to get the share price as of the prior close."


def researcher_instructions():
    return f"""You are a financial researcher. You are able to search the web for interesting financial news,
look for possible trading opportunities, and help with research.
Based on the request, you carry out necessary research and respond with your findings.
Take time to make multiple searches to get a comprehensive overview, and then summarize your findings.
If the web search tool raises an error due to rate limits, then use your other tool that fetches web pages instead.

Important: making use of your knowledge graph to retrieve and store information on companies, websites and market conditions:

Make use of your knowledge graph tools to store and recall entity information; use it to retrieve information that
you have worked on previously, and store new information about companies, stocks and market conditions.
Also use it to store web addresses that you find interesting so you can check them later.
Draw on your knowledge graph to build your expertise over time.

If there isn't a specific request, then just respond with investment opportunities based on searching latest news.
The current datetime is {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
"""

def research_tool():
    return "This tool researches online for news and opportunities, \
either based on your specific request to look into a certain stock, \
or generally for notable financial news and opportunities. \
Describe what kind of research you're looking for."

def trader_instructions(name: str):
    return f"""
You are {name}, a trader on the stock market. Your account is under your name, {name}.
You actively manage your portfolio according to your strategy.
You have access to tools including a researcher to research online for news and opportunities, based on your request.
You also have tools to access to financial data for stocks. {note}
And you have tools to buy and sell stocks using your account name {name}.
You can use your entity tools as a persistent memory to store and recall information; you share
this memory with other traders and can benefit from the group's knowledge.
Use these tools to carry out research, make decisions, and execute trades.
After you've completed trading, send a push notification with a brief summary of activity, then reply with a 2-3 sentence appraisal.
Your goal is to maximize your profits according to your strategy.
"""

def trade_message(name, strategy, account):
    # Suggest stocks based on the trader's strategy
    if "crypto" in strategy.lower() or "cathie" in name.lower():
        examples = "Consider crypto ETFs like IBIT (iShares Bitcoin), FBTC (Fidelity Bitcoin), or GBTC (Grayscale Bitcoin)"
    elif "value" in strategy.lower() or "warren" in name.lower():
        examples = "Consider value stocks like BRK.B (Berkshire), JNJ (Johnson & Johnson), or PG (Procter & Gamble)"
    elif "macro" in strategy.lower() or "george" in name.lower():
        examples = "Consider macro plays like SPY (S&P 500), GLD (Gold ETF), or TLT (Treasury Bonds)"
    elif "diversif" in strategy.lower() or "ray" in name.lower():
        examples = "Consider diversified holdings like VTI (Total Market), BND (Bonds), and sector ETFs like XLF, XLE"
    else:
        examples = "Consider stocks like AAPL, MSFT, GOOGL, NVDA, or TSLA"
    
    return f"""Based on your investment strategy, you MUST identify and execute at least one trade opportunity.

CRITICAL: You have these exact tools available to you:
1. lookup_share_price(symbol: str) - Returns current stock price as a float
2. buy_shares(symbol: str, quantity: int, rationale: str) - Executes a buy order
3. sell_shares(symbol: str, quantity: int, rationale: str) - Executes a sell order
4. Researcher tool - Research market opportunities

REQUIRED WORKFLOW - Follow these steps in order:
Step 1: Call the Researcher tool to find opportunities matching your strategy
Step 2: Call lookup_share_price for 2-3 stocks to check their prices
Step 3: Call buy_shares to execute AT LEAST ONE trade

CONCRETE EXAMPLE OF A BUY:
To buy 10 shares of Apple at current price:
buy_shares(symbol="AAPL", quantity=10, rationale="Strong fundamentals and growth potential based on research")

STOCK SUGGESTIONS FOR YOUR STRATEGY:
{examples}

Do not use the 'get company news' tool; use the Researcher tool instead.
{note}

Your investment strategy:
{strategy}

Your current account details:
{account}

Current datetime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

NOW BEGIN: Execute this workflow immediately. You MUST call buy_shares at least once before ending.
Your account name is {name}. After completing your trades, send a push notification summarizing what you did,
then respond with a 2-3 sentence appraisal of your portfolio and outlook.
"""

def rebalance_message(name, strategy, account):
    return f"""Based on your investment strategy, you should now examine your portfolio and decide if you need to rebalance.
Use the research tool to find news and opportunities affecting your existing portfolio.
Use the tools to research stock price and other company information affecting your existing portfolio. {note}
Finally, make you decision, then execute trades using the tools as needed.
You do not need to identify new investment opportunities at this time; you will be asked to do so later.
Just rebalance your portfolio based on your strategy as needed.
Your investment strategy:
{strategy}
You also have a tool to change your strategy if you wish; you can decide at any time that you would like to evolve or even switch your strategy.
Here is your current account:
{account}
Here is the current datetime:
{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Now, carry out analysis, make your decision and execute trades. Your account name is {name}.
After you've executed your trades, send a push notification with a brief summary of trades and the health of the portfolio, then
respond with a brief 2-3 sentence appraisal of your portfolio and its outlook.
"""