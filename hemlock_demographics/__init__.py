# file:///C:/Users/DBSpe/Downloads/F00010738-WVS-7_Master_Questionnaire_2017-2020_English.pdf

from .languages import languages

from country_list import countries_for_language
from flask_login import current_user
from hemlock import Binary, Check, Debug as D, Embedded, Input, Page, Range, Select, Submit as S, Validate as V
from hemlock.tools import show_on_event

from datetime import datetime, timedelta
from random import choice, randint

def demographics(
        *items, 
        page=False,
        require=False, 
        record_order=False, 
        record_index=False, 
        record_choice_index=False
    ):
    def add_question(item):
        q = demographics_items[item](require)
        (
            questions.extend(q) if isinstance(q, (tuple, list)) 
            else questions.append(q)
        )

    def set_question_attrs(question):
        question.data_rows = -1
        question.record_order = record_order
        question.record_index = record_index
        question.record_choice_index = record_choice_index

    questions = []
    [add_question(item) for item in items]
    [set_question_attrs(q) for q in questions]
    if page:
        return Page(
            *questions,
            name='Demographics',
            timer=dict(
                var='DemographicsTime',
                data_rows=-1,
                record_order=False,
                record_index=False
            ),
            debug=[D.debug_questions(), D.forward()]
        )
    return questions

def comprehensive_demographics(**kwargs):
    return demographics(
        'gender',
        'age',
        'race',
        'religion',
        'household_residents',
        'children',
        'live_with_parents',
        'marital_status',
        'education',
        'employment',
        'occupation',
        'sector',
        'primary_wage_earner',
        'save_money',
        'social_class',
        'income_group',
        **kwargs
    )

def basic_demographics(**kwargs):
    return demographics('gender', 'age', 'race', 'religion', **kwargs)

def family_demographics(**kwargs):
    return demographics(
        'household_residents', 
        'children', 
        'live_with_parents', 
        'marital_status', 
        **kwargs
    )

def country_demographics(**kwargs):
    return demographics('country', 'language', **kwargs)

def status_demographics(**kwargs):
    return demographics(
        'education', 
        'employment', 
        'occupation', 
        'sector', 
        'primary_wage_earner', 
        'save_money', 
        'social_class', 
        'income_group',
        **kwargs 
    )

demographics_items = {}

def register(key=None):
    def inner(func):
        demographics_items[key or func.__name__] = func
        return func

    return inner

def _debug_choices(question, require):
    values = [c.value for c in question.choices if c.value not in (None, '')]
    question.debug = D.click_choices(
        choice(values), p_exec=1 if require else .8
    )
    return question

@register()
def gender(require=False):
    gender = Check(
        '<p>What is your gender?</p>',
        ['Male', 'Female', 'Other'],
        var='Gender',
        validate=V.require() if require else None,
        submit=_record_male
    )
    _debug_choices(gender, require)
    specify = Input(
        '<p>If other, please specify.</p>',
        var='GenderSpecify', data_rows=-1
    )
    show_on_event(specify, gender, 'Other')
    return gender, specify

def _record_male(gender_q):
    current_user.embedded.append(
        Embedded(
            'Male', 
            int(gender_q.data=='Male'), 
            data_rows=-1,
            record_order=False,
            record_index=False
        )
    )

@register()
def age(require=False):
    start, end = datetime.strptime('1900-01', '%Y-%m'), datetime.utcnow()
    rand_date = start + timedelta(days=randint(0, (end-start).days))
    return Input(
        '<p>Enter your month and year of birth.</p>',
        var='BirthMonth',
        extra_attrs={
            'type': 'month', 
            'min': start.strftime('%Y-%m'), 
            'max': end.strftime('%Y-%m')
        },
        validate=V.require() if require else None,
        submit=_record_age,
        debug=[D.send_datetime(rand_date, p_exec=1 if require else .8)]
    )

def _record_age(age_q):
    # calculate age in years
    if age_q.data:
        age = (datetime.utcnow() - age_q.data).days / 365.25
    else:
        age = None
    # record age as embedded data
    current_user.embedded.append(
        Embedded(
            'Age', 
            age, 
            data_rows=-1,
            record_order=False,
            record_index=False
        )
    )

@register()
def race(require=False):
    race_q = Check(
        '''
        <p>Which race or ethnicity do you belong to?</p>
        <p>Check as many as apply.</p>
        ''',
        [
            'White',
            'Black',
            ('South Asian (Indian, Pakistani, etc.)', 'South Asian'),
            ('East Asian (Chinese, Japanese, etc.)', 'East Asian'),
            'Arabic or Central Asian',
            'Other'
        ],
        var='Race', multiple=True,
        validate=V.require() if require else None
    )
    _debug_choices(race_q, require)
    specify = Input(
        '<p>Please specify your race or ethnicity.</p>',
        var='RaceSpecify', data_rows=-1
    )
    show_on_event(specify, race_q, 'Other')
    return race_q, specify

@register()
def religion(require=False):
    religion_q = Select(
        '''
        <p>Which religion or religious denomination do you belong to, if any?
        </p>
        ''',
        [
            '',
            'None',
            'Roman Catholic',
            'Protestant',
            ('Orthodox (Russian, Greek, etc.)', 'Orthodox'),
            'Jewish',
            'Muslim',
            'Hindu',
            'Buddhist',
            'Other'
        ],
        var='Religion',
        validate=V.require() if require else None
    )
    _debug_choices(religion_q, require)
    specify = Input(
        '<p>Please specify your religion or religious denomination.</p>',
        var='RelgionSpecify',
    )
    show_on_event(specify, religion_q, 'Other')
    return religion_q, specify

# list of (English country name, ISO 3166-1 code) tuples
countries = countries_for_language('en')
countries = [(c[1], c[0]) for c in countries]

@register()
def country(require=False):
    residence = Select(
        '<p>What country are you currently living in?</p>',
        countries.copy() + [('Other', 'other')],
        default='US', var='CountryOfResidence'
    )
    birth = Select(
        '<p>What country were you born in?</p>',
        [('I live in the country I was born in', 'same')] + countries.copy(),
        default='same', var='CountryOfBirth',
        submit=S(_check_for_same_country, residence)
    )
    citizen = Select(
        '<p>What is your country of primary citizenship?</p>',
        (
            [('I live in my country of primary citizenship', 'same')] 
            + countries.copy()
        ),
        default='same', var='CountryOfCitizenship',
        submit=[
            S(_check_for_same_country, residence), 
            S(_immigration_status, residence)
        ]
    )
    return [_debug_choices(q, require) for q in (residence, birth, citizen)]

def _check_for_same_country(country_q, residence_q):
    if country_q.data == 'same':
        country_q.data = residence_q.data

def _immigration_status(citizen_q, residence_q):
    immigrant = int(citizen_q.data != residence_q.data)
    current_user.embedded.append(
        Embedded(
            'Immigrant', 
            immigrant, 
            data_rows=-1,
            record_order=False,
            record_index=False
        )
    )

languages = [(l[1], l[0]) for l in languages]

@register()
def language(require=False):
    language_q = Select(
        '<p>What language do you normally speak at home?</p>',
        languages.copy() + [('Other', 'other')],
        default='en', var='Language'
    )
    return _debug_choices(language_q, require)

@register()
def household_residents(require=False):
    return Input(
        '''
        <p>How many people regularly live in your household, including 
        yourself and children?</p>
        ''',
        var='NHouseholdResidents', extra_attrs={'type': 'number', 'min': 1},
        validate=V.require() if require else None,
        debug=D.send_keys(str(randint(1, 10)), p_exec=1 if require else .8)
    )

@register()
def children(require=False):
    return Input(
        '<p>How many children do you have?</p>',
        var='NChildren', extra_attrs={'type': 'number', 'min': 0},
        validate=V.require() if require else None,
        debug=D.send_keys(str(randint(1, 10)), p_exec=1 if require else .8)
    )

@register()
def live_with_parents(require=False):
    live_with_parents = Binary(
        '<p>Do you live with one or both of your parents?</p>',
        var='LiveWithParents', 
        validate=V.require() if require else None
    )
    live_with_inlaws = Binary(
        '<p>Do you live with one or both your parents in law?</p>',
        ['Yes', 'No (or, I do not have parents in law)'],
        var='LiveWithInlaws', 
        validate=V.require() if require else None
    )
    return [
        _debug_choices(q, require) 
        for q in (live_with_parents, live_with_inlaws)
    ]

@register()
def marital_status(require=False):
    status_q = Select(
        '<p>What is your marital status?</p>',
        [
            '',
            'Married',
            'Living together as married',
            'Divorced',
            'Separated',
            'Widowed',
            'Single'
        ],
        var='MaritalStatus',
        validate=V.require() if require else None
    )
    return _debug_choices(status_q, require)

@register()
def education(require=False):
    educ_q = Select(
        '''
        <p>What is the highest educational level you have completed? (Values in
        parentheses are for the U.S. school system.)</p>
        ''',
        [
            '',
            ('Early childhood education or no education', 0),
            ('Primary education (elementary school)', 1),
            ('Lower secondary education (middle school)', 2),
            ('Upper secondary education (high school/GED)', 3),
            ('Post-secondary non-tertiary education (vocational training)',4),
            ('Short-cycle tertiary education (2-year college)', 5),
            ('Bachelor or equivalent', 6),
            ('Master or equivalent', 7),
            ('Doctoral or equivalent', 8)
        ],
        var='Education',
        validate=V.require() if require else None
    )
    return _debug_choices(educ_q, require)

@register()
def employment(require=False):
    employment_q = Select(
        '''
        <p>What is your employment status?</p>
        <p>If you have multiple jobs, select the option for your main job.</p>
        ''',
        [
            '',
            ('Full time employment (30 or more hours/week)', 'full'),
            ('Part time employment (fewer than 30 hours/week)', 'part'),
            ('Self employed', 'self'),
            ('Retired/pensioned', 'retired'),
            ('Stay at home spouse not otherwise employed', 'home'),
            ('Student', 'student'),
            ('Unemployed', 'unemployed')
        ],
        var='Employment',
        validate=V.require() if require else None
    )
    return _debug_choices(employment_q, require)

@register()
def occupation(require=False):
    occupation_q = Select(
        '''
        <p>To which occupational group do you belong?</p>
        <p>If you have multiple jobs, select the option for your main job. If 
        you are not employed, select the option for your most recent job.</p>
        ''',
        [
            '',
            (
                '''
                Professional and technical (for example: doctor, teacher, 
                engineer, artist, accountant, nurse)
                ''', 
                'professional'
            ),
            (
                '''
                Higher administrative (for example: banker, executive in big 
                business, high government official, union official)
                ''', 
                'admin'
            ),
            (
                '''
                Clerical (for example: secretary, clerk, office manager, civil 
                servant, bookkeeper)
                ''', 
                'clerical'
            ),
            (
                '''
                Sales (for example: sales manager, shop owner, shop assistant, 
                insurance agent, buyer)
                ''', 
                'sales'
            ),
            (
                '''
                Service (for example: restaurant owner, police officer, 
                waitress, barber, caretaker)
                ''', 
                'service'
            ),
            (
                '''
                Skilled worker (for example: foreman, motor mechanic, printer,
                seamstress, tool and die maker, electrician)
                ''', 
                'skilled'
            ),
            (
                '''
                Semi-skilled worker (for example: bricklayer, bus driver, 
                cannery worker, carpenter, sheet metal worker, baker)
                ''', 
                'semi-skilled'
            ),
            (
                '''
                Unskilled worker (for example: laborer, porter, unskilled 
                factory worker, cleaner)
                ''', 
                'unskilled'
            ),
            ('Farm worker', 'farm worker'),
            ('Farm proprietor or manager', 'farm manager'),
            ('Never had a job', 'none')
        ],
        var='Occupation', 
        validate=V.require() if require else None
    )
    return _debug_choices(occupation_q, require)

@register()
def sector(require=False):
    sector_q = Select(
        '''
        <p> Are you working for the government or public institution, for 
        private business or industry, or for a private nonprofit organization? 
        </p>
        <p>If you are not employed, select the option for your most recent 
        job.</p>
        ''',
        [
            '',
            ('Government or public instution', 'public'),
            ('Private business or industry', 'private'),
            ('Private non-profit organization', 'non-profit'),
            ('Never had a job', 'none')
        ],
        var='Sector',
        validate=V.require() if require else None
    )
    return _debug_choices(sector_q, require)

@register()
def primary_wage_earner(require=False):
    wage_q = Binary(
        '<p>Are you the primary wage earner in your household?</p>',
        var='PrimaryWageEarner',
        validate=V.require() if require else None
    )
    return _debug_choices(wage_q, require)

@register()
def save_money(require=False):
    save_q = Select(
        '<p>In the last year, did your family:</p>',
        [
            '',
            ('Save money', 'save'),
            ('Just get by', 'get by'),
            ('Spent some savings', 'spent'),
            ('Spent savings and borrowed money', 'borrowed')
        ],
        var='Savings',
        valdate=V.require() if require else None
    )
    return _debug_choices(save_q, require)

@register()
def social_class(require=False):
    social_q = Select(
        '''
        <p>Which social class would you describe yourself as belonging to?</p>
        ''',
        [
            '',
            ('Upper class', 'upper'),
            ('Upper middle class', 'upper middle'),
            ('Lower middle class', 'lower middle'),
            ('Working class', 'working'),
            ('Lower class', 'lower')
        ],
        var='SocialClass',
        validate=V.require() if require else None
    )
    return _debug_choices(social_q, require)

@register()
def income_group(require=False):
    return Range(
        '''
        <p>On a scale from 0 (lowest) to 10 (highest), which income group does 
        your household belong to?</p>
        <p>Please consider all wages, salaries, pensions, investments, and 
        other income.</p>
        ''',
        min=0, max=10, var='IncomeGroup'
    )