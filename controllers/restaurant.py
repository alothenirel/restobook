# -*- coding: utf-8 -*-

def reservation():
    """
    Make an dict based planning for specified restaurant
    args :
    0 = restaurant id
    """
    restaurant = db(
        db.restaurant.id == request.args(0)
    ).select().first()
    if not (restaurant \
            and auth.has_permission('read',
                                    'reservation',
                                    restaurant.id)):
        redirect(URL('visitor','index'))

    reservations = db(
        db.reservation.restaurant == restaurant
    ).select(
        orderby=db.reservation.planned_date
    )
    return dict(restaurant=restaurant,
                 reservations=reservations)
