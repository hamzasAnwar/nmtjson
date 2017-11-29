from flask import Flask, abort, jsonify

app = Flask(__name__)

print (flush=True,values='gasg')

def translate(text)
	translate.main()
	//add NMT Translator here
    return text.upper()


@app.route('/nmt/api/v1.0/translate/<string:text>', methods=['GET'])
def get_translate(text):
    object = translate(text)
    if len(object) == 0:
        abort(404)
    return jsonify({'text':text,'translation': object})




if __name__ == '__main__':
    app.run(debug=True)
