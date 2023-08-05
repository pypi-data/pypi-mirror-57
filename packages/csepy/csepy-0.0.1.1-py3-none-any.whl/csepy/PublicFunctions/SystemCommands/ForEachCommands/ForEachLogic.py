#!/usr/bin/python3
import itertools
import re
from csepy.System.FileSystem.FileSystem import ReadFile, ReadOnlineFile
from csepy.System.Randomizer.Randomizer import GetRandomString

from csepy.System.Regex import subRegex, httpRegex


class ForEachLogic:
    def GetNewCommands(self, commands):
        swapDictionary = {}
        newParamList = []
        for param in commands:
            done = False
            while not done:
                done = True
                regMatch = subRegex.search(param)
                if regMatch:
                    param = self.GetNewParam(param, regMatch, swapDictionary, self.GetRegexFunctionType(regMatch.group(1)))
                    done = False

            newParamList.append(param)
        return self.GetCommandsFromSwapDictionary(" ".join(newParamList), swapDictionary)

    def GetNewParam(self, param, regexResult, swapDictionary, getListFunction):
        randomString = GetRandomString(32)
        path = regexResult.group(1)
        param = re.sub(subRegex, randomString, param, 1)
        parsedList = getListFunction(path)
        swapDictionary[randomString] = parsedList
        return param

    def GetRegexFunctionType(self, path):
        if httpRegex.match(path):
            return self.GetListFromUrl
        if "," in path:
            return self.GetListFromString
        return self.GetListFromPath

    def GetListFromPath(self, path):
        fileContent = ReadFile(path)
        if not fileContent:
            return []
        parsedList = list(itertools.chain.from_iterable([x.split(",") if x else "" for x in fileContent]))
        return parsedList

    def GetListFromUrl(self, path):
        fileContent = ReadOnlineFile(path)
        if not fileContent:
            return []
        parsedList = list(itertools.chain.from_iterable([x.split(",") if x else "" for x in fileContent]))
        return parsedList

    def GetListFromString(self, string):
        return string.split(",")

    def GetCommandsFromSwapDictionary(self, command, swapDictionary):
        valuesList = list(swapDictionary.values())
        keysList = list(swapDictionary.keys())
        allOptions = itertools.product(*valuesList)
        paramCount = len(keysList)
        results = []
        for option in allOptions:
            newCommand = command
            for i in range(paramCount):
                newCommand = newCommand.replace(keysList[i], option[i])
            results.append(newCommand)
        return results
