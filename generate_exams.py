import os
import random
import re
import shutil
import subprocess
import sys


def main(nv):

    random.seed(29)

    print()
    print("Creating ", nv, " randomized versions of the exam")
    print()

    # First we want to check if we would be deleting any files, and ask if we can overwrite
    if len(os.listdir("./Generated_tex")) != 0:
        contcheck = input("You already have some generated exams, ok to delete and start over? (y/n): ")
        print()
        if contcheck == "y":
            # deleting existing files within our output folders
            os.system('rm -rf ./Generated_tex/*')
            os.system('rm -rf ./Generated_pdf/*')
            os.system('mkdir ./Generated_pdf/Answer_Key')
        else:
            print("Ok, terminating program, nothing will be deleted/generated")
            print()
            exit
    

    # We want to load the master tex file into memory
    tf = open("./Master_Template/Master_Template.tex", 'r')
    tfcontent = tf.read()


    # Now split the content in the master tex file using our question break 'keys', which is %% ! Q
    tfcontent = tfcontent.split(r"%% ! Q")
    
    # we only randomize the questions, not the preamble (header) or ending (footer)
    tfheader = tfcontent[0]
    tffooter = tfcontent[-1]
    tfbody = tfcontent[1:-1]

    # manually add back in split characters b/c nothing else is working for me when I do split...
    for i, line in enumerate(tfbody):
        print(i)
        tfbody[i] = r"%% ! Q" + line
    tffooter = r"%% ! Q" + tffooter

    # Two versions of header, one with "answers" and one without
    if not "[answers]" in tfheader:
        tfheaderanswers = tfheader.replace(r"\documentclass[]{exam}", r"\documentclass[answers]{exam}")
    else:
        tfheaderanswers = tfheader 
        tfheader = tfheader.replace(r"\documentclass[answers]{exam}", r"\documentclass[]{exam}")
        


    # Each version needs to have its own random number, so we generate integers between 1 and 100, which will be written in each tex file version:
    L = range(1,101)
    texseeds = [random.choice(L) for _ in range(nv)]

    restr = r'setrandomizerseed\{(\d+)\}'

    # Loop across each version to generate:
    for i in range(1,nv+1):

        #    Set random seed for the latex header:
        newstr = r"setrandomizerseed{" + str(texseeds[1])+r'}'
        tfheader        = re.sub(restr, newstr, tfheader)
        tfheaderanswers = re.sub(restr, newstr, tfheaderanswers)

        #    Randomize order of questions (we don't care about remembering original order)
        random.shuffle(tfbody)

        #    Replace the version number in the first section !TBA!

        #    Create folder for version i
        os.system("mkdir ./Generated_tex/Version_"+str(i))
 
        #    Write the tex file 
        texout = tfheaderanswers + flatten(tfbody) + tffooter
        tfout = open("./Generated_tex/Version_"+str(i)+"/Version_"+str(i)+".tex", "w")
        tfout.write(texout)
        tfout.close()

        #    First, generate 'answer' key (tex compile)
        #needs multiple compilies to get references right:
        for j in range(3): 
            subprocess.call(["pdflatex",
                             "Version_"+str(i)+".tex"], #./Generated_tex/Version_"+str(i)+"/
                             shell = False,
                             cwd="./Generated_tex/Version_"+str(i)+"/")
        print(os.getcwd())
        print()
        # copy pdf to output folder (AK suffix)
        shutil.copy("./Generated_tex/Version_"+str(i)+"/Version_"+str(i)+".pdf", 
                    "./Generated_pdf/Answer_Key/Version_"+str(i)+"_AK.pdf")

        #    Second, generate the exam (tex compile).  Copy pdf to output folder
        texout = tfheader + flatten(tfbody) + tffooter
        tfout = open("./Generated_tex/Version_"+str(i)+"/Version_"+str(i)+".tex", "w")
        tfout.write(texout)
        tfout.close()
        #needs multiple compilies to get references right:
        for j in range(3): 
            subprocess.call(["pdflatex",
                             "Version_"+str(i)+".tex"], #./Generated_tex/Version_"+str(i)+"/
                             shell = False,
                             cwd="./Generated_tex/Version_"+str(i)+"/")
        # copy pdf to output folder
        shutil.copy("./Generated_tex/Version_"+str(i)+"/Version_"+str(i)+".pdf", 
                    "./Generated_pdf/Version_"+str(i)+".pdf")



def flatten(A):
    rt = ""
    for i in A:
       rt = rt + i
    return rt


if __name__ == "__main__":
    if sys.argv[1:]:
        main(int(sys.argv[1]))
    else:
        print()
        print("~~~~ Please specify number of versions when calling script ~~~~")
        print()
        print("Simply add a number, e.g., generate_exams 3 ")
        print()
        
    