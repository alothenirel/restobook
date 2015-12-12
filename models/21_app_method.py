# -*- coding: utf-8 -*-

def get_occupation(restaurant_id,
                   date):
    query = db.reservation.restaurant == restaurant_id
    query &= db.reservation.planned_date >= date - datetime.timedelta(hours=1)
    query &= db.reservation.planned_date <= date + datetime.timedelta(hours=1)
    occupation = db.reservation.quantity.sum()
    return db(query).select(occupation).first()[occupation] or 0

def availibility_query(date):
    query = db.restaurant_availability.restaurant == db.restaurant.id
    query &= db.restaurant_availability.week_day == date.weekday()
    query &= db.restaurant_availability.start_time <= date.time()
    query &= db.restaurant_availability.end_time >= date.time()
    return query

left_space = lambda r: (
    get_occupation(r.id,session.date) + session.quantity \
    <= r.capacity
)
