import sys
for each in sys.path:
    print each

    print '\nAlways start by adding the "classes" folder to the python path:'
    if not ("C:\Users\Lifygen\projects\python" in sys.path):
        sys.path.append("C:\Users\Lifygen\projects\python")
    if not ("C:\Users\Lifygen\projects\python\classes" in sys.path):
        sys.path.append("C:\Users\Lifygen\projects\python\classes")
    if not ("C:\Users\Lifygen\projects\python\testclasses" in sys.path):
        sys.path.append("C:\Users\Lifygen\projects\python\testclasses")
    for each in sys.path:
        print each
print "hack1 installed!"