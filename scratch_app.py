import eventlet
eventlet.monkey_patch()

from hemlock import Branch, Page, Label, create_app, route
from hemlock_demographics import comprehensive_demographics

@route('/survey')
def start():
    return Branch(
        comprehensive_demographics(page=True),
        Page(
            Label('The end.'), 
            terminal=True
        )
    )

app = create_app()

if __name__ == '__main__':
    from hemlock.app import socketio
    socketio.run(app, debug=True)