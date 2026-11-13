import json
from flask import Flask, request, Response, send_from_directory

app = Flask(__name__)

# palvelimen juuri, http://127.0.0.1:3000/
@app.route('/')
def hello():
    print("Helloa kutsuttu!")
    return "No moro! Tervetuloa palvelimelle!"

# laskin reitti, esim. http://127.0.0.1:3000/sum?number1=3&number2=6.5
@app.route('/sum')
def calculate_sum():
    args = request.args
    print(args)
    number1 = float(args.get("number1"))
    number2 = float(args.get("number2"))
    total_sum = number1+number2
    #return str(total_sum)
    response = {
        "sovellus": "yhteenlaskukone",
        "number1": number1,
        "number2": number2,
        "result": total_sum
    }
    return response

# laskin reitti v2, esim. http://127.0.0.1:3000/sum2/3/6.5
@app.route('/sum2/<number1>/<number2>')
def calculate_sum2(number1, number2):
    try:
        number1 = float(number1)
        number2 = float(number2)
        total_sum = number1+number2
        #return str(total_sum)
        response = {
            "sovellus": "yhteenlaskukone",
            "number1": number1,
            "number2": number2,
            "result": total_sum
        }
        return response
    except ValueError:
        response_content = json.dumps({"message": "virheellinen pyyntö, tarkasta arvot"})
        response = Response(response=response_content, status=400, mimetype="application/json")
        return response

# esimerkki html-tyyppisestä vastauksesta
@app.route('/joku-sivu')
def htmlpage():
    response_content = """
    <html>
    <h1>Testailua vaan</h1>
    <p>Tämä on epävalidi html sivu</p>
    </html>
    """
    return response_content


@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message": "Invalid endpoint",
        "status": 404
    }
    json_response = json.dumps(response)
    http_response = Response(response=json_response, status=404, mimetype="application/json")
    return http_response


# Www-sivusto ("client")
# index.hmtl aina polun juuresta
@app.route('/sivusto/')
def serve_index():
    return send_from_directory('client', "index.html")
# kaikki tiedostot client-kansiosta tiedoston nimellä
# esim. http://127.0.0.1:3000/sivusto/client.js
@app.route('/sivusto/<path:filename>')
def serve_static(filename):
    return send_from_directory('client', filename)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)
