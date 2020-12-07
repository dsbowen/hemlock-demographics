from hemlock import Branch, Page, Label, route
from hemlock_demographics import comprehensive_demographics

@route('/survey')
def start():
    return Branch(
        comprehensive_demographics(page=True),
        Page(
            Label('The End'), 
            terminal=True
        )
    )