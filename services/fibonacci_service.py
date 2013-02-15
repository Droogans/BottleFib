"""
Licence (MIT)
-------------

    Copyright (c) 2013, Andrew Yurisich.

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

__author__  = "Andrew Yurisich"
__version__ = "0.1.dev"
__license__ = "MIT"

import bottle

from lib import fibonacci

from xml.dom.minidom import getDOMImplementation

@bottle.route('/fib')
@bottle.route('/fib/')
def redirect_to_fib_series():
    bottle.redirect('/fib/1')

@bottle.route('/fib/<limit>')
def fibonacci_document(limit):
    """xml document of fibonacci series to `limit`"""
    try:
        limit = int(limit)
    except ValueError:
        limit = -1

    impl = getDOMImplementation()

    if limit < 0:
        error_xml  = impl.createDocument(None, "error", None)
        error_elem = error_xml.documentElement

        message = error_xml.createElement("message")
        error_elem.appendChild(message)
        message_text = "Argument error: Fibonacci sequence limit must be > 1"
        error_message = error_xml.createTextNode(message_text)
        message.appendChild(error_message)
        return error_xml.toxml()
        
    series = fibonacci.series(limit)

    fib_xml  = impl.createDocument(None, "fibonacci", None)
    fib_elem = fib_xml.documentElement
    
    for ix, n in enumerate(series):
        value = fib_xml.createElement("value")
        value.setAttribute("index", str(ix))
        fib_elem.appendChild(value)
        fib_value = fib_xml.createTextNode(str(n))
        value.appendChild(fib_value)
    
    bottle.response.content_type = "application/xml"
    return fib_xml.toxml()

if __name__ == '__main__':
    bottle.run(debug=True)
