#!/usr/bin/env python3

from aws_cdk import core

from demo1.demo1_stack import Demo1Stack


app = core.App()
Demo1Stack(app, "demo1")

app.synth()
