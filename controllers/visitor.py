# -*- coding: utf-8 -*-

def index():
    """
    entry point
    List all restaurant in DB
    """
    restaurants = db(db.restaurant.id > 0).select()
    return dict(restaurants=restaurants)

def reserve():
    """
    expose an make a reservation in given restaurant
    args :
    0 = restaurant id
    """
    restaurant = db(db.restaurant.id == request.args(0)).select().first()
    if not restaurant :
        redirect(URL('visitor','index'))

    db.reservation.restaurant.writable = False
    db.reservation.restaurant.readable = False

    form = SQLFORM(db.reservation)
    form.vars.restaurant = restaurant.id
    if form.process().accepted:
        session.flash = 'Réservation éfféctuée'
        redirect(URL('visitor','index'))
    elif form.errors:
        response.flash = 'form has errors'
    return dict(restaurant=restaurant,
                form=form)
