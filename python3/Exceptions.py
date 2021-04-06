def validate_broker_signup_request(request):
    try:    
        email = request.data.get("email")
        contact_id = request.data.get("contact_id")
        if email is None:
            raise Exception("Bad Request, no email address supplied")
        if "@" not in email:
            raise Exception("Bad Request, invalid email address")
        if contact_id is None:
            raise Exception("Bad Request, no contact id supplied")

    except Exception as e:
        debugging and logger.exception(e)
        return JsonResponse({"status": getattr(e, "args", repr(e))}, status=HTTP_400_BAD_REQUEST)
