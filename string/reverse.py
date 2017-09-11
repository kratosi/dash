"""
Reverse works of a senetence separated by .

i.like.this.program.very.much
much.very.program.this.like.i

"""


def method2():
    str = ".i.like.this.program.very.much"
    newstr = ""
    l = len(str) - 1
    end = l
    deli = "."
    for i in range(l, -1, -1):
        if str[i] == "." :
            if i == 0:
                deli = ""
            newstr += str[i+1 : end+1] + deli
            end = i - 1

    print newstr
    

def reverse(str, l, h):
    while l < h:
        str[l], str[h] = str[h] , str[l]
        l += 1
        h -= 1


def method1():
    str = list("i like this program very much ")
    l = 0
    for i in range(len(str)):
        if str[i] == ' ' or i == len(str) -1:
            reverse(str, l, i -1)
            l = i+1

    print ''.join(str)
    reverse(str, 0, len(str)-1)
    print ''.join(str)

    
def main():
    method1()

main()
