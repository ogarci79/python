#!/usr/bin/env python

import argparse
import csv
import os
import datetime
import pandas as pd
import getpass
import random
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def compare(txt,e,toaddr,sub):

    count=0
    if txt != open('words.txt','a+').read():
        outfile=open('words.txt',"w")
        outfile.write(txt)
        outfile.close()
        while email(txt,toaddr,sub) and count < 2:
            count=count+1
        return count

    if e:
        while email(txt,toaddr,sub) and count < 2:
            count=count+1
        return count

    
    return count
 
def email(txt,toaddr,sub):
  

    print "Enter Password for words.ogarci79@gmail.com (ctr + c to cancel email)"
    password=getpass.getpass()

    try:
        fromaddr = "words.ogarci79@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ", ".join(toaddr)
        msg['Subject'] = sub
   
        body = txt
        msg.attach(MIMEText(body, 'plain'))
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        print "Invalid password"
        if server:
            server.quit()
        return True

    return False



def readFile(words):
    words=pd.read_csv('words.csv')
    return words


def parse():
    parser = argparse.ArgumentParser(description='Increase Vocabulary')
    parser.add_argument('words', type=int, default=0, nargs="?", help='max number of words to review, defalut "All"')
    parser.add_argument('--favor', '-f', help='Only Favored Words', action='store_true')
    parser.add_argument('--week', '-w', help='weekly set of 10', action='store_true')
    parser.add_argument('--email', '-e', help='Send words to ogarci79@gmail.com and ofgarci@sandia.gov', action='store_true')
    parser.add_argument('--seed', '-s', type=int, help='set seed')

    args = parser.parse_args()
    return [args.words, args.favor, args.week, args.email, args.seed]

def main():

    toaddr=["ofgarci@sandia.gov","ogarci79@gmail.com","divaldez80@gmail.com"]
    words=[]
    words=readFile(words)
    [p,f,w,e,s]=parse()
    numWords=10
    cede=datetime.date.today().isocalendar()[1]

    if f:
        words=words[pd.notnull(words['Favor'])]
        words.index=range(len(words.index))

    if w:
        random.seed(cede)
        p=numWords

    if s:
        random.seed(s)

    p = p if p != 0  else len(words)
    p = p if p < len(words) else len(words)
    deck = list(range(len(words)))

    m=numWords
    for n in range(0,m):
        random.shuffle(deck)

    k=1
    txt=""
    for n in deck[:p]:
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n\n\n\n\n\n\n\n\n\n")
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n")
        print("\t\t\t\t\t\t\t\tDefinition: " + words['Definition'][n])
        print("\t\t\t\t\t\t\t\tSynonyms: " + words['Synonyms'][n])
        print("\t\t\t\t\t\t\t\tSentence: " + words['Sentence'][n])
        print("\t\t\t\t\t\t\t\tType: " + words['Type'][n])
        print("\t\t\t\t\t\t\t\tPronunciation: " + words['Pronunciation'][n])
        print("\t\t\t\t\t\t\t\tCount: " + str(k) + " of " + str(p) + "\n\n\n\n")
        k=k+1
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
        txt=txt + words['Word'][n] + " (" + words['Type'][n] + ") - " + words['Definition'][n] + "\n"

    if e and f and w:
        sub = "Weekly Words: Week " + str(cede)
        if compare(txt,e,toaddr,sub) == 2:
            print "Failed to Send Email!"
    elif e:
        sub = "Words: Random"
        count=0
        while email(txt,toaddr,sub) and count < 2:
            count=count+1
        if count==2:
            print "Failed to Send Email!"

    print("\n\n\n\n\t\t\t\t\t\t\t\tAll Done(" + str(p) + "/" + str(p) +")!\n\n\n\n")

if __name__ == "__main__":
    main()

