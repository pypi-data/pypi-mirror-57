from furl import furl
import unittest

def add_subdomain_to_url(url, *args):
    """
    add subdomains to url
    :param url:
    :param args: subdomains
    :return: url with subdomains
    """
    f = furl(url)
    subs = list(args)[::-1]
    for sub in subs:
        if f.host:
            f.host = sub + '.' + f.host
    return f.url

def add_path_to_url(url, *args):
    """
    add pathes to url
    :param url:
    :param args: path parts
    :return:
    """
    f = furl(url)
    for arg in args:
        f /= arg
    return f.url

def is_url_have_host(url):
    f = furl(url)
    if f.host:
        return True
    else:
        return False

def url_replace_path(url, path):
    f = furl(url)
    f.path = path

    return f.url



class TestUrlFuncs(unittest.TestCase):

    def test_is_url_have_host(self):
        self.assertTrue(is_url_have_host('https://google.com'))
        self.assertFalse(is_url_have_host('/erert/dfgdfg/dfg'))

    def test_url_replace_path(self):
        self.assertEqual(url_replace_path('https://google.com/123/321', '/111/222'), 'https://google.com/111/222')

if __name__ == '__main__':
    unittest.main()