from flask import Flask,render_template,request, redirect, url_for,flash
import requests
import boto3
from boto3.session import Session
import cStringIO
import os
import urllib2
from yattag import Doc
from stat import *

app=Flask(__name__)

'''
session = Session(aws_access_key_id='',
                  aws_secret_access_key='',
                  region_name='')

ec2 = session.resource('s3')
ec2_us_west_2 = session.resource('ec2', region_name='us-west-2')
s3client = boto3.client('s3')


s3client.create_bucket(Bucket='thisismythird')
'''

@app.route('/', methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        uname=request.form['uname']
	userfile=os.path.dirname(__file__)+'/users.txt'
        f=open(userfile)
        for line in iter(f):
            if uname in line:
                abc=1
                break
            else:
                abc=0
        if abc==1:
            return render_template('home2.html')
    return render_template('home.html')


@app.route('/home2', methods=['GET','POST'])
def home():
    if request.method == "POST":
        #return 'testing'
        #return render_template('home2.html')
        filename=request.files['file']
        session = Session(aws_access_key_id='A',
                  aws_secret_access_key='',
                   region_name='')
        s3= session.resource('s3')
        s3.create_bucket(Bucket='thisonebucket')
        contents=filename.read()
        fname=filename.filename
        fsize=len(contents)
        userfile=os.path.dirname(__file__)+'/users.txt'
        #return contents
        s3.Bucket('thisismythirdPaush1123').put_object(Key=str(filename.filename), Body=contents)
        print 'abc'
        print str(fname)
        print str(fsize)

    return render_template('home2.html')

@app.route('/view',methods=['GET','POST'])
def view():
    rSet = []
    fileNameSet=[]
    if request.method == "GET":
        session = Session(aws_access_key_id='',
                      aws_secret_access_key='+2C',
                       region_name='us-east-1')
        s3= session.resource('s3')
        bucket = s3.Bucket('thisismythirdPaush1123')

        for key in bucket.objects.all():
    #         print(key.key)
            #chk = key.key.split('/')
            link = 'https://s3.amazonaws.com/' + 'thisismythirdPaush1123' + '/' + key.key
    #             print link
            rSet.append(link)
    #             print calcSize(key.size)
                #fsize.append(calcSize(key.size, ''))
    #             print key.last_modified
    #         lmd.append(key.last_modified)
            fileNameSet.append(key.key)
    return render_template('view.html',list=rSet,FileName=fileNameSet)

'''@app.route('/delete',methods=['GET','POST'])
def delete():
    return 'test'
    if request.method == "POST":
        return 'test'
        FileId=request.form('mydata')
        session = Session(aws_access_key_id='',
                  aws_secret_access_key='+2C',
                   region_name='us-east-1')
        s3 = session.resource('s3')
        s3.Object('thisismythirdPaush1123',FileId).delete()
'''

@app.route('/delete',methods=['GET','POST'])
def delete():
     if request.method=="POST":
        FileId=request.form['mydata']
        #return str(FileId)
        session=Session(aws_access_key_id='',
                  aws_secret_access_key='',
                   region_name='')
        s3=session.resource('s3')
        s3.Object('thisismythirdPaush1123',FileId).delete()


if __name__ == '__main__':
   app.run(debug=True)
