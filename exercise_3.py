def calculate_years_months_days(_days): 
    years = _days // 365
    mounths = (_days % 365) // 30
    days = (_days % 365) % 30
    return years, mounths, days