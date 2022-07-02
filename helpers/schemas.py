class Schemas:
    TOP_RATED_200 = {'page': {'type': 'integer'},
                     'results': {'type': 'list'},
                     'total_results': {'type': 'integer'},
                     'total_pages': {'type': 'integer'}
                     }
    TOP_RATED_401 = {'success': {'type': 'boolean'},
                     'status_code': {'type': 'integer'},
                     'status_message': {'type': 'string'}
                     }
