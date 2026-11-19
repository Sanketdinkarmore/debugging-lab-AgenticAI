def calculate_total(items, discount_percent=0, tax_rate=0.08):
    subtotal = 0

    for item in items:
        subtotal += item["price"] * item["quantity"]

    discount = subtotal * (discount_percent / 100)
    discounted_subtotal = subtotal - discount

    tax = discounted_subtotal * tax_rate

    return round(discounted_subtotal + tax, 2)
