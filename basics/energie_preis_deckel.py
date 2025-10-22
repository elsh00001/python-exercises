def energie_preis_deckel(prev_year: int, this_year: int, price_per_kwh: float) -> float:
    # First 80% of previous year are capped at 0.4
    # any usage beyond these 80% needs to pay the full fill of price_per_kwh
    # If the cost for energy is below 0.4, pay the regular price
    capped_price_per_kwh = min(0.4, price_per_kwh)
    # if we have less than 80% of last year, simply return cheap
    if this_year < prev_year * 0.8:
        return round(this_year * capped_price_per_kwh, 2)
    # compute the
    cheap_amount = prev_year * 0.8
    extensive_amount = this_year - cheap_amount
    return round(extensive_amount * price_per_kwh + cheap_amount * capped_price_per_kwh, 2)
    pass


def main() -> None:
    # Note: This is only for student-side debugging
    assert energie_preis_deckel(10000, 8000, 0.3) == 2400.0
    assert energie_preis_deckel(10000, 8000, 0.4) == 3200.0
    assert energie_preis_deckel(10000, 8000, 0.5) == 3200.0
    assert energie_preis_deckel(8000, 10000, 0.5) == 4360.0


# this only ensures that main() is called when executing python file.py
if __name__ == '__main__':
    main()
