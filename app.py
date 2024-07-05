from flask import Flask
from flask_restful import Resource, Api
from index import auto_comment
from media.xhs import XHSMedia

app = Flask(__name__)
api = Api(app)

driver = auto_comment(XHSMedia)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class ScrollBehavior(Resource):
    def get(self):
        driver.media.disguise()
        print('scroll')
        return {'hello': 'scroll'}
class searchKeywords(Resource):
    def get(self):
        
        return {'111'}

api.add_resource(HelloWorld, '/')

api.add_resource(ScrollBehavior, '/scroll')

if __name__ == '__main__':
    app.run(debug=True)