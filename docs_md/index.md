# Hemlock demographics

Hemlock-demographics is a <a href="https://dsbowen.github.io/hemlock/" target="_blank">hemlock</a> extension for collecting demographic information.

## Installation

=== "Hemlock-CLI"
    ```
    $ hlk install hemlock-demographics
    ```

=== "pip"
    ```
    $ pip install hemlock-demographics
    ```

## Quickstart

=== "Using hemlock template"
    In `survey.py`:

    ```python
    from hemlock import Branch, Page, Label, route
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
    ```

=== "From scratch"
    Create a file `app.py`:

    ```python
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
    ```

## Running your app

=== "Hemlock-CLI"
    ```bash
    $ hlk serve
    ```

=== "python3"
    ```bash
    $ python3 app.py
    ```

Go to <http://localhost:5000/> in your browser.

## Citation

Hemlock-demographics is based largely on the demographics section of the [World Values Survey](http://www.worldvaluessurvey.org/).

```
@software{bowen2020hemlock-demographics,
  author = {Dillon Bowen},
  title = {Hemlock-Demographics},
  url = {https://dsbowen.github.io/hemlock-demographics/},
  date = {2020-10-05},
}

@dataset{inglehart2014wvs,
    author = {Inglehart, R., and C. Haerpfer, and A. Moreno, and C. Welzel, and K. Kizilova, and J. Diez-Medrano, and M. Lagos, and P. Norris, and E. Ponarin and B. Puranen and et al.},
    title={World Values Survey: Round Six},
    url = {http://www.worldvaluessurvey.org/},
    date = {2014.}
}
```

## License

Users must cite this package in any publications which use it.

It is licensed with the MIT [License](https://github.com/dsbowen/hemlock-demographics/blob/master/LICENSE).