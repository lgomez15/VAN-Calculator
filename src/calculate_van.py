def calculate_van(initial_investment,cash_flows, discount_rate):
    van = -initial_investment
    for i in range(len(cash_flows)):
        van += cash_flows[i] / (1 + discount_rate) ** (i+1)
    return van