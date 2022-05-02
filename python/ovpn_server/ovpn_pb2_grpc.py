# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import ovpn_pb2 as ovpn__pb2


class OVPNStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.list = channel.unary_unary(
                '/ovpn_package.OVPN/list',
                request_serializer=ovpn__pb2.Empty.SerializeToString,
                response_deserializer=ovpn__pb2.ListResponse.FromString,
                )
        self.get_id = channel.unary_unary(
                '/ovpn_package.OVPN/get_id',
                request_serializer=ovpn__pb2.Name.SerializeToString,
                response_deserializer=ovpn__pb2.ID.FromString,
                )
        self.get_name = channel.unary_unary(
                '/ovpn_package.OVPN/get_name',
                request_serializer=ovpn__pb2.ID.SerializeToString,
                response_deserializer=ovpn__pb2.Name.FromString,
                )


class OVPNServicer(object):
    """The greeting service definition.
    """

    def list(self, request, context):
        """lists all clients
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_id(self, request, context):
        """get id of a client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_name(self, request, context):
        """get name of a client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OVPNServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'list': grpc.unary_unary_rpc_method_handler(
                    servicer.list,
                    request_deserializer=ovpn__pb2.Empty.FromString,
                    response_serializer=ovpn__pb2.ListResponse.SerializeToString,
            ),
            'get_id': grpc.unary_unary_rpc_method_handler(
                    servicer.get_id,
                    request_deserializer=ovpn__pb2.Name.FromString,
                    response_serializer=ovpn__pb2.ID.SerializeToString,
            ),
            'get_name': grpc.unary_unary_rpc_method_handler(
                    servicer.get_name,
                    request_deserializer=ovpn__pb2.ID.FromString,
                    response_serializer=ovpn__pb2.Name.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ovpn_package.OVPN', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OVPN(object):
    """The greeting service definition.
    """

    @staticmethod
    def list(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovpn_package.OVPN/list',
            ovpn__pb2.Empty.SerializeToString,
            ovpn__pb2.ListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovpn_package.OVPN/get_id',
            ovpn__pb2.Name.SerializeToString,
            ovpn__pb2.ID.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ovpn_package.OVPN/get_name',
            ovpn__pb2.ID.SerializeToString,
            ovpn__pb2.Name.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
