from random import randint
import subprocess
from time import sleep
import sys


############################
# MAIN
# Usage N = # of days in past you want to populate up to
# EX: populate.py 40 will populate last 40 days randomly with commits
############################

def main(argv):
    n = int(argv[0])
    while n > 0:
        num_commits = randint(0, 1)
        if num_commits != 0:
            subprocess.run(["touch", "realwork.txt"])
            with open("realwork.txt", "a") as f:
                f.write("new line\n")
            subprocess.run(["git", "add", "realwork.txt"])
            subprocess.call("git commit --date=\"{} day ago \" -m \"added realwork\"".format(str(n)))
#            subprocess.run(["git", "commit", "--date=\"%s".format(str(i)), "day", "ago\"", "-m" "\"added real work\""])
            subprocess.run(["git", "push"])
            sleep(.5)
        n -= randint(0,3)
        if (num_commits != 0):
            subprocess.run(["git", "rm", "realwork.txt"])
            subprocess.call("git commit --date=\"{} day ago \" -m \"deleted realwork\"".format(str(n)))
            #subprocess.run(["git", "commit", "--date=\"%s".format(str(i)), "day", "ago\"", "-m" "\"removed real work\""])
            subprocess.run(["git", "push"])


if __name__ == "__main__":
    main(sys.argv[1:])
