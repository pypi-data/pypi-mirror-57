#!/usr/bin/python3
from csepy.System.Logger.Logger import Logger


def GetLogger(config, osType):
    return Logger(config, osType)
