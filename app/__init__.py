from flask import Flask

# __name__ variable passed to the Flask class is a Python predefined variable
# which is set to the name of the module in which it is used.
app = Flask(__name__)

# Another peculiarity is that the routes module is imported at the bottom and not at the top of the script as it is always done.
# The bottom import is a workaround to circular imports
from app import routes
