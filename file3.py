class vc:

    def m1(self):
        with open('file3.txt','r+') as f:
            countv=0
            countc=0
            #f.write("while working with exclusive or mode file must be exist other wise we get file exist error")
            v=list("aeiou")
            c=list("bcdfghjklmnpqrstvwxyz")
            for x in f.read():
                if x in v:
                    countv+=1
                elif x in c:
                    countc+=1
            print('no of vowels are:',countv)
            print('no of consonents are:',countc)
d=vc()
d.m1()