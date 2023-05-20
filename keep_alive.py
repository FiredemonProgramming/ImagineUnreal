abb1=["#e50000","#0343df","#15b01a","#ffff14","#9a0eea","#f97306","#0f9b8e","#bbf90f","#fcb001","#5d06e9","#fd3c06","#ff81c0","#000000"]
# -*- coding: utf-8 -*-
from flask import Flask, request, redirect
from flask import render_template
import subprocess
try:
    from sympy import*
except:
    import sys
    ddddd=sys.executable
    subprocess.check_call([ddddd, "-m", "pip", "install", "sympy"])
    from sympy import*
try:
    import matplotlib.pyplot as plt
except:
    import sys
    ddddd=sys.executable
    subprocess.check_call([ddddd, "-m", "pip", "install", "matplotlib"])
    import matplotlib.pyplot as plt
try:
    import numpy as np
except:
    import sys
    ddddd=sys.executable
    subprocess.check_call([ddddd, "-m", "pip", "install", "numpy"])
    import numpy as np
app = Flask(__name__)
z=[]
lcheck=""
x1=None
justalpha=["a","b","c","d","e","f","g","h","k","l","m","n"]
@app.route('/', methods=['GET','POST'])
def home():
    global gooodstuff
    global z
    global justalpha
    global lcheck
    global x1
    z=[]
    hhh3=[]
    hhh4=["","","","","","","","","","","",""]
    label15=""
    lcheck=""
    somethingpicture="/static/graph_empty.png"
    somethingpicture1="../static/graph_empty.png"
    if request.method=="POST":
        if request.form.get('action2') == 'Посчитать':
            for hhh in range(1,13):
                x1=str(request.form[str(hhh)])
                x1=x1.replace(" ","")
                if x1!="" and x1!=None:
                    hhh4[hhh-1]=str(x1)
                    lcheck=None
                    x4=str(x1).replace('i','j')
                    _locals = locals()
                    try:
                        exec("global lcheck; lcheck=("+str(x4)+")")
                    except:
                        lcheck=""
                    try:
                        lcheck=simplify(str(x4))
                    except:
                        lcheck=""
                    try:
                        if "i" in str(lcheck) or "j" in str(lcheck) or "I" in str(lcheck) or "J" in str(lcheck):
                            check=False
                            hhh3.append(hhh-1)
                            for i in range(len(z)):
                                try:
                                    z[i]=str(z[i]).replace('i','j')
                                except:
                                    None
                                try:
                                    _locals = locals()
                                    exec("global z; z[i]=complex("+str(z[i])+")")
                                except:
                                    None
                            x2=str(x1).replace('i','j')
                            _locals = locals()
                            exec("global z; z.append(complex("+str(x2)+"))")
                        else:
                            print(lcheck)
                    except:
                        print(lcheck)
            try:
                x1=str(request.form["13"])
                if x1!="" and x1!=None:
                    for gh in range(0,12):
                        x1=str(x1).lower().replace(justalpha[gh],"("+hhh4[gh]+")")
                    try:
                        x4 = str(x1).replace('i', 'j')
                        exec("simplify("+x4+")")
                        hhh3.append(12)
                        lcheck = None
                        _locals = locals()
                        exec("global lcheck; lcheck=(" + str(x4) + ")")
                        lcheck = simplify(str(x4))
                        try:
                            if "i" in str(lcheck) or "j" in str(lcheck) or "I" in str(lcheck) or "J" in str(lcheck):
                                check = False
                                for i in range(len(z)):
                                    try:
                                        z[i] = str(z[i]).replace('i', 'j')
                                    except:
                                        None
                                    try:
                                        _locals = locals()
                                        exec("global z; z[i]=complex(" + str(z[i]) + ")")
                                    except:
                                        None
                                x2 = str(x1).replace("i","j")
                                _locals = locals()
                                exec("global z; z.append(round(complex(" + str(x2) + ").real, 2) + round(complex(" + str(x2) + ").imag, 2) * 1j)")
                            else:
                                print(lcheck)
                        except Exception as gggg:
                            print(gggg)
                            print(lcheck)
                    except Exception as fgg:
                        None
            except Exception as agg:
                print(agg)
            try:
                label15=""
                if "i" in str(lcheck) or "j" in str(lcheck) or "I" in str(lcheck) or "J" in str(lcheck):
                    print(z,hhh3)
                    import math
                    import sympy
                    bbb2=""
                    axis_type=2
                    whatcolor=hhh3
                    if True:
                        w=max(np.abs(z))
                        print(abs(w))
                        fig, ax = plt.subplots()
                        if axis_type==0:
                            plt.axis("off")
                            plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
                            plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
                        elif axis_type==1:
                            plt.axis("on")
                            plt.grid()
                            plt.text(-0.15*w, 0.8*w, "Im", fontsize=14)
                            plt.text( 0.8*w,-0.15*w, "Re", fontsize=14)
                        else:
                            plt.grid()
                            ax.spines['left'].set_position('center')
                            ax.spines['bottom'].set_position('center')

                            ax.spines['right'].set_color('none')
                            ax.spines['top'].set_color('none')

                            ax.xaxis.set_ticks_position('bottom')
                            ax.yaxis.set_ticks_position('left')

                            ax.set_xlabel('                                                 Re')
                            ax.set_ylabel('                                                 Im')

                        plt.xlim(-w,w)
                        plt.ylim(-w,w)

                        plt.arrow(0, -w, 0, 1.9*w, head_width=w/20, head_length=w/20, fc='k', ec='k');
                        plt.arrow(-w, 0, 1.9*w, 0, head_width=w/20, head_length=w/20, fc='k', ec='k');
                        abb=["xkcd:red","xkcd:blue","xkcd:green","xkcd:yellow","xkcd:violet","xkcd:orange","xkcd:bluegreen","xkcd:yellowgreen","xkcd:yellow orange","xkcd:blue violet","xkcd:red orange","xkcd:pink","xkcd:black"]
                        for i in range(len(z)):
                            fi_a=np.angle(z[i])
                            x=z[i].real -abs(w)/20*np.cos(fi_a)
                            y=z[i].imag-abs(w)/20*np.sin(fi_a)
                            plt.arrow(0, 0, x, y, head_width=w/20, head_length=w/20, fc='b', ec='b').set_color(abb[whatcolor[i]])
                            ans1='∠'+str(round(float(fi_a)*(180/np.pi),1))+"°"
                            print(z[i],ans1)
                            um=(z[i].real)**2
                            um1=(z[i].imag)**2
                            tem=round(um+um1,3)
                            ans=sympy.nsimplify('sqrt('+str(tem)+')')
                            if '/' in str(ans):
                                ans='sqrt('+str(tem)+')'
                            ans=str(ans).replace('sqrt','√')
                            ans=str(ans).replace('*','')
                            print(z[i],ans)
                            print(z[i],str(ans)+str(ans1))
                            bbb2+=str(ans+ans1).replace("(","").replace(")","")+" = "+str(z[i]).replace("(","").replace(")","").replace("j","i")+"\n"
                        plt.savefig('static/graph.png')
                    label15="Результат<br/>"
                    print(len(bbb2.split('\n')))
                    for i in range(len(bbb2.split('\n'))-1):
                        #position: absolute;
                        label15+='<div style="position: absolute; background-color: '+abb1[hhh3[i]]+'; clear: left;" class="square"></div>'+'<p style="margin-left: 20px; color: #f3d01b">'+bbb2.split('\n')[i].replace('<','&lt;').replace('>','&gt;')+"</p>"
                    somethingpicture="/static/graph.png"
                    somethingpicture1="../static/graph.png"
                else:
                    label15="Результат<br/><br/>"+str(lcheck)
            except Exception as jhj:
                print(jhj)
                print(lcheck)
        if somethingpicture=="/static/graph_empty.png":
            if label15=="Результат<br/><br/>" or label15==None or label15=="Результат<br/><br/>()":
                label15='Результат<br/><p style="color: #e50000">Что-то пошло не так! Убедитесь что ввод корректный и попробуйте еще раз</p>'
    return open("templates/home.html","r",encoding="utf-8").read().replace("THISISASPLIT","<p>"+str(label15)+"</p>").replace("HAHAHHAHAHAHHA",somethingpicture).replace("whatw",somethingpicture1)

@app.route('/doc', methods=['GET'])
def doc():
    return open("templates/doc.html","r",encoding="utf-8").read()

#@app.route('/nonstand', methods=['GET'])
#def nonstand():
#    return open("templates/nonstand.html","r",encoding="utf-8").read()
def keep_alive():
    app.run(
        host='0.0.0.0',
        port=200
    )
def run():
    t=Thread(target=run)
    t.start()
