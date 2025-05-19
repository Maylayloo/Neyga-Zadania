def process_order(user, order):
    # validate user
    if not user["active"]:
        raise ValueError("User not active")

    # calculate price
    price = sum(order["items"])
    if price > 100:
        price *= 0.9
    return price
