import sys
import MetaTrader5 as mt5


PATH: str = r"/" # Specify Path
SERVER: str = "MetaQuotes-Demo" # Demo Account For Test
LOGIN: int = 0 # Enter Login Serial

def initialize(password, symbol) -> int:
    """ Initializes the terminal and fetches basic data. """
    if not mt5.initialize(path=PATH, login=LOGIN, server=SERVER, password=password):
        sys.exit(f"initialize() failed, error-code={mt5.last_error()}")

    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        sys.exit("Symbol not found, cannot call order_check()")

    return 0
