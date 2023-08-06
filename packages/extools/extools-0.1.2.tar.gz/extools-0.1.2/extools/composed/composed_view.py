"""
The ComposedExView is an abstract class that automates the
generation of composed ExViews from the special COMPOSE
class constant.
"""
from extools.exview import ExView

class ComposedExView():

    # The COMPOSE map has the following entry structure:
    # ("rotoid", "name", ("composed view name", "composed view name"...),
    COMPOSE = []

    def __init__(self, id=-1):
        try:
            for vd in COMPOSE:
                setattr(self, vs[1], ExView(vs[0], index))

            for vd in COMPOSE:
                v = getattr(self, vd[1])
                v.compose(getattr(self, c) for c in vd[2])

        except ExViewError as err:
            # Failed to compose views
            raise
