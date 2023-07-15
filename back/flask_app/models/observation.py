from flask_app.config.mysqlconnection import connectToMySQL
from datetime import datetime

class Observation:
    def __init__(self, data):
        #identity
        self.image = data['image']
        self.note = data['note']

        #coordinates
        self.time_s = data['time_s']
        self.lat_deg = data['lat_deg']
        self.long_deg = data['long_deg']
        self.elev_m = data['elev_m']

        #meta
        self.id = data['id']
        self.createdon = data['createdon']
        self.modifiedon = data['modifiedon']
        self.creator_id = data['creator_id']

        #kinds
        self.common_kinds = []
        self.formal_kinds = []

    @classmethod
    def get_all(cls):
        query = """
        SELECT 
            o.id, o.image, o.note, o.time_s, o.lat_deg, o.long_deg, o.elev_m, o.createdon, o.modifiedon, o.creator_id
        FROM 
            observations o
        """
        results = connectToMySQL().query_db(query)
        observations = []
        for result in results:
            observations.append(cls(result))
        return observations

    @classmethod
    def get_observation_by_time( cls, data ):
        query = """
        SELECT * 
        FROM observations o 
        WHERE o.time_s = %(time_s)s
        """
        results = connectToMySQL().query_db(query, data)
        return cls(results[0]) if results else None

    def fetch_common_kinds(self):
        query = """
            SELECT ck.name
            FROM common_kinds ck
            INNER JOIN observation_common_kinds ock ON ock.common_kind_id = ck.id
            WHERE ock.observation_id = %(observation_id)s
        """
        data = {'observation_id': self.id}
        results = connectToMySQL().query_db(query, data)
        self.common_kinds = [result['name'] for result in results]

    def fetch_formal_kinds(self):
        query = """
            WITH RECURSIVE Hierarchy AS (
                    SELECT t.parent_id, fk.name
                    FROM observations o
                    JOIN observation_formal_kinds ofk ON o.id = ofk.observation_id
                    JOIN formal_kinds fk ON ofk.formal_kind_id = fk.id
                    JOIN taxonomy t on fk.id = t.child_id              
                    WHERE o.id = %(observation_id)s
                    
                    UNION ALL
                    
                    SELECT t.parent_id, fk.name
                    FROM Hierarchy h
                    JOIN taxonomy t ON h.parent_id = t.child_id
                    JOIN formal_kinds fk ON t.child_id = fk.id
                )
            SELECT name
            FROM Hierarchy;
        """
        data = {'observation_id': self.id}
        results = connectToMySQL().query_db(query, data)
        self.formal_kinds = [result['name'] for result in results]