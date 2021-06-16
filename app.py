# flask_web/app.py
import os,json,datetime
from flask import Flask,render_template,request
from flask_cors import cross_origin
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Access the following API to generate JMX: /api/gjmx'

@app.route('/api/gjmx',methods=["POST"])
@cross_origin(supports_credentials=True)
def gjmx():   
    return_dict= {'return_code': '200', 'return_info': 'Processed successfully', 'result': False}
    if request.get_data() is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = 'Request parameter is empty'
        return json.dumps(return_dict, ensure_ascii=False)
    get_Data=request.get_data()
    get_Data=json.loads(get_Data)
    project=request.args.get('client_id')
    # get_Data=[{'httpsp': {'domain': '','port': '','protocol': '','contentEncoding': '','path': '','method':'GET','follow_redirects': 'true','auto_redirects': 'false','use_keepalive': 'true','DO_MULTIPART_POST': 'false','embedded_url_re': '','connect_timeout': '','response_timeout': ''},'headerm': {'authorization': 'AuthorizationToken','authority':'','method':'GET'}}]
    with open(project+'.jmx','w') as f:
        f.write(str(render_template('templates.jmx',lst=get_Data)))
    return_dict['result']='Generate Success!'
    return json.dumps(return_dict, ensure_ascii=False)
 
if __name__== '__main__':
    app.run(debug=True, host='0.0.0.0')
