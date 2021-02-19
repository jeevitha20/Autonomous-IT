import boto3
import json
from flask import Flask, request, render_template

app = Flask(__name__,template_folder='templates')

@app.route('/', methods =["GET", "POST"])
def hello():
    if request.method == "POST":
        with open("C:/Users/yesgo/Desktop/flaskproject/awstemplate.json") as f:
            data = json.load(f)
        data['Parameters']['KeyName']['Default'] = request.form.get("Keypair")
        data['Parameters']['DBUser']['Default'] = request.form.get("Dbuser")
        data['Parameters']['DBPassword']['Default'] = request.form.get("Dbpass")
        data['Parameters']['DBRootPassword']['Default'] = request.form.get("Dbroot")
        data['Parameters']['InstanceType']['Default'] = request.form.get("Itype")
        # print(data['Parameters']['KeyName']['Default'])
        client = boto3.client('cloudformation',
            region_name = 'ap-south-1',
            aws_access_key_id='AKIA2PNU57XCKEC5Y7EF',
            aws_secret_access_key='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')
        
        response = client.create_stack(
            StackName=request.form.get("sname"),
            TemplateBody=json.dumps(data),
            DisableRollback=False,
        )
    return render_template("second.html")


if __name__ == '__main__':
    app.run()


 
