import logging
from concurrent import futures

import grpc

from couchers import config
from couchers.interceptors import ErrorSanitizationInterceptor, LoggingInterceptor
from couchers.servicers.account import Account
from couchers.servicers.api import API
from couchers.servicers.auth import Auth
from couchers.servicers.bugs import Bugs
from couchers.servicers.conversations import Conversations
from couchers.servicers.gis import GIS
from couchers.servicers.jail import Jail
from couchers.servicers.media import Media, get_media_auth_interceptor
from couchers.servicers.requests import Requests
from couchers.servicers.sso import SSO
from pb import (
    account_pb2_grpc,
    api_pb2_grpc,
    auth_pb2_grpc,
    bugs_pb2_grpc,
    conversations_pb2_grpc,
    gis_pb2_grpc,
    jail_pb2_grpc,
    media_pb2_grpc,
    requests_pb2_grpc,
    sso_pb2_grpc,
)

logger = logging.getLogger(__name__)


def run_foreground():
    auth = Auth()
    open_server = grpc.server(
        futures.ThreadPoolExecutor(2), interceptors=[ErrorSanitizationInterceptor(), LoggingInterceptor()]
    )
    open_server.add_insecure_port("[::]:1752")
    auth_pb2_grpc.add_AuthServicer_to_server(auth, open_server)
    bugs_pb2_grpc.add_BugsServicer_to_server(Bugs(), open_server)
    open_server.start()

    jailed_server = grpc.server(
        futures.ThreadPoolExecutor(2),
        interceptors=[
            ErrorSanitizationInterceptor(),
            LoggingInterceptor(),
            auth.get_auth_interceptor(allow_jailed=True),
        ],
    )
    jailed_server.add_insecure_port("[::]:1754")
    jail_pb2_grpc.add_JailServicer_to_server(Jail(), jailed_server)
    jailed_server.start()

    servicer = API()
    server = grpc.server(
        futures.ThreadPoolExecutor(2),
        interceptors=[
            ErrorSanitizationInterceptor(),
            LoggingInterceptor(),
            auth.get_auth_interceptor(allow_jailed=False),
        ],
    )
    server.add_insecure_port("[::]:1751")

    account_pb2_grpc.add_AccountServicer_to_server(Account(), server)
    api_pb2_grpc.add_APIServicer_to_server(servicer, server)
    conversations_pb2_grpc.add_ConversationsServicer_to_server(Conversations(), server)
    gis_pb2_grpc.add_GISServicer_to_server(GIS(), server)
    requests_pb2_grpc.add_RequestsServicer_to_server(Requests(), server)
    sso_pb2_grpc.add_SSOServicer_to_server(SSO(), server)

    server.start()

    media_server = grpc.server(
        futures.ThreadPoolExecutor(2),
        interceptors=[LoggingInterceptor(), get_media_auth_interceptor(config.config["MEDIA_SERVER_BEARER_TOKEN"])],
    )
    media_server.add_insecure_port("[::]:1753")
    media_pb2_grpc.add_MediaServicer_to_server(Media(), media_server)
    media_server.start()

    logger.info(f"Serving on 1751 (secure), 1752 (auth), 1753 (media), and 1754 (jailed)")

    fg = (server, jailed_server, open_server, media_server)
    return fg
