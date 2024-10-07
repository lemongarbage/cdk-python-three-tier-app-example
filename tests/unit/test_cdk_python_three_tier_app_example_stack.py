import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_python_three_tier_app_example.cdk_python_three_tier_app_example_stack import CdkPythonThreeTierAppExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_python_three_tier_app_example/cdk_python_three_tier_app_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkPythonThreeTierAppExampleStack(app, "cdk-python-three-tier-app-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
