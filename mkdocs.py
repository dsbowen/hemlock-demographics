from docstr_md.python import PySoup, compile_md
from docstr_md.src_href import Github

src_href = Github('https://github.com/dsbowen/hemlock-demographics/blob/master')

path = 'hemlock_demographics/__init__.py'
soup = PySoup(path=path, parser='sklearn', src_href=src_href)
soup.keep_objects(
    'demographics',
    'comprehensive_demographics',
    'basic_demographics',
    'family_demographics',
    'country_demographics', 
    'status_demographics',
    'register'
)
compile_md(soup, compiler='sklearn', outfile='docs_md/api.md')