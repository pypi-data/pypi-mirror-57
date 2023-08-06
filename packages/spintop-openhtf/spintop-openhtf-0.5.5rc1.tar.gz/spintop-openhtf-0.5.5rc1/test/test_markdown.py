from spintop_openhtf.util.markdown import markdown, replace_image_urls, image_url

def test_simple_image_url():
    my_string = "foo=%s, bar=x" % image_url('bar')
    expected = 'foo=bar, bar=x'
    assert replace_image_urls(my_string) == expected
    assert my_string != expected
    
def test_multi_image_url():
    my_string = "foo=%s, bar=%s" % (image_url('bar'), image_url('foo'))
    expected = 'foo=bar, bar=foo'
    assert replace_image_urls(my_string) == expected
    assert my_string != expected
    
    