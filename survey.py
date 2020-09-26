from hemlock import Branch, Page, Label, route
from hemlock_demographics import demographics

@route('/survey')
def start():
    return Branch(
        Page(*demographics('gender', 'dob')),
        Page(
            Label('<p>Hello World</p>'), 
            terminal=True
        )
    )