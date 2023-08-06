import re
from markdown2 import markdown as orig_markdown

IMAGE_DELIMITERS = (r"{&this-is-image_url-wrapper{", r"}&}")
IMAGE_REGEX = None

def wrap_image_delimiters(string):
    if IMAGE_REGEX and re.match(IMAGE_REGEX, string):
        raise RuntimeError('Cannot wrap an image url inside another image url.')
    return IMAGE_DELIMITERS[0] + string + IMAGE_DELIMITERS[1]

IMAGE_REGEX = wrap_image_delimiters(r'([\s\S]*?)')

def markdown(*args, **kwargs):
    return orig_markdown(*args, **kwargs)

def image_url(filepath):
    return wrap_image_delimiters(filepath)

def replace_image_urls(string, url_transform=lambda url: url):
    return re.sub(IMAGE_REGEX, lambda pattern: url_transform(pattern.group(1)), string)
    
    