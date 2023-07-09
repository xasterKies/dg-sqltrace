def new_middleware(get_response):

    def middleware(request):

        print("before")

        response = get_response(request)

        print("after")

        return response

    return middleware