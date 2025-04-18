from flask import Blueprint, request, jsonify
from flask import render_template, abort
import logging

"""
This imports:
- `Blueprint` from Flask, which allows you to organize routes in a modular way
- `request` to access incoming HTTP request data
- `jsonify` to convert Python dictionaries to JSON responses
- `logging` for error handling and reporting
"""

router = Blueprint('main', __name__)
"""
This creates a Blueprint named 'main'. The __name__ parameter tells Flask where to find the Blueprint's resources. 
This Blueprint will be registered with the main Flask application (as seen in your previous code with app.register_blueprint(main_bp)).
"""


"""
This decorator defines a route at the URL path '/predict' that only accepts POST requests. The function predict() will handle these requests.
"""
@router.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Process input with your AI model
        # Example: result = current_app.model.predict(data['input'])
        return jsonify({'result': 'prediction_here'}), 200
        """
            Inside the function:
            It attempts to parse JSON data from the request body using request.get_json()
            There's a commented placeholder for processing this data with an AI model
            It returns a JSON response with a placeholder result and HTTP status code 200 (OK)
        """
    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500
        """
        Error handling:
        It catches any exceptions that occur during processing
        Logs the error with details
        Returns a JSON error response with HTTP status code 500 (Internal Server Error)
        """

@router.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

"""
This defines a second endpoint at '/health' that only accepts GET requests. 
This is a simple health check endpoint that returns a status message indicating the service is operational
"""

@router.route("/user",methods=['GET'])
def test():
    return jsonify({'status': 'ok', 'message':"Muhammed on da code"}), 200

""" - Variable in URL - """
@router.route("/user/<username>",methods=['GET'])
def test2(username):
    # show the User Profile for that user
    return "User %s" % username

@router.route("/post/<int:post_id>")
def post(post_id):
    # show the post with given id
    return f"post {post_id}"

""" - Templates - """
@router.route("/greeting")
@router.route("/greeting/<string:name>")
def greeting(name=None):
    return render_template("greeting.html", name=name)


""" - Form & Request Object - """
@router.route("/formtest", methods=['POST','GET'])
def form_test():
    if request.method == "POST":
        if 'username' not in request.form:
            abort(404,description="No username provided")
        username = request.form.get('username', 'Guest')  # Default to 'Guest' if missing
        return f"Your Username is => {username}, Welcome"
    return """
        <form method="post" action="/formtest"> 
            Name: <input type="text" name="name"><br>
            <input type="submit" value="Submit">
        </form>
    """



@router.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404