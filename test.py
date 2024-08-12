d = {"aziz" : 20, "ouss" : 19, "ahmed" : 17}

def test (dd = {}, **paras) : 
    print (dd)
    print (paras)
ch = ""
test ()
print (type(d.keys()))
print (d.values())
print (d.items())

for i in d.keys () : 
    print (i)
