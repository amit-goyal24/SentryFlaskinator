from flask import Flask
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# Initialize Sentry
sentry_sdk.init(
    dsn='',  # Add your Sentry DSN here
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0,
    debug=True
)

app = Flask(__name__)  # __name__ not _name_

@app.route('/')
def index():
    return "Welcome to Flask + Sentry"

@app.route('/err')  # 'App' ➡️ 'app' (case sensitive!)
def trigger_err():
    division_by_zero = 1 / 0
    return str(division_by_zero)

if __name__ == '__main__':  # '__name__' and '__main__'
    app.run(debug=True)
