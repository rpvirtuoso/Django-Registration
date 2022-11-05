from django.http import Http404


class RestrictingAccessMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path == "/login" or request.path == "/signup" or request.path == "/home" or request.path == "/logout" \
                or request.path == "/change-password" or request.path == "/admin/":
            pass
        else:
            print(request.path)
            raise Http404

        response = self.get_response(request)
        return response
