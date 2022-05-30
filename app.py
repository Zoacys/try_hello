from flask import Flask
from flask import request
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/')
@swag_from('colors.yml')
def hello_world():
    name = request.args.get("name", "")
    print(f"name:{name}")
    if name:
        return 'hello ' + name
    else:
        return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
