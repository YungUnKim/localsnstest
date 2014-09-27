1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
# -*- coding:utf-8 -*-
'''
 
 
    ___________________________________
___/ YOUR GOOGLE APPENGINE FOLDER PATH \__________________________________________________
                                                                                       '''
MODE = 'UPDATE'
 
'''
GOOGLE_APPENGINE_PATH : Path of directory which has appcfg.py
MODE :
    'UPDATE'   => execute update
    'ROLLBACK' => execute appengine rollback
 
______________________________________________________________________________________/'''
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
def auto_newline(string, bound) :
    if bound < 3 : raise ValueError("bound value should be bigger than 2.")
    splitted_str, bound = "", bound - 2
    while True :
        if len(string) <= bound : return splitted_str + ' ' + string
        splitted_str += ' %s %s' % (string[:bound], os.linesep)
        string = string[bound:]
 
""" Path Setting : MODIFY YOUR GOOGLE-APPENGINE PATH """
import platform
OS = platform.system()
 
if OS == 'Darwin' : GOOGLE_APPENGINE_PATH = "/usr/local/google_appengine"
elif OS == 'Windows' : GOOGLE_APPENGINE_PATH = "C:\\Program Files (x86)\\Google\\google_appengine"
else : raise ValueError('OS VALUE IS NOT VALID : %s not in [Darwin, Windows]' % OS)
 
import os, sys
 
try :
    sys.path.insert(0, GOOGLE_APPENGINE_PATH)
    from appcfg import run_file
except:
    GOOGLE_APPENGINE_PATH = "C:\\Program Files\\Google\\Cloud SDK\\google-cloud-sdk\\platform\\google_appengine"
    sys.path.insert(0, GOOGLE_APPENGINE_PATH)
    from appcfg import run_file
 
 
""" Deploy """
print "======= Google App Engine Deploy Script ========================================"
cfg_path = os.path.join(GOOGLE_APPENGINE_PATH, "appcfg.py")
if MODE == 'ROLLBACK' : cmd_depl = 'rollback'
elif MODE == 'UPDATE' : cmd_depl = 'update'
else : raise ValueError('MODE VALUE IS NOT VALID : %s not in [ROLLBACK, UPDATE]' % MODE)
prj_path = os.path.abspath(".")
print auto_newline(
    " ".join([
        "python",
        "'%s'" % cfg_path,
        "--oauth2",
        cmd_depl,
        "'%s'" % prj_path
    ]),
    80
)
print "================================================================================"
 
""" Execute """
 
while len(sys.argv) > 0 :
    sys.argv.pop()
sys.argv.append(cfg_path)
sys.argv.append("--oauth2")
sys.argv.append(cmd_depl)
sys.argv.append(prj_path)
run_file(cfg_path, globals())
 
""" Recover Path """
sys.path.pop(0)