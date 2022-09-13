from aws_cdk import (
    App,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as _apigw
)


class ApplicationStack(Stack):

    def __init__(self, scope: App, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # The "Simple lambda" is a lambda that does not need any additional
        # third-party modules installed.  The code asset is the directory of
        # your lambda function
        simple_lambda = _lambda.Function(self,'SimpleLambda',
            handler='lambda-handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('simple-lambda'),
        )

        # The "Complex" lambda is one the required the installation of third-party
        # modules.  The pipeline will create a zip-file in the directory that contains
        # your code and the third party modules (pip3 install -r requirements.txt -t .)
        complex_lambda = _lambda.Function(self,'ComplexLambda',
            handler='lambda-handler.handler',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('complex-lambda/complex-lambda.zip'),
        )

        # the name of the handler, needs to match the name of the Go-Binary
        go_lambda = _lambda.Function(self,'GoLambda',
            handler='go-lambda',
            runtime=_lambda.Runtime.GO_1_X,
            code=_lambda.Code.from_asset('go-lambda'),
        )
        
        api = _apigw.RestApi(self, 'sample-api')
        simple_resource = api.root.add_resource('simple')
        simple_resource.add_method('GET', _apigw.LambdaIntegration(simple_lambda))

        complex_resource = api.root.add_resource('complex')
        complex_resource.add_method('GET', _apigw.LambdaIntegration(complex_lambda))

        go_resource = api.root.add_resource('go')
        go_resource.add_method('GET', _apigw.LambdaIntegration(go_lambda))
