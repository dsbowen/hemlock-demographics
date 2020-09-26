# file:///C:/Users/DBSpe/Downloads/F00010738-WVS-7_Master_Questionnaire_2017-2020_English.pdf

from flask_login import current_user
from hemlock import Check, Debug as D, Embedded, Input, Submit as S, Validate as V

from datetime import datetime

def demographics(*items, require=False):
    items = [demographics_items[item]() for item in items]
    if require:
        for item in items:
            item.validate.append(V.require())
    return items

demographics_items = {}

def register(key=None):
    def inner(func):
        demographics_items[key or func.__name__] = func
        return func

    return inner

@register
def gender():
    def record_male(gender_q):
        current_user.embedded.append(
            Embedded('Male', int(gender_q.data=='Male'), data_rows=-1)
        )

    return Check(
        '<p>What is your gender?</p>',
        ['Male', 'Female', 'Other'],
        var='Gender', data_rows=-1, submit=S(record_male)
    )

@register
def dob():
    def date_format(dob_q):
        try:
            # try to convert to a datetime object
            datetime.strptime(dob_q.response, '%m/%d/%Y')
        except:
            # if this fails, the participant entered an invalid response
            return '<p>Format your date of birth as mm/dd/yyyy.</p>'

    def record_age(dob_q):
        # calculate age in years
        date_of_birth = datetime.strptime(dob_q.data, '%m/%d/%Y')
        age = (datetime.utcnow() - date_of_birth).days / 365.25
        # record age as embedded data
        current_user.embedded.append(Embedded('Age', age, data_rows=-1))

    return Input(
        '<p>Enter your date of birth.</p>',
        placeholder='mm/dd/yyyy',
        var='DoB', data_rows=-1,
        validate=V(date_format),
        submit=S(record_age),
        debug=[D.send_keys(), D.send_keys('10/26/1992', p_exec=.8)]
    )

