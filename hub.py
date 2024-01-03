from StorageAdapter import StorageAdapter


class Hub:
    LS = StorageAdapter()
    """
    HUB - is core of this technology.
    It`s handling incoming requests from services.
    Get requests and redirected for target services.
    Interacting with local storage for getting configurations and ws server for communicate with connected services.
    Annotation: LS - Local storage, WSS - WebSocker Server
    """
    def registry_service(
            self,
            host: str,
            port: int,
            unique_name: str
    ):
        """
        Method for registry new services
        :param host: address of service
        :param port:
        :param unique_name: name of service for fast search in LS
        :return:
        """
        pass

    def handle_request(
            self,
            target_service_name: str,
            message_body: dict
    ):
        pass

    def handle_response(
            self,
            target_service_name: str,
            message_body: dict
    ):
        pass

    def incoming_message_handle(
            self,
            origin_host: str,
            origin_port: int,
            request_type: str,
            target_service_name: str,
            message_body: dict
    ):
        """
        Method - handler incoming requests get configuration from LS
        Logic in developing
        :param origin_host: service host what send request
        :param origin_port: service port what send request
        :param request_type: type of request (registry, request, response)
        :param target_service_name: name of service, where redirect request
        :param message_body: payload for target service request
        :return:
        """
        pass

