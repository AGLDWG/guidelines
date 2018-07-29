import requests
import rdflib

def definitional_required_1(uri)
    """Definitional resources: ***MUST*** be presented in the Resource Description Framework, RDF
    """
    # RDF/XML, Turtle, JSON-LD, N-triples, N-quads or TriG
    rdf_accept_header = {
        'Accept': 'application/rdf+xml;q=1, text/turtle;q=0.9, application/ld+json;q=0.8, application/n-triples;q=0.7, application/n-quads;q=0.6, application/trig'
    }
    r = requests.get(uri, headers=rdf_accept_header)
    if 'rdf+xml' in r.headers['Content-Type']
        or 'turtle' in r.headers['Content-Type']
        or 'ld+json' in r.headers['Content-Type']
        or 'n-triple' in r.headers['Content-Type']
        or 'n-quads' in r.headers['Content-Type']
        or 'trig' in r.headers['Content-Type']:
        return True
    else:
        return False

def definitional_optional_2()
    """Definitional resources: ***SHOULD*** be presented in Hypertext Mark-Up Language version 5, HTML5
    """
    '''
    https://pypi.org/project/html5lib/
    '''
    pass

def definitional_optional_3()
    """Definitional resources: ***MAY*** use either hash or slash URIs for subelements
    """

    pass

def dataset_required_1():
    """Datasets: ***MUST*** present a landing page for the dataset in RDF    
    """
    pass

if __name__ == '__main__':
    pass
