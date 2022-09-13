#!/usr/bin/env python3

from aws_cdk import core

from cipipe-core.cipipe_core_stack import ApplicationStack


app = core.App()
ApplicationStack(app, "cipipe-core-stack")

app.synth()
