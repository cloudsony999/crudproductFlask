from flask import Flask, render_template, url_for,request

import db as d

app=Flask(__name__)


@app.route('/')
def index():
    cr=url_for('c')
    ins=url_for('i')
    de=url_for('d')
    return "<body bgcolor='yellow' text='red'><a href={}>Click for create</a>".format(cr)+\
           "<br><a href={}>Click for insert</a>".format(ins)+\
           "<br><a href={}>Click for delete</a>".format(de)+"</body>"


def callInsert():
    return render_template('insert.html')

def callDelete():
    return render_template('delete.html')

def callCreate():
    return render_template('create.html')

app.add_url_rule('/create','c',callCreate)

app.add_url_rule('/insert','i',callInsert)

app.add_url_rule('/delete','d',callDelete)


@app.route('/createsubmit')
def createtable():
    conn=d.setDB()
    cur=conn.cursor()
    tname=request.args.get('t1')
    qry='''
    create table {} (pid integer,pname text(20),price integer)
    '''.format(tname)
    try:
        cur.execute(qry)
        return "<body bgcolor='blue' text='white'><h1>The table has been created....</h1></body>"
    except:
        return "<body bgcolor='black' text='white'><h1>The table has not been created....</h1></body>"
    conn.close()

@app.route('/insertsubmit')
def inserttable():
    conn=d.setDB()
    cur=conn.cursor()
    di=request.args.get('i')
    name=request.args.get('n')
    pr=request.args.get('p')
    print(di,name,pr)
    print("----------------------------")
    try:
        cur.execute("INSERT INTO NEHA VALUES(:a,:b,:c)",{"a":di,"b":name,"c":pr})
        conn.commit()
        return "<body bgcolor='white' text='blue'><h1>Data is inserted....</h1></body>"
    except Exception as e:
        return "<body bgcolor='black' text='white'><h1>insert not done!!!!...."+str(e)+"</h1></body>"
    conn.close()




if __name__=='__main__':
    app.run(debug=True)


