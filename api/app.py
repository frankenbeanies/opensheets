from flask import Flask

from business.business_controller import business_controller

app = Flask(__name__) 

app.register_blueprint(business_controller, url_prefix="/api/business")


if __name__ == "__main__":
    app.run(debug=True)
