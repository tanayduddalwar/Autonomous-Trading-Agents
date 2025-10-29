# 🤖 AI Trading Simulation System

An autonomous multi-agent trading simulation where AI traders with distinct personalities and strategies compete in a simulated stock market. Each trader uses Large Language Models (LLMs) to analyze market data, research opportunities, and execute trades based on their unique investment philosophy.

![Trading Dashboard](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.12-blue)


## 📋 Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Trader Personalities](#trader-personalities)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How It Works](#how-it-works)
- [API Keys & Environment Variables](#api-keys--environment-variables)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project simulates a trading floor where four AI-powered traders autonomously make investment decisions. Each trader has:
- **Unique personality** inspired by legendary investors (Warren Buffett, George Soros, Ray Dalio, Cathie Wood)
- **Distinct investment strategy** (value investing, macro trading, diversification, innovation focus)
- **Autonomous decision-making** using LLM-based agents
- **Real market data** integration via Polygon.io API
- **Live monitoring dashboard** built with Gradio

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    TRADING FLOOR (Scheduler)                 │
│  - Runs every N minutes                                      │
│  - Coordinates all traders                                   │
└────────────────────────┬─────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│   TRADER 1   │  │   TRADER 2   │  │   TRADER 3   │  ...
│   (Warren)   │  │   (George)   │  │    (Ray)     │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                  │
       └─────────────────┼──────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   AI AGENT CORE      │
              │  - LLM (Nemotron)    │
              │  - Researcher Tool   │
              │  - MCP Servers       │
              └──────────┬───────────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
  ┌──────────┐   ┌──────────────┐  ┌────────────┐
  │ Market   │   │  Account     │  │ Knowledge  │
  │ Data     │   │  Operations  │  │ Graph      │
  │ (MCP)    │   │  (MCP)       │  │ (LibSQL)   │
  └──────────┘   └──────┬───────┘  └────────────┘
                        │
                        ▼
              ┌──────────────────────┐
              │   DATABASE           │
              │  - Account State     │
              │  - Transactions      │
              │  - Portfolio History │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   GRADIO UI          │
              │  - Portfolio Charts  │
              │  - Live Monitoring   │
              │  - Transaction Logs  │
              └──────────────────────┘
```

## ✨ Features

### Core Capabilities
- **Autonomous Trading**: AI agents make independent buy/sell decisions
- **Multi-Strategy Simulation**: Four distinct trading philosophies compete simultaneously
- **Real-time Market Data**: Integration with Polygon.io for live/delayed stock prices
- **Persistent Memory**: Knowledge graph stores learned information across sessions
- **Live Dashboard**: Real-time portfolio visualization with Gradio
- **Transaction Logging**: Complete audit trail of all trading decisions
- **Risk Management**: Enforces balance checks, position limits, and trading rules

### Technical Features
- **MCP (Model Context Protocol)**: Modular tool architecture for extensibility
- **Async/Await**: Efficient concurrent execution of multiple traders
- **OpenAI-Compatible API**: Works with NVIDIA NIM, Gemini, or other providers
- **Configurable Scheduler**: Adjustable trading frequency (minutes to days)
- **Market Hours Aware**: Optional trading only during market hours

## 👥 Trader Personalities

### 🏦 Warren ("Patience")
**Strategy**: Value Investing
- Focuses on undervalued companies with strong fundamentals
- Long-term holding period
- Emphasizes cash flow, management quality, and competitive advantages
- Inspired by Warren Buffett

### 🎯 George ("Bold")
**Strategy**: Macro Trading
- Seeks large-scale market mispricings
- Contrarian approach based on macroeconomic analysis
- Bold, concentrated positions
- Inspired by George Soros

### 📊 Ray ("Systematic")
**Strategy**: Risk Parity & Diversification
- Systematic, principles-based approach
- Diversified across asset classes and sectors
- Adjusts based on macroeconomic indicators
- Inspired by Ray Dalio

### 🚀 Cathie ("Crypto")
**Strategy**: Disruptive Innovation
- Focuses on crypto ETFs and blockchain technology
- High-risk, high-reward positioning
- Active portfolio management
- Inspired by Cathie Wood

## 🚀 Installation

### Prerequisites
- Python 3.12+
- UV (Python package manager) or pip
- API keys (see [Configuration](#configuration))

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-trading-simulation.git
cd ai-trading-simulation
```

2. **Install dependencies**
```bash
# Using UV (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

3. **Set up environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys
```

4. **Initialize trader accounts**
```bash
uv run reset_accounts.py
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following:

```env
# Required: AI Model API Key
NVIDIA_API_KEY=your_nvidia_api_key_here
# OR
GEMINI_API_KEY=your_gemini_api_key_here

# Market Data (Optional - defaults to mock data)
POLYGON_API_KEY=your_polygon_api_key_here
POLYGON_PLAN=free  # Options: free, paid, realtime

# Trading Schedule
RUN_EVERY_N_MINUTES=60  # Run every 60 minutes
RUN_EVEN_WHEN_MARKET_IS_CLOSED=false  # Set to true for 24/7 operation

# MCP Server Configuration (Optional)
BRAVE_API_KEY=your_brave_search_key  # For web research
```

### API Key Setup

#### NVIDIA NIM (Recommended)
1. Visit [build.nvidia.com](https://build.nvidia.com)
2. Sign up and generate an API key
3. Add to `.env`: `NVIDIA_API_KEY=your_key`

#### Google Gemini (Alternative)
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create an API key
3. Add to `.env`: `GEMINI_API_KEY=your_key`

#### Polygon.io (Market Data)
1. Visit [polygon.io](https://polygon.io)
2. Sign up for free tier (15 min delayed data)
3. Add to `.env`: `POLYGON_API_KEY=your_key`

## 📖 Usage

### Start the Trading Simulation

```bash
# Run the main trading floor
uv run trading_floor.py
```

The system will:
1. Initialize all 4 traders
2. Run trading cycles every N minutes
3. Log all activity to the database
4. Continue until stopped (Ctrl+C)

### Launch the Dashboard

In a separate terminal:

```bash
# Start the Gradio UI
uv run ui.py
```

Then open http://localhost:7860 in your browser.

### Manual Testing

```bash
# Check account status
uv run debug.py

# View detailed logs
uv run check_logs.py

# Test individual components
uv run test_basic.py
```

## 📁 Project Structure

```
ai-trading-simulation/
├── trading_floor.py       # Main scheduler and orchestrator
├── traders.py             # AI agent trader implementation
├── accounts.py            # Account management and trading operations
├── ui.py                  # Gradio dashboard for monitoring
├── templates.py           # AI prompt templates
├── reset_accounts.py      # Initialize trader strategies
├── market.py              # Market data integration
├── database.py            # Persistence layer
├── tracers.py            # Logging and tracing utilities
├── mcp_params.py         # MCP server configuration
├── accounts_client.py    # MCP client for account operations
├── requirements.txt      # Python dependencies
├── .env                  # Environment configuration (create from .env.example)
└── README.md             # This file
```

### Core Components

#### 1. `trading_floor.py` - Orchestrator/Scheduler
**Role:** The main entry point that coordinates everything

**Responsibilities:**
- Creates 4 trader instances (Warren, George, Ray, Cathie) with different personalities
- Runs on a configurable schedule (every N minutes via `RUN_EVERY_N_MINUTES`)
- Checks if market is open before running (optional)
- Executes all traders concurrently using `asyncio.gather()`
- Toggles traders between "trading" and "rebalancing" modes

**Key Code:**
```python
traders = create_traders()  # Creates 4 Trader instances
await asyncio.gather(*[trader.run() for trader in traders])  # Runs all traders
```

---

#### 2. `traders.py` - AI Agent Logic
**Role:** Defines the `Trader` class containing the AI agent brain

**Flow per trader:**
1. **Creates an AI agent** with:
   - A researcher tool (for market research via web search)
   - MCP servers (for accessing market data and account operations)
   - Instructions specific to that trader's personality
2. **Fetches account data** (current balance, holdings, transaction history)
3. **Fetches strategy** (the trader's investment philosophy)
4. **Sends prompt to AI agent** asking it to:
   - Make trades (buy/sell decisions), OR
   - Rebalance portfolio
5. **AI agent analyzes and decides** based on:
   - Market research (via researcher tool)
   - Current portfolio state
   - Assigned investment strategy
6. **Executes trades** via MCP server tools (which call `accounts.py` methods)

**Key Code:**
```python
# Creates message for AI agent
message = trade_message(name, strategy, account)  # or rebalance_message

# AI agent runs with max turns
await Runner.run(self.agent, message, max_turns=MAX_TURNS)
```

---

#### 3. `accounts.py` - Trading Operations & State Management
**Role:** Manages account state and executes all trading operations

**Responsibilities:**
1. **Stores account data** in database:
   - Cash balance
   - Stock holdings (symbol → quantity mapping)
   - Complete transaction history
   - Portfolio value time series
   
2. **Provides trading methods** that AI agents call:
   - `buy_shares(symbol, quantity, rationale)` - Purchase stocks
   - `sell_shares(symbol, quantity, rationale)` - Sell stocks
   - `calculate_portfolio_value()` - Compute total worth (cash + holdings)
   - `report()` - Return JSON summary of account state

3. **Enforces trading rules**:
   - Validates sufficient funds before buying
   - Validates share ownership before selling
   - Applies 0.2% spread on all trades
   - Prevents invalid transactions

4. **Logs all actions** to database for monitoring and audit trail

**Key Code:**
```python
def buy_shares(self, symbol, quantity, rationale):
    price = get_share_price(symbol)
    total_cost = price * quantity * (1 + SPREAD)
    if total_cost > self.balance:
        raise ValueError("Insufficient funds")
    self.balance -= total_cost
    self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
    self.transactions.append(transaction)
    self.save()
```

---

#### 4. `ui.py` - Visualization & Monitoring
**Role:** Gradio-based web dashboard for live monitoring

**Features:**
1. **Portfolio value charts** showing performance over time
2. **Current holdings table** with real-time positions
3. **Recent transactions log** with timestamps and rationale
4. **Profit/loss indicators** with color coding
5. **Auto-refresh** every 2 minutes for latest data

**Note:** The `Trader` class in `ui.py` is a data container for visualization, separate from the AI agent in `traders.py`.

---

#### Supporting Files

**`templates.py`** - AI prompt engineering
- Contains instruction templates for trader agents
- Defines trade and rebalance message formats
- Includes tool descriptions and examples

**`market.py`** - Market data integration
- Interfaces with Polygon.io API for stock prices
- Caches market data to reduce API calls
- Falls back to mock data if API unavailable

**`database.py`** - Persistence layer
- SQLite-based storage for accounts and logs
- Handles all read/write operations
- Ensures data consistency

**`tracers.py`** - Logging and observability
- Custom tracing processor for agent activities
- Logs all agent actions, function calls, and errors
- Provides debugging visibility

**`mcp_params.py`** - MCP server configuration
- Defines MCP server parameters for each trader
- Configures market data and account operation servers

**`accounts_client.py`** - MCP client
- Exposes account operations as MCP tools
- Bridges AI agents with account methods
- Handles resource reading for strategies

**`reset_accounts.py`** - Account initialization
- Resets all trader accounts to initial state
- Sets unique strategies for each trader
- Useful for starting fresh simulations

## 🔄 How It Works

### 1. Scheduler Loop (trading_floor.py)
```python
while True:
    if market_is_open() or run_always:
        # Run all traders concurrently
        await asyncio.gather(*[trader.run() for trader in traders])
    
    # Wait N minutes before next cycle
    await asyncio.sleep(RUN_EVERY_N_MINUTES * 60)
```

### 2. Trader Execution (traders.py)
For each trader:
1. **Fetch current state**: Account balance, holdings, strategy
2. **Create AI agent**: With researcher tool and MCP servers
3. **Send prompt**: "Based on your strategy, make trades..."
4. **Agent decides**: 
   - Calls Researcher tool for market analysis
   - Calls lookup_share_price to check prices
   - Calls buy_shares or sell_shares to execute
5. **Update state**: Save transactions to database

### 3. Account Operations (accounts.py)
```python
def buy_shares(symbol, quantity, rationale):
    price = get_share_price(symbol)
    cost = price * quantity * (1 + SPREAD)  # 0.2% spread
    
    if cost > balance:
        raise ValueError("Insufficient funds")
    
    balance -= cost
    holdings[symbol] += quantity
    transactions.append(Transaction(...))
    save()
```

### 4. Dashboard Updates (ui.py)
- Refreshes every 2 minutes
- Displays portfolio charts, holdings, transactions
- Shows profit/loss for each trader

## 🔑 API Keys & Environment Variables

| Variable | Required | Purpose | Where to Get |
|----------|----------|---------|--------------|
| `NVIDIA_API_KEY` | Yes* | LLM for AI agents | [build.nvidia.com](https://build.nvidia.com) |
| `GEMINI_API_KEY` | Yes* | Alternative LLM | [Google AI Studio](https://makersuite.google.com) |
| `POLYGON_API_KEY` | No | Real market data | [polygon.io](https://polygon.io) |
| `BRAVE_API_KEY` | No | Web search for research | [Brave Search API](https://brave.com/search/api/) |

*Either NVIDIA or GEMINI key is required

## 🐛 Troubleshooting

### Common Issues

**Problem**: "404 page not found" error
- **Solution**: Model not available. Check available models:
  ```bash
  curl https://integrate.api.nvidia.com/v1/models \
    -H "Authorization: Bearer $NVIDIA_API_KEY"
  ```

**Problem**: Traders not executing trades
- **Solution**: Check logs with `uv run check_logs.py`. Ensure prompts are explicit about requiring trades.

**Problem**: "Insufficient funds" errors
- **Solution**: Reset accounts: `uv run reset_accounts.py`

**Problem**: API rate limits
- **Solution**: Increase `RUN_EVERY_N_MINUTES` or upgrade API tier

### Debug Commands

```bash
# Check trader account status
uv run debug.py

# View last 50 log entries for each trader
uv run check_logs.py

# Test market data connection
python -c "from market import get_share_price; print(get_share_price('AAPL'))"

# Manually execute a test trade
python -c "from accounts import Account; Account.get('warren').buy_shares('AAPL', 1, 'test')"
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

**⚠️ Disclaimer**: This is a simulation for educational purposes only. Not financial advice. Do not use for real trading decisions.
