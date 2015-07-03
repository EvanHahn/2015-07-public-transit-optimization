def optimize_caltrain(days):
    if days == 0:
        return 0.0

    eight_rides = days / 4
    normal_days = days % 4

    eight_rides_price = eight_rides * 50.0
    normal_days_price = normal_days * 13.50
    non_monthly_price = eight_rides_price + normal_days_price

    if non_monthly_price < 179:
        if eight_rides != 0:
            print eight_rides, '8-ride tickets for', eight_rides_price
        if normal_days != 0:
            print normal_days, 'Caltrain days', normal_days_price
        return non_monthly_price
    else:
        print 'Caltrain monthly pass for', 179
        return 179.0


def optimize_muni(days):
    if days == 0:
        return 0.0

    individual_ticket_price = days * 4.50
    if individual_ticket_price < 70:
        print days, 'invidual tickets for', individual_ticket_price
        return individual_ticket_price
    else:
        print 'Muni month pass for', 70
        return 70.0


def optimize(days_in_palo_alto):
    days_in_sf = 20 - days_in_palo_alto

    print days_in_palo_alto, 'days of Caltrain,',
    print days_in_sf, 'days of Muni'

    caltrain_amount = optimize_caltrain(days_in_palo_alto)
    muni_amount = optimize_muni(days_in_sf)

    total = caltrain_amount + muni_amount

    print 'Total:', total
    return total


for days_in_palo_alto in xrange(21):
    optimize(days_in_palo_alto)
    print
