from . import main

print("inside views")
@main.route('/', methods=['GET'])
def index():
    return "hello world"

