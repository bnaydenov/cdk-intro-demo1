from aws_cdk import core
import aws_cdk.aws_ec2 as ec2

class Demo1Stack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # ec2.CfnVPC(
        #     self, "MyVPC",
        #     cidr_block="10.0.0.0/16"
        # )
        ec2.Vpc(
            self,"MyVPC",
            cidr="10.0.0.0/16"
        )
