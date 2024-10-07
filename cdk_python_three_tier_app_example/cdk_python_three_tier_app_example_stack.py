from aws_cdk import (
    Stack,
    StackProps,
    RemovalPolicy,
    aws_dynamodb as _ddb
)


from constructs import Construct

class CdkPythonThreeTierAppExampleStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create the DDB table
        table = _ddb.Table(self, 'NotesTable',
            billing_mode=_ddb.BillingMode.PAY_PER_REQUEST,
            partition_key=_ddb.Attribute(
                name="pk",
                type=_ddb.AttributeType.STRING
            ),
            removal_policy=RemovalPolicy.DESTROY,
            sort_key=_ddb.Attribute(
                name="sk",
                type=_ddb.AttributeType.STRING
            ),
            table_name="NotesTable"       
            )