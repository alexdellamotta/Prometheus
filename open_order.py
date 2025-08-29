import MetaTrader5 as mt5


def open_order(symbol, lot, stop_loss, order_type) -> None:
    price = mt5.symbol_info_tick(symbol).ask


    if order_type == "buy":
        type = mt5.ORDER_TYPE_BUY

    # Fix the catch-all
    else:
        type = mt5.ORDER_TYPE_SELL

    order_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": type,
    "price": price,
    "sl": stop_loss,
    "comment": "python script open",
    "type_time": mt5.ORDER_TIME_GTC,
    }

    result = mt5.order_send(order_request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"order send failed, retcode={result.retcode}\n {result}")
    else:
        result_dict = result._asdict()
        for key, field in result_dict.items():
            if key == "request":
                traderequest_dict = field._asdict()
                for trade_req_key, tradereq_field in traderequest_dict.items():
                    print(f"traderequest: {trade_req_key}={tradereq_field}")
            else:
                print(f"{key}={field}")
