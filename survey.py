from hemlock import Branch, Page, Label, route
from hemlock_demographics import demographics

@route('/survey')
def start():
    return Branch(
        demographics('age_bins', 'race', 'gender', require=True, page=True),
        Page(
            Label('<p>Hello World</p>'), 
            terminal=True
        )
    )