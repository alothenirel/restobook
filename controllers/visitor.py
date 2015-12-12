# -*- coding: utf-8 -*-

def index():
    """
    entry point
    List all restaurant in DB
    """
    session.quantity = int(request.vars.get("quantity",
                                            session.quantity or 1))
    date = request.vars.get("date",None)
    if date :
        session.date = datetime.datetime.strptime(date,
                                                  "%Y-%m-%d %H:%M:%S")
    else :
        session.date = datetime.datetime.now()
    query = (db.restaurant.id > 0)
    query &= (db.restaurant.capacity >= session.quantity)
    query &= availibility_query(session.date)
    restaurants = [ r for r in db(query).select() if left_space(r.restaurant)]
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
    if session.quantity and not form.vars.quantity:
        form.vars.quantity = session.quantity
    if session.date and not form.vars.planned_date:
        form.vars.planned_date = session.date

    if not left_space(restaurant):
        session.flash = 'Le restaurant est complet'
        redirect(URL('visitor','index'))

    if form.process().accepted:
        session.flash = 'Réservation éfféctuée'
        redirect(URL('visitor','index'))
    elif form.errors:
        response.flash = 'form has errors'
    return dict(restaurant=restaurant,
                form=form)
