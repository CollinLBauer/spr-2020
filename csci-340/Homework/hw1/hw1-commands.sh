#!bin/bash

# validate script is run properly
if [ $# -lt 1 ]; then
    echo "Must provide an output file as argument."
    exit
fi
if [ $1 == $0 ]; then
    echo "Output file must be different from script file."
    exit
fi
printf "Script executing..."

# designate output file
OUT_FILE=$1

# (re)create output file
rm $OUT_FILE
touch $OUT_FILE


# header
printf "Collin Bauer\nCSCI 340 - Operating Systems\nDr. Crosby\nSpring 2020\n\n" >> $OUT_FILE
echo "Note that, while I do have a Ubuntu VM on my Windows laptop, I also have a Linux laptop." >> $OUT_FILE
echo "I plan to do most coding from my Linux laptop, but test sensitive code on the VM." >> $OUT_FILE
printf "\nThe following output is from my Linux laptop.\n\n\n" >> $OUT_FILE


# 1-a) Commands from homework instructions
echo "====uname output====" >> $OUT_FILE
uname -a >> $OUT_FILE
printf "\n\n" >> $OUT_FILE

echo "====ps output====" >> $OUT_FILE
ps -al >> $OUT_FILE
printf "\n\n" >> $OUT_FILE

echo "====cat meminfo output====" >> $OUT_FILE
cat /proc/meminfo >> $OUT_FILE
printf "\n\n" >> $OUT_FILE

echo "====cat cpuinfo output====" >>$OUT_FILE
cat /proc/cpuinfo >> $OUT_FILE
printf "\n" >> $OUT_FILE


# 1-b) What these commands do
echo "====Explanations of uname and ps commands====" >> $OUT_FILE
# uname
echo "uname (short for username) prints the user information from the system and related data, such as OS version, information, and time the command was run" >> $OUT_FILE
# ps
echo "ps (short for processes) outputs a list of currently running processes." >> $OUT_FILE
echo "  -l makes the output take a long-hand form, reporting more information like parent process ID and memory address." >> $OUT_FILE
echo "  -a extends the list to include all running processes, not just those visible to the bash shell." >> $OUT_FILE
echo "  -al combines the functionality of both above arguments." >> $OUT_FILE
printf "\n\n" >> $OUT_FILE


# 2-b) Git status from ostep (copied and pasted)
echo "====Git status output====" >> $OUT_FILE
echo "On branch master" >> $OUT_FILE
echo "Your branch is up to date with 'origin/master'." >> $OUT_FILE
echo >> $OUT_FILE
echo "nothing to commit, working tree clean" >> $OUT_FILE

printf "Done.\n"
exit
