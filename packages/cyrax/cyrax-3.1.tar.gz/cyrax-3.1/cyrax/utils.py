import os
import os.path as op
import posixpath
from itertools import takewhile


try:
    import itertools.izip as zip
except ImportError:
    pass

    
try:
    from urlparse import urlparse, urlunparse
except ImportError:
    from urllib.parse import urlparse, urlunparse


def makedirs(path):
    try:
        os.makedirs(path)
    except OSError:
        pass


def safe_url_join(base, path):
    """
    >>> safe_url_join('blog/x', 'foo/bar')
    'blog/x/foo/bar'
    >>> safe_url_join('/blog/x/', 'foo/bar')
    '/blog/x/foo/bar'
    >>> safe_url_join('http://blog/x', 'foo/bar')
    'http://blog/x/foo/bar'
    """
    scheme, netloc, basepath, params, query, fragment = urlparse(base)
    newpath = posixpath.join(basepath, path)
    parts = (scheme, netloc, newpath, params, query, fragment)
    return urlunparse(parts)


def base_path(url):
    """
    >>> base_path('http://google.com')
    '/'
    >>> base_path('http://piranha.org.ua/blog')
    '/blog'
    """
    basepath = urlparse(url)[2]
    return basepath or '/'


def url2path(url):
    return op.sep.join(url.split('/'))


def path2url(path):
    return '/'.join(path.split(op.sep))


def removecommon(p1, p2):
    common = takewhile(lambda x: x[0] == x[1], zip(p1, p2))
    l = len(list(common))
    return p1[l:], p2[l:]


def relpath(cur, dest):
    p1, p2 = removecommon(cur.split(op.sep), dest.split(op.sep))
    # empty element because of / in the end of name
    if p1 and p1[-1] == '':
        p1 = p1[:-1]
    p = ['../'] * len(p1) + p2
    if not p:
        return ''
    return op.join(*p)
