from rest_framework.renderers import JSONRenderer


class CustomRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None, version=1.0):
        status_code = renderer_context['response'].status_code

        response = {
            "version": version,
            "status": True,
            "statusCode": status_code,
            "result": data,
            'message': "",
            "error": {}
        }

        if not str(status_code).startswith('2'):
            response["status"] = False

            if isinstance(data, dict):
                print("data", data)
                message = data.get('message')
                error = data.get('error')

                if not message and data:

                    response['message'] = message
                    response['result'] = {}
                    response['error'] = data

                elif message:

                    response['message'] = message
                    response['error'] = data
                    response['result'] = {}
                    del data["message"]
                else:
                    print('here')

        elif isinstance(data, dict):
            message = data.get("message", None)
            response["message"] = message if message else "successfully executed"
            if "message" in data.keys():
                del data["message"]
            response["result"] = data

        return super(CustomRenderer, self).render(response, accepted_media_type, renderer_context)
