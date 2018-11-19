#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import argparse
import csv
import os
import datetime
import pandas as pd
import getpass
import random
from scipy import linalg 
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def compare(txt,e):

    count=0
    if e:
        while email(txt) and count < 2:
            count=count+1
        return count

    if txt == open('words.txt','a+').read():
        return count
    else:
        outfile=open('words.txt',"w")
        outfile.write(txt)
        outfile.close()
        while email(txt) and count < 2:
            count=count+1
    
    return count
 
def email(txt):
  
    toaddr=["ofgarci@sandia.gov","ogarci79@gmail.com","divaldez80@gmail.com"]

    print "Enter Password for words.ogarci79@gmail.com"
    password=getpass.getpass()

    for to in toaddr:
        try:
            fromaddr = "words.ogarci79@gmail.com"
            msg = MIMEMultipart()
            msg['From'] = fromaddr
            msg['To'] = to
            msg['Subject'] = "Weekly Words: Week " + str(datetime.date.today().isocalendar()[1])
   
            body = txt
            msg.attach(MIMEText(body, 'plain'))
    
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddr, password)
            text = msg.as_string()
            server.sendmail(fromaddr, to, text)
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

    args = parser.parse_args()
    return [args.words, args.favor, args.week, args.email]

def main():

    words=[]
    words=readFile(words)
    [p,f,w,e]=parse()
    numWords=10

    if f:
        words=words[pd.notnull(words['Favor'])]
        words.index=range(len(words.index))

    if w:
        random.seed(datetime.date.today().isocalendar()[1])
        p=numWords

    w = p if p != 0  else len(words)
    w = w if w < len(words) else len(words)
    deck = list(range(len(words)))

    m=numWords
    for n in range(0,m):
        random.shuffle(deck)

    k=1
    txt=""
    for n in deck[:w]:
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
        print("\t\t\t\t\t\t\t\tCount: " + str(k) + " of " + str(w) + "\n\n\n\n")
        k=k+1
        s=raw_input("Press Enter to continue ...")
        os.system('clear')
        txt=txt + words['Word'][n] + " (" + words['Type'][n] + ") - " + words['Definition'][n] + "\n"

    if f and w != len(words):
        if compare(txt,e) == 2:
            print "Failed to Send Email!"

    print("\n\n\n\n\t\t\t\t\t\t\t\tAll Done(" + str(w) + "/" + str(w) +")!\n\n\n\n")

if __name__ == "__main__":
    main()

