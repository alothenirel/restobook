# -*- coding: utf-8 -*-
import datetime

db.define_table(
    'restaurant',
    Field('name', 'string'),
    Field('address', 'string'),
    Field('zip', 'string'),
    Field('city', 'string'),
    Field('capacity', 'integer'),
)

db.define_table(
    'restaurant_availability',
    Field('restaurant',
          db.restaurant,
          requires=IS_IN_DB(db, 'restaurant.id', '%(name)s')),
    Field('week_day', 'integer'),
    Field('start_time', 'time'),
    Field('end_time', 'time')
)

db.define_table(
    'reservation',
    Field('restaurant',
          db.restaurant,
          requires=IS_IN_DB(db, 'restaurant.id', '%(name)s')),
    Field('planned_date', 'datetime',
         requires=IS_DATETIME_IN_RANGE(minimum=datetime.datetime.now())),
    Field('name', 'string',
          requires=IS_NOT_EMPTY()),
    Field('contact', 'string',
         requires=IS_NOT_EMPTY()),
    Field('quantity', 'integer'),
)
