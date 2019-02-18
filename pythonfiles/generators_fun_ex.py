#simple generator function

def gen_ints(m):
    for i in range(m):
        yield i
gen=gen_ints(4)
print gen
print gen.next()
print gen.next()
print gen.next()
print gen.next()

print __name__

#if __name__=="__main__":