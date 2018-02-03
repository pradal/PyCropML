from path import Path
from urlparse import urlparse
from pycropml import pparse, render_python
from test1 import example, cwd, xmls


data = Path('data')
models = example()
m, = models
t1, t2 = m.tests

file_psets = {}
psets = m.parametersets
# Compute for each parameter set the set of parameters.
# A parameter set is a dict of parameter_name and values.
for name in psets:
    ps = psets[name]
    if not ps.params:
        # compute the params from the uri
        # define a function that may do the job
        uri = ps.uri
        parse_res = urlparse(uri)
        if parse_res.scheme == 'file':
            filename = parse_res.netloc
            _filename = data/filename
            if _filename.isfile():
                # read the file and fill the params
                if filename not in file_psets:
                    file_psets[filename] = pparse.pset_parser(_filename, m)
            else:
                assert 0, ('The file '+ filename+ ' do not exists')


# Compute the tests and make the relationships
for test in (t1, t2):
    print 'Test: ',test.name
    print test.paramsets
    param_values = {}

    uri = test.uri
    parse_res = urlparse(uri)
    if parse_res.scheme == 'file':
        filename = parse_res.netloc
        # parse tests

        # Build the content of the test with the run
        # Generate the Python code

