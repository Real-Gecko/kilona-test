from concurrent import futures

import grpc
import pytest
from sqlalchemy import func, select

from db import session
from db.models import GeneratedNumbers
from randomizer import randomizer_pb2, randomizer_pb2_grpc
from server import RandomizerServicer


@pytest.fixture(scope="function")
def stub():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    randomizer_pb2_grpc.add_RandomizerServicer_to_server(RandomizerServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()

    try:
        with grpc.insecure_channel("localhost:50051") as channel:
            yield randomizer_pb2_grpc.RandomizerStub(channel)
    finally:
        server.stop(None)


def test_request(stub):
    statement = select(func.count()).select_from(GeneratedNumbers)
    old_count: int = session.execute(statement).scalar()
    request: randomizer_pb2.Request = randomizer_pb2.AddRequest()
    response: randomizer_pb2.Response = stub.RandomNumber(request)
    new_count: int = session.execute(statement).scalar()

    assert isinstance(response.result, float)
    assert new_count == old_count + 1
