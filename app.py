from flask import Flask,jsonify,request,make_response
from flask_restful import Resource, Api
import DC,NewTestament,OldTestament,BoM,ScriptureList,pgp

app = Flask(__name__)
api = Api(app)

@app.errorhandler(404)
def not_found(e):
    response = jsonify({'status': 404,'error': 'not found',
                        'message': 'invalid resource URI'})
    response.status_code = 404
    return response

@app.errorhandler(400)
def bad_request(e):
		response = jsonify({'status': 400,'error': 'bad request',
												'message': 'invalid resource URI'})
		response.status_code = 400
		return response

@app.errorhandler(405)
def method_not_allowed(e):
		response = jsonify({'status': 405,'error': 'method not allowed',
												'message': 'invalid resource URI'})
		response.status_code = 405
		return response

@app.errorhandler(500)
def internal_server_error(e):
		response = jsonify({'status': 500,'error': 'internal server error',
												'message': 'invalid resource URI'})
		response.status_code = 500
		return response

class Help(Resource):
    def get(self):
        oldList = []
        a = ScriptureList.old_list
        for i in range(len(a)):
            oldList.append(a[i][2])
        body = {'OldTestament': oldList}
        return jsonify(body)

class CallOT(Resource):
    def get(self):
        book = request.args.get("book")
        chapter = request.args.get("chapter")
        verseF = request.args.get("start")
        verseT = request.args.get("end")
        master = OldTestament.main(book,chapter,verseF,verseT)
        text = master[0]
        text1 = master[1]
        text2 = master[2]
        body = {'English':text2,'Japanese':text1,'chapter':text}
        return jsonify(body)

class CallNT(Resource):
    def get(self):
        book = request.args.get("book")
        chapter = request.args.get("chapter")
        verseF = request.args.get("start")
        verseT = request.args.get("end")
        master = NewTestament.main(book,chapter,verseF,verseT)
        text = master[0]
        text1 = master[1]
        text2 = master[2]
        body = {'chapter':text,'Japanese':text1,'English':text2}
        return jsonify(body)

class CallBM(Resource):
    def get(self):
        book = request.args.get("book")
        chapter = request.args.get("chapter")
        verseF = request.args.get("start")
        verseT = request.args.get("end")
        master = BoM.main(book,chapter,verseF,verseT)
        text = master[0]
        text1 = master[1]
        text2 = master[2]
        body = {'chapter':text,'Japanese':text1,'English':text2}
        return jsonify(body)

class CallDC(Resource):
    def get(self):
        chapter = request.args.get("chapter")
        verseF = request.args.get("start")
        verseT = request.args.get("end")
        master = DC.main(chapter,verseF,verseT)
        text = master[0]
        text1 = master[1]
        text2 = master[2]
        body = {'chapter':text,'Japanese':text1,'English':text2}
        return jsonify(body)

class CallPG(Resource):
    def get(self):
        book = request.args.get("book")
        chapter = request.args.get("chapter")
        verseF = request.args.get("start")
        verseT = request.args.get("end")
        master = pgp.main(book,chapter,verseF,verseT)
        text = master[0]
        text1 = master[1]
        text2 = master[2]
        body = {'chapter':text,'Japanese':text1,'English':text2}
        return jsonify(body)

api.add_resource(Help, '/api')
api.add_resource(CallOT, '/api/ot')
api.add_resource(CallNT, '/api/nt')
api.add_resource(CallBM, '/api/bom')
api.add_resource(CallPG, '/api/pgp')



if __name__ == "__main__":
	app.run(debug=True)
