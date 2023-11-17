from flask_app import app
from flask import jsonify
from flask_app.models.observation import Observation

@app.route('/api/o', methods=['GET'])
def get_observations():
    observations = Observation.get_all()
    observation_data = []
    for observation in observations:
        observation_data.append({
            'id': observation.id,
            'createdon': observation.createdon,
            'modifiedon': observation.modifiedon,
            'creator_id': observation.creator_id,
            'elev_m': observation.elev_m,
            'image': observation.image,
            'lat_deg': observation.lat_deg,
            'long_deg': observation.long_deg,
            'note': observation.note,
            'time_s': observation.time_s,
        })
    return jsonify(observation_data)

@app.route('/api/o/<int:time_s>', methods=['GET'])
def get_observation_by_time(time_s):
    observation = Observation.get_observation_by_time({'time_s': time_s})
    observation.fetch_formal_kinds()
    observation.fetch_common_kinds()
    if observation:
        observation_data = {
            'id': observation.id,
            'createdon': observation.createdon,
            'modifiedon': observation.modifiedon,
            'creator_id': observation.creator_id,
            'elev_m': observation.elev_m,
            'image': observation.image,
            'lat_deg': observation.lat_deg,
            'long_deg': observation.long_deg,
            'note': observation.note,
            'time_s': observation.time_s,
            'common_kinds': observation.common_kinds,
            'formal_kinds': observation.formal_kinds
        }
        return jsonify(observation_data)
    else:
        return jsonify({'error': 'Observation not found'})

if __name__ == '__main__':
    app.run()