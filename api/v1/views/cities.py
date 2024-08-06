#!/usr/bin/python3
"""
Same as State, create a new view for City objects
"""

@app_views.route('/states/<state_id>/cities/')
def list_cities_of_state(state_id):
    '''cities objects'''
    obj = storage.get("State", state_id)
    if not obj:
        abort(404)
    list_cities = [city.to_dict() for city in obj.cities]
    return (jsonify(list_cities))


@app_views.route('/states/<state_id>/cities/', methods=['POST'])
def create_city(state_id):
    '''post new'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    obj = storage.get("State", state_id)
    if not obj:
        abort(404)
    city = City(name=request.json['name'], state_id=state_id)
    storage.new(city)
    storage.save()
    return (jsonify(city.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete(city_id):
    '''Deletes'''
    obj = storage.get("City", city_id)
    if not obj:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/cities/<city_id>')
def get_city(city_id):
    '''Retrieves a City object'''
    obj = storage.get("City", city_id)
    if not obj:
        abort(404)
    return (jsonify(obj.to_dict()))
