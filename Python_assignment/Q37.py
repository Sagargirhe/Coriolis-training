#Write a program that given a text file will create a new text file in which all the lines from the original file are numberedfrom 1 to n (where n is the number of lines in the file).

def new_file_with_line_no(fname):
    cnt = 1
    f = open(fname,'r')
    f1 = open('new_'+fname,'w')
    for line in f:
        f1.write(str(cnt)+' '+line)
        cnt+=1
    f1.close()
    f.close()

new_file_with_line_no('Q37.txt')


