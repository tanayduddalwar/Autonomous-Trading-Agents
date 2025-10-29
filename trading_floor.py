import os
import asyncio
from typing import List
from dotenv import load_dotenv
from tracers import LogTracer
from agents import add_trace_processor
from market import is_market_open
from traders import Trader

load_dotenv(override=True)

# Scheduler settings
RUN_EVERY_N_MINUTES = int(os.getenv("RUN_EVERY_N_MINUTES", "60"))
RUN_EVEN_WHEN_MARKET_IS_CLOSED = (
    os.getenv("RUN_EVEN_WHEN_MARKET_IS_CLOSED", "false").strip().lower() == "true"
)

# Trader info
names = ["Warren", "George", "Ray", "Cathie"]
lastnames = ["Patience", "Bold", "Systematic", "Crypto"]

# Force all traders to use Gemini models only
model_names = ["gemini-2.5-flash"] * len(names)
short_model_names = ["Gemini 2.5 Flash"] * len(names)


def create_traders() -> List[Trader]:
    """
    Create Trader instances with Gemini-only models.
    """
    traders = []
    for name, lastname, model_name in zip(names, lastnames, model_names):
        traders.append(Trader(name=name, lastname=lastname, model_name=model_name))
    return traders


async def run_every_n_minutes():
    """
    Run all traders repeatedly at intervals defined by RUN_EVERY_N_MINUTES.
    """
    add_trace_processor(LogTracer())
    traders = create_traders()

    while True:
        if RUN_EVEN_WHEN_MARKET_IS_CLOSED or is_market_open():
            print("Running traders...")
            await asyncio.gather(*[trader.run() for trader in traders])
        else:
            print("Market is closed, skipping run.")

        await asyncio.sleep(RUN_EVERY_N_MINUTES * 60)


if __name__ == "__main__":
    print(f"Starting scheduler to run every {RUN_EVERY_N_MINUTES} minutes")
    asyncio.run(run_every_n_minutes())
