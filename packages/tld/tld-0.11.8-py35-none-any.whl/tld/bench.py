
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from tld import get_tld
URLS_COUNT = 10000
URLS = [u'http://www.google.co.uk', u'http://www.v2.google.co.uk', u'http://www.google.co.uk:8001/lorem-ipsum/', u'http://www.me.cloudfront.net',
        u'http://www.v2.forum.tech.google.co.uk:8001/lorem-ipsum/', u'https://pantheon.io/', u'delusionalinsanity.com', u'www.baidu.com.cn', u'i.dont.exist', u'http://delusionalinsanity.com']
TIMES = 10000
for _ in range(TIMES):
    for url in URLS:
        tld = get_tld(url, fix_protocol=True, fail_silently=True)
