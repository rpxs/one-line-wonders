print "\n".join(["\t".join(map(str,(lambda g,f,n: g(g,f,n))(lambda a,b,c:[1] if c==0 else b(a(a,b,c-1)),lambda a:[1]+[a[i-1]+a[i]for i in range(1,len(a))]+[1],n)))for n in range(int(__import__('sys').argv[1]))])
