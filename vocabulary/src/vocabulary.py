#!/usr/bin/env python3

import argparse
import csv
import os
import datetime
import pandas as pd
import getpass
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def printStuff(p,cede,toaddr,f,w,e,deck,words,c,numWords):

    k=1
    output=""
    for n in deck[:p]:
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n\n\n\n\n\n\n\n\n\n")
        s=input("Press Enter to continue ...")
        os.system('clear')
        print("\n\n\n\n\t\t\t\t\t\t\t\t" + words['Word'][n] + " (" + words['Type'][n] + ")\n\n")
        print("\t\t\t\t\t\t\t\tDefinition: " + words['Definition'][n])
        print("\t\t\t\t\t\t\t\tSynonyms: " + words['Synonyms'][n])
        print("\t\t\t\t\t\t\t\tSentence: " + words['Sentence'][n])
        print("\t\t\t\t\t\t\t\tType: " + words['Type'][n])
        print("\t\t\t\t\t\t\t\tPronunciation: " + words['Pronunciation'][n])
        print("\t\t\t\t\t\t\t\tCount: " + str(k) + " of " + str(p) + "\n\n\n\n")
        print("\n\n\n\t\t\t\t\t\t\t\t")
        k=k+1
        s=input("Press Enter to continue ...")
        os.system('clear')
        #output=output + words['Word'][n] + " (" + words['Type'][n] + ") - " + words['Definition'][n] + "<br>"
        if c:
            output=(output + words['Word'][n] + " (" + words['Type'][n] + ")\n\tDefinition: " + words['Definition'][n] + "\n\tSynonyms: " 
                + words['Synonyms'][n] + "\n\tSentence: " + words['Sentence'][n] + "\n\tType: " + words['Type'][n]
                + "\n\tPronunciation: " + words['Pronunciation'][n] + "\n")
        else:
            output=output + words['Word'][n] + " (" + words['Type'][n] + ") - " + words['Definition'][n] + "\n"

    if f and w:
        sub = "Weekly Words: Week " + str(cede)
        if compare(output,e,toaddr,sub,c,numWords,p) == 2:
            print("Failed to Send Email!")
    elif e:
        sub = "Words: Random"
        count=0
        max_count=10000
        while email(output,toaddr,sub) and count < max_count:
            count=count+1
        if count==max_count:
            print("Failed to Send Email!")

    print("\n\n\n\n\t\t\t\t\t\t\t\tAll Done(" + str(p) + "/" + str(p) +")!\n\n\n\n")
    


def compare(output,e,toaddr,sub,c,numWords,p):

    maxLoop=10000
    count=0
    if not c and output != open('/home/ogarci79/code/python/vocabulary/src/words.txt','a+').read() and p==numWords:
        outfile=open('/home/ogarci79/code/python/vocabulary/src/words.txt',"w")
        outfile.write(output)
        outfile.close()
        while email(output,toaddr,sub) and count < maxLoop:
            count=count+1
        return count

    if e:
        while email(output,toaddr,sub) and count < maxLoop:
            count=count+1
        return count
    
    return count


 
def email(output,toaddr,sub):

    #print "Enter Password for words.ogarci79@gmail.com ('Ctrl + c' to cancel email)"
    #password=getpass.getpass()
    password="a1e5c3b2"

    try:
        fromaddr = "words.ogarci79@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = ", ".join(toaddr)
        msg['Subject'] = sub
   
        output=output + "\nhttps://www.merriam-webster.com/word-games/vocabulary-quiz"
        body = output
        msg.attach(MIMEText(body, 'plain'))
        #msg.attach(MIMEText(body, 'Rich Text'))
        #msg.attach(MIMEText(body, 'html'))
    
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, password)
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)
        server.quit()
    except:
        #print "Invalid password"
        #if server:
            #server.quit()
        return True

    return False



def readFile(words):

    words=pd.read_csv('/home/ogarci79/code/python/vocabulary/src/words.csv')
    return words



def parse():

    parser = argparse.ArgumentParser(description='Increase Vocabulary')
    parser.add_argument('words', type=int, default=0, nargs="?", help='max number of words to review, defalut "All"')
    parser.add_argument('--favor', '-f', help='Select only Favored Words', action='store_true')
    parser.add_argument('--week', '-w', help='Weekly set of 5', action='store_true')
    parser.add_argument('--complete', '-c', help='Print complete set of definitions', action='store_true')
    parser.add_argument('--email', '-e', help='Send words to ogarci79@gmail.com and ofgarci@sandia.gov', action='store_true')
    parser.add_argument('--seed', '-s', type=int, help='Set seed')

    args = parser.parse_args()
    return [args.words, args.favor, args.week, args.email, args.seed, args.complete]



def main():

    toaddr=["ofgarci@sandia.gov","ogarci79@gmail.com","divaldez80@gmail.com"]
    #toaddr=["ogarci79@gmail.com"]
    words=[]
    words=readFile(words)
    [p,f,w,e,s,c]=parse()
    numWords=10
    cede=int(datetime.date.today().strftime("%U"))+1

    #print(words)
    #return

    if f:
        words=words[pd.notnull(words['Favor'])]
        words.index=range(len(words.index))
    if w:
        random.seed(cede)
        if p == 0:
            p=numWords
    if s:
        random.seed(s)

    p = p if p != 0  else len(words)
    p = p if p < len(words) else len(words)
    deck = list(range(len(words)))

    m=3
    for n in range(0,m):
        random.shuffle(deck)

    printStuff(p,cede,toaddr,f,w,e,deck,words,c,numWords)

if __name__ == "__main__":
    main()

