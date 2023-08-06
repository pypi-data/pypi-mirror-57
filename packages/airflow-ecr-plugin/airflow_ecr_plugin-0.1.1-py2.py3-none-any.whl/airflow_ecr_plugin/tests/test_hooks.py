import moto
import pytest

from airflow.models import connection
from airflow.utils import db
from aws_ecr_plugin import hooks


class TestAwsEcrHook(object):
    @pytest.fixture
    def aws_connection(self):
        db.upgradedb()
        # with db.create_session() as session:
        #     aws_connection = connection.Connection(
        #         conn_id="aws_default",
        #         conn_type="aws",
        #         login="aws",
        #         password="password",
        #     )
        # session.add(aws_connection)

    def test_create_hook(self, aws_connection):
        ecr_hook = hooks.AwsEcrHook(region_name="us-east-1")
        print(ecr_hook)

    @moto.mock_ecr
    def test_get_auth_data_default_registry(self):
        ecr_hook = hooks.AwsEcrHook(region_name="us-east-2")
        auth_data = ecr_hook.get_auth_data()

        assert auth_data
        print auth_data._asdict()
        print auth_data.username
        print auth_data.password
