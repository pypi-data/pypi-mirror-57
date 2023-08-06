#  MIT License
# 
#  Copyright (c) 2019 Jac. Beekers
# 
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# 

##
# Process deploy list for Scheduler artifacts
# @Since: 25-OCT-2019
# @Author: Jac. Beekers
# @Version: 20191025.0 - JBE - Initial

import supporting.errorcodes as err
import supporting, logging
import os
from cicd.scheduler import schedulerConstants as constants
from cicd.scheduler import schedulerSettings as settings
import supporting.deploylist
from pathlib import Path
from cicd.scheduler.schedulerArtifactChecks import checkSchedulerEntryType
from supporting.generatezip import generate_zip
from pygit2 import clone_repository

logger = logging.getLogger(__name__)
entrynr = 0
level = 0


def processGitBranch(git_repository, git_branch, path):
    thisproc = "processGitBranch"
    repo = clone_repository(git_repository, "schedulergit", bare=False, checkout_branch=git_branch)
    # TODO: Collect the schedules
    latestError = err.OK
    return latestError


def processList(deployFile):
    thisproc = "processList"
    latestError = err.OK
    result, deployItems = supporting.deploylist.getWorkitemList(deployFile)
    if result.rc == 0:
        for deployEntry in supporting.deploylist.deployItems:
            supporting.log(logger, logging.DEBUG, thisproc, "Found deploy entry >" + deployEntry + "<.")
            result = processEntry(deployEntry)
            supporting.log(logger, logging.DEBUG, thisproc, "deployEntry returned >" + result.code + "<.")
            supporting.log(logger, logging.DEBUG, thisproc, "Overall result is >" + latestError.code + "<.")
            if result.rc != 0:
                latestError = result
    else:
        latestError = result
    return latestError


def processEntry(deployEntry):
    thisproc = "processEntry"
    result = err.OK
    supporting.log(logger, logging.DEBUG, thisproc, "Current directory is >" + os.getcwd() + "<.")
    supporting.log(logger, logging.DEBUG, thisproc, "Started to work on deploy entry >" + deployEntry + "<.")

    type, directory, filter = deployEntry.split(':', 3)
    supporting.log(logger, logging.DEBUG, thisproc,
                   'Type is >' + type + '<, directory is >' + directory + '< and filter is >' + filter + '<')

    result = checkSchedulerEntryType(type)
    if result.rc != 0:
        return result

    zipfilename = determinebaseTargetDirectory(type) + "/" + directory.replace('/', '_') + ".zip"
    os.makedirs(determinebaseTargetDirectory(type), exist_ok=True)
    supporting.log(logger, logging.DEBUG, thisproc, 'zipfilename set to >' + zipfilename + "<.")

    source_dir, result = determineSourceDirectory(directory, type)
    if result.rc != 0:
        supporting.log(logger, logging.DEBUG, thisproc,
                       'source directory could not be determined. directory is >' + directory + "< and type was set to >" + type + "<.")
        return result

    result = generate_zip(determinebaseSourceDirectory(type), source_dir, zipfilename, filter)

    supporting.log(logger, logging.DEBUG, thisproc,
                   "Completed with rc >" + str(result.rc) + "< and code >" + result.code + "<.")

    return result


def determinebaseSourceDirectory(type):
    if type == constants.DAGS or type == constants.JOBASCODE:
        return settings.sourceschedulerdir
    if type == constants.PLUGINS or type == constants.JOBTYPE:
        return settings.sourceschedulertypedir

    return constants.NOT_SET


def determinebaseTargetDirectory(type):
    if type == constants.DAGS or type == constants.JOBASCODE:
        return settings.targetschedulerdir
    if type == constants.PLUGINS or type == constants.JOBTYPE:
        return settings.targetschedulertypedir

    return constants.NOT_SET


def determineSourceDirectory(directory, type):
    thisproc = "determineSourceDirectory"

    # type_path = directory + "/" + type
    type_path = directory
    directoryPath = Path(type_path)
    if directoryPath.is_dir():
        supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + type_path + "<.")
        directory = type_path
    else:
        sourceDir = determinebaseSourceDirectory(type) + "/"
        supporting.log(logger, logging.DEBUG, thisproc, 'directory >' + type_path + '< not found. Trying >'
                       + sourceDir + type_path + '<...')
        type_path = sourceDir + type_path
        directoryPath = Path(type_path)
        if directoryPath.is_dir():
            supporting.log(logger, logging.DEBUG, thisproc, 'Found directory >' + type_path + "<.")
        else:
            supporting.log(logger, err.SQLFILE_NF.level, thisproc,
                           "directory checked >" + type_path + "<. " + err.DIRECTORY_NF.message)
            result = err.DIRECTORY_NF
            return constants.NOT_SET, result

    return type_path, err.OK
