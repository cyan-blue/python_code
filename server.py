from cgi import parse_qs, escape
def hello_world(env, start_response):
    parameters = parse_qs(env.get('query_string', ''))
    if 'subject' in parameters:
        subject = escape(parameters['subject'[0]])
    else:
        subject = 'world'
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ['''Hello %(subject)s
    Hello %(subject)s!
            '''%{'subject': subject}]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    srv = make_server('localhost', 8080, hello_world)
    srv.serve_forever()
