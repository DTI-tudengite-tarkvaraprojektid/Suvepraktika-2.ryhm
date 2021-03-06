import prices
import powerUsage
import datetime

now = datetime.datetime.now()


def market_fee(start_hour, end_hour):
    time = end_hour - start_hour
    today_price = prices.get_today_price()
    price = 0
    for i in range(time):
        price += today_price[start_hour + i] * powerUsage.get_mwh()
    return price


def network_fee(day_fee, night_fee, start_hour, end_hour):
    # 8-12 / 12-8 winter 7-11 / 11-7

    fee = 0.0
    time = end_hour - start_hour

    for i in range(time):

        current_hour = start_hour + i
        # summertime
        if 4 <= now.month <= 9:

            if 8 <= current_hour <= 23:

                fee += day_fee

            else:
                fee += night_fee

        else:
            # wintertime
            if 7 <= current_hour <= 22:

                fee += day_fee

            else:
                fee += night_fee

    return fee


def const_fee(fee, start_hour, end_hour):
    time = end_hour - start_hour
    sum_m = fee * time

    return sum_m


def current_market():
    market = prices.get_today_price()
    return str(market[now.hour])
