<script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML" type="text/javascript"></script>

<link rel="stylesheet" href="https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css" type="text/css" />

<style>
    a.src-href {
        float: right;
    }
    p.attr {
        margin-top: 0.5em;
        margin-left: 1em;
    }
    p.func-header {
        background-color: gainsboro;
        border-radius: 0.1em;
        padding: 0.5em;
        padding-left: 1em;
    }
    table.field-table {
        border-radius: 0.1em
    }
</style># Demographics

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        
    </tbody>
</table>



##hemlock_demographics.**demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>demographics</b>(<i>*items, page=False, require=False, record_index=False</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L18">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>*items : <i>str</i></b>
<p class="attr">
    Names of demographic items to return. <a href="items.md">See the full list of available items</a>.
</p>
<b>page : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that a page should be returned containing the demographics items. If <code>False</code>, a list of questions is returned.
</p>
<b>require : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that participants are required to respond to the items.
</p>
<b>record_index : <i>bool, default=False</i></b>
<p class="attr">
    Indicates that the dataframe should record the order in which the demographic items appear on the page.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>demographics : <i>hemlock.Page or list of hemlock.Question</i></b>
<p class="attr">
    A page containing the requested demographics items if <code>page</code>, otherwise a list of demographics questions.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
from hemlock import push_app_context
from hemlock_demographics import demographics

app = push_app_context()

demographics('age', 'gender', 'race', page=True).preview()
```

##hemlock_demographics.**comprehensive_demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>comprehensive_demographics</b>(<i>**kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L82">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>demographics</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>demographics : <i></i></b>
<p class="attr">
    A comprehensive demographics questionnaire including basic demographics, family demographics, country demographics, and SES demographics.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_demographics.**basic_demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>basic_demographics</b>(<i>**kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L118">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>demographics</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>basic demographics : <i></i></b>
<p class="attr">
    Gender, age, and race.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_demographics.**family_demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>family_demographics</b>(<i>**kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L132">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>demographics</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>family demographics : <i></i></b>
<p class="attr">
    Number of household residents, number of children, living with parents or in-laws, marital status.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_demographics.**country_demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>country_demographics</b>(<i>**kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L153">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>demographics</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>country demographics : <i></i></b>
<p class="attr">
    Country of residence, origin, citizenship, and household language.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_demographics.**status_demographics**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>status_demographics</b>(<i>**kwargs</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L167">[source]</a>
</p>



<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>**kwargs : <i></i></b>
<p class="attr">
    Keyword arguments are passed to <code>demographics</code>.
</p></td>
</tr>
<tr class="field">
    <th class="field-name"><b>Returns:</b></td>
    <td class="field-body" width="100%"><b>SES demographics : <i></i></b>
<p class="attr">
    Education, employment, occupation, work sector, savings, subjective social class and income group.
</p></td>
</tr>
    </tbody>
</table>



##hemlock_demographics.**register**

<p class="func-header">
    <i>def</i> hemlock_demographics.<b>register</b>(<i>key=None</i>) <a class="src-href" target="_blank" href="https://github.com/dsbowen/hemlock-demographics/blob/master/hemlock_demographics/__init__.py#L194">[source]</a>
</p>

Register a demographics item.

<table class="docutils field-list field-table" frame="void" rules="none">
    <col class="field-name" />
    <col class="field-body" />
    <tbody valign="top">
        <tr class="field">
    <th class="field-name"><b>Parameters:</b></td>
    <td class="field-body" width="100%"><b>key : <i>str or None, default=None</i></b>
<p class="attr">
    String key for the item. If <code>None</code>, the name of the function is used.
</p></td>
</tr>
    </tbody>
</table>

####Examples

```python
@register()
def gender(require=False):
    gender = Check(
        '<p>What is your gender?</p>',
        ['Male', 'Female', 'Other'],
        var='Gender'
    )
```