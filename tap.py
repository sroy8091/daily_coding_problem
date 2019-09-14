def htmlize(tag):
    def inner_func(f):
        def wrap(*args):
            s = f(args)
            return "<"+tag+">"+s+"</"+tag+">"
        return wrap
    return inner_func



@htmlize('section')
@htmlize('blockquote')
def generate_lorem(n_sentences):
    return "Lorem ipsum is at it's best"

# print(generate_lorem(1))
