# -*- coding: utf-8 -*-


class CodingOpenAPIException(Exception):
    def __init__(self, code, message, request_id=None):
        self.code = code
        self.message = message
        self.request_id = request_id

    def __str__(self):
        return f"""
        Request ID: {self.request_id}
        Error Code: {self.code}
        Error Message: {self.message}
        """


def raise_if_error(response: dict):
    if 'Error' in response['Response']:
        raise CodingOpenAPIException(code=response['Response']['Error']['Code'],
                                     message=response['Response']['Error']['Message'],
                                     request_id=response['Response']['RequestId'])
