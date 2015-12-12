# -*- coding: utf-8 -*-

@auth.requires_membership('admin')
def restaurant():
    """
    expose an protected CRUD for Restaurant
    """
    grid = SQLFORM.grid(db.restaurant,
                       csv=False,)
    return dict(grid = grid)
