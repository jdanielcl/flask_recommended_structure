from . import outer_blueprint

@outer_blueprint.route('/outer', methods=['GET'])
def index():
    return "hello world from outer"

