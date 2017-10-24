#!/usr/bin/env python
'''
This software was created by United States Government employees at 
The Center for the Information Systems Studies and Research (CISR) 
at the Naval Postgraduate School NPS.  Please note that within the 
United States, copyright protection is not available for any works 
created  by United States Government employees, pursuant to Title 17 
United States Code Section 105.   This software is in the public 
domain and is not subject to copyright. 
'''

# Filename: validate.py
# Description:
# This is the validate script to be run by the instructor.
# Note:
# 1. It needs 'start.config' file, where
#    <labname> is given as a parameter to the script.
#

import getpass
import glob
import json
import md5
import os
import sys
import shutil

instructor_cwd = os.getcwd()
instructor_bin = os.path.join(instructor_cwd, 'bin')
student_cwd = instructor_cwd.replace('labtainer-instructor', 'labtainer-student')
student_bin = os.path.join(student_cwd, 'bin')
# Append Student CWD to sys.path
sys.path.append(student_cwd)
sys.path.append(student_bin)
sys.path.append(instructor_bin)

import evalExpress
import labutils
import logging
import GoalsParser
import LabtainerLogging
import ParseStartConfig
import ParameterParser
import ResultParser

# TEMPORARY PATH - to copy 'config' and 'instr_config' to validate
TEMPDIR="/tmp/vallabtainers"

executefilelist = []

boolean_tokens = ['(',')','and_not', 'AND_NOT', 'or_not', 'OR_NOT', 'not','NOT','and','AND','or','OR','True','False']


def validate_parameter_result(parameter_list, resultidlist, goals, inputtag):
    validate_ok = True
    use_target = ""
    if "." in inputtag:
        (use_target, inputtagstring) = inputtag.split('.')
    if use_target == "":
        use_target = "result"
        inputtagstring = inputtag
    if use_target == "parameter" or use_target == "parameter_ascii":
        if inputtagstring not in parameter_list:
            validate_ok = False
    elif use_target == "result":
        if inputtagstring not in resultidlist:
            # handle expression here
            if inputtagstring.startswith('(') and inputtagstring.endswith(')'):
                express = inputtagstring[inputtagstring.find("(")+1:inputtagstring.find(")")]
                for tag in resultidlist:
                    labutils.logger.DEBUG('is tag %s in express %s' % (tag, express))
                    if tag in express:
                        # Replace each occurence of tag with 2
                        express = express.replace(tag, "2")
                try:
                    labutils.logger.DEBUG('try eval of <%s>' % express)
                    result = evalExpress.eval_expr(express)
                except:
                    labutils.logger.ERROR('could not evaluation %s, which became %s' % (inputtagstring, express))
                    validate_ok = False
            else:
                labutils.logger.ERROR('ERROR: expected expression in parens' % inputtagstring)
                validate_ok = False
    else:
        validate_ok = False
    return validate_ok

def check_count(parameter_list, resultidlist, goals, jsongoalid, jsonresulttag):
    found_error = False
    # Make sure the resulttag is valid - no special case for resulttag
    validate_resulttag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonresulttag)
    if not validate_resulttag_ok:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid resulttag (%s)" % (jsongoalid, jsonresulttag))

    if not validate_resulttag_ok:
        found_error = True
    return found_error

def check_countgreater(parameter_list, resultidlist, goals, jsongoalid, jsonanswertag, boolean_string):
    found_error = False
    try:
        value = int(jsonanswertag)
    except:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid int (%s)" % (jsongoalid, jsonanswertag))
    # boolean_string must start with '(' and end with ')'
    # and contains comma separated goals
    validate_ok = True
    if boolean_string.startswith('(') and boolean_string.endswith(')'):
        express = boolean_string[boolean_string.find("(")+1:boolean_string.find(")")]
        for tag in express.split(','):
            goaltag = tag.strip()
            # goaltag must be in goals otherwise it is an error
            found_goaltag_in_goals = False
            for eachgoal in goals:
                if goaltag == eachgoal['goalid']:
                    found_goaltag_in_goals = True
                    break
            if found_goaltag_in_goals:
                continue
            else:
                labutils.logger.ERROR('invalid goal %s in %s' % (goaltag, boolean_string))
                validate_ok = False
                break
    else:
        labutils.logger.ERROR('ERROR: expected goals %s in parens' % boolean_string)
        validate_ok = False
    if not validate_ok:
        found_error = True
    return found_error

def check_temporal(parameter_list, resultidlist, goals, jsongoalid, goal1tag, goal2tag):
    found_error = False
    goal1tag_ok = True
    goal2tag_ok = True
    if goal1tag not in goals:
        goal1tag_ok = False
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid goal1tag (%s)" % (jsongoalid, goal1tag))
    if goal2tag not in goals:
        goal2tag_ok = False
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid goal2tag (%s)" % (jsongoalid, goal2tag))
    if not (goal1tag_ok and goal2tag_ok):
        found_error = True
    return found_error

def check_boolean(parameter_list, resultidlist, goals, jsongoalid, boolean_string):
    found_error = False
    # Make it easier to tokenize later
    boolean_string = boolean_string.replace('(', ' ( ')
    boolean_string = boolean_string.replace(')', ' ) ').strip()
    # boolean_string must start with '(' and end with ')'
    # must be token separated goals
    validate_ok = True
    if boolean_string.startswith('(') and boolean_string.endswith(')'):
        for tag in boolean_string.split():
            goaltag = tag.strip()
            # if goaltag is valid boolean operator, skip
            if goaltag in boolean_tokens:
                continue
            # goaltag must be in goals otherwise it is an error
            found_goaltag_in_goals = False
            for eachgoal in goals:
                if goaltag == eachgoal['goalid']:
                    found_goaltag_in_goals = True
                    break
            if found_goaltag_in_goals:
                continue
            else:
                labutils.logger.ERROR('invalid goal %s in %s' % (goaltag, boolean_string))
                validate_ok = False
                break
    else:
        labutils.logger.ERROR('ERROR: expected goals %s in parens' % boolean_string)
        validate_ok = False
    if not validate_ok:
        found_error = True

def check_execute(parameter_list, resultidlist, goals, jsongoalid, executefilepath, jsonanswertag, jsonresulttag):
    found_error = False
    executefile = os.path.basename(executefilepath)
    if executefile not in executefilelist:
        executefile_ok = False

    # Make sure the answertag is valid - not expecting special case 'answer=<string>'
    validate_answertag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonanswertag)
    if not validate_answertag_ok:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid answertag (%s)" % (jsongoalid, jsonanswertag))

    # Make sure the resulttag is valid - no special case for resulttag
    validate_resulttag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonresulttag)
    if not validate_resulttag_ok:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid resulttag (%s)" % (jsongoalid, jsonresulttag))

    if not (execute_file_ok and validate_answertag_ok and validate_resulttag_ok):
        found_error = True
       
    return found_error

def check_matches(parameter_list, resultidlist, goals, jsongoalid, jsonanswertag, jsonresulttag):
    found_error = False
    validate_answertag_ok = True
    # Make sure the answertag is valid
    # Handle special case 'answer=<string>'
    if '=' in jsonanswertag:
        # skip it
        validate_answertag_ok = True
    else:
        validate_answertag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonanswertag)
    if not validate_answertag_ok:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid answertag (%s)" % (jsongoalid, jsonanswertag))

    validate_resulttag_ok = True
    # Make sure the resulttag is valid - no special case for resulttag
    validate_resulttag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonresulttag)
    if not validate_resulttag_ok:
        labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid resulttag (%s)" % (jsongoalid, jsonresulttag))

    if not (validate_answertag_ok and validate_resulttag_ok):
        found_error = True

    return found_error

def validate_goals(parameter_list, resultidlist, goals):
    #labutils.logger.DEBUG("Result ID list is ")
    #labutils.logger.DEBUG(resultidlist)
    #labutils.logger.DEBUG("Parameter list is ")
    #labutils.logger.DEBUG(parameter_list)
    #labutils.logger.DEBUG("Goals list is ")
    #labutils.logger.DEBUG(goals)
    for eachgoal in goals:
        #labutils.logger.DEBUG("Current goal is ")
        #labutils.logger.DEBUG(eachgoal)
        #labutils.logger.DEBUG("    goalid is (%s)" % eachgoal['goalid'])
        #labutils.logger.DEBUG("    goaltype is (%s)" % eachgoal['goaltype'])
        #labutils.logger.DEBUG("    answertag is (%s)" % eachgoal['answertag'])
        #labutils.logger.DEBUG("    resulttag is (%s)" % eachgoal['resulttag'])
        jsongoalid = eachgoal['goalid']
        jsongoaltype = eachgoal['goaltype']

        found_error = False
        if (jsongoaltype == "matchany" or
            jsongoaltype == "matchlast" or
            jsongoaltype  == "matchacross"):
            jsonanswertag = eachgoal['answertag']
            jsonresulttag = eachgoal['resulttag']
            found_error = check_matches(parameter_list, resultidlist, goals, jsongoalid, jsonanswertag, jsonresulttag)
        elif jsongoaltype == "execute":
            executefilepath = eachgoal['goaloperator']
            jsonanswertag = eachgoal['answertag']
            jsonresulttag = eachgoal['resulttag']
            found_error = check_execute(parameter_list, resultidlist, goals, jsongoalid, executefilepath, jsonanswertag, jsonresulttag)
        elif jsongoaltype == "boolean":
            boolean_string = eachgoal['boolean_string']
            found_error = check_boolean(parameter_list, resultidlist, goals, jsongoalid, boolean_string)
        elif jsongoaltype == "time_before" or jsongoaltype == "time_during":
            goal1tag = eachgoal['goal1tag']
            goal2tag = eachgoal['goal2tag']
            found_error = check_temporal(parameter_list, resultidlist, goals, jsongoalid, goal1tag, goal2tag)
        elif jsongoaltype == "count_greater":
            boolean_string = eachgoal['boolean_string']
            jsonanswertag = eachgoal['answertag']
            found_error = check_countgreater(parameter_list, resultidlist, goals, jsongoalid, jsonanswertag, boolean_string)
        elif jsongoaltype == "count" or jsongoaltype == "value":
            jsonresulttag = eachgoal['resulttag']
            found_error = check_count(parameter_list, resultidlist, goals, jsongoalid, jsonresulttag)
        elif jsongoaltype.startswith('is_'):
            jsonresulttag = eachgoal['resulttag']
            validate_resulttag_ok = validate_parameter_result(parameter_list, resultidlist, goals, jsonresulttag)
            if not validate_resulttag_ok:
                found_error = True
                labutils.logger.ERROR("ERROR: Goals goalid (%s) has invalid resulttag (%s)" % (jsongoalid, jsonresulttag))
        else:
            sys.stdout.write("Error: Invalid goal type!\n")
            sys.exit(1)

        # Found an error - break for loop
        if found_error:
            break


def setup_to_validate(lab_path, labname):
    # Create TEMPDIR - remove if it exists
    if os.path.exists(TEMPDIR):
        shutil.rmtree(TEMPDIR)
    TEMPLOCAL = os.path.join(TEMPDIR, ".local")
    os.makedirs(TEMPLOCAL)

    # Pick arbitrary e-mail
    user_email = "validate%s@dummy.org" % labname
    config_path       = os.path.join(lab_path,"config") 
    start_config_path = os.path.join(config_path,"start.config")
    start_config = ParseStartConfig.ParseStartConfig(start_config_path, labname, "instructor", labutils.logger)
   
    lab_master_seed = start_config.lab_master_seed
    # Create hash using LAB_MASTER_SEED concatenated with user's e-mail
    # LAB_MASTER_SEED is per laboratory - specified in start.config
    string_to_be_hashed = '%s:%s' % (lab_master_seed, user_email)
    mymd5 = md5.new()
    mymd5.update(string_to_be_hashed)
    lab_instance_seed = mymd5.hexdigest()
    labutils.logger.DEBUG("seed %s" % lab_instance_seed)

    # Create files
    LAB_SEEDFILE = os.path.join(TEMPLOCAL, ".seed")
    with open(LAB_SEEDFILE, "w") as fh:
        fh.write("%s\n" % lab_instance_seed)
    fh.close()
    USER_EMAILFILE = os.path.join(TEMPLOCAL, ".email")
    with open(USER_EMAILFILE, "w") as fh:
        fh.write("%s\n" % user_email)
    fh.close()
    LAB_NAMEFILE = os.path.join(TEMPLOCAL, ".labname")
    with open(LAB_NAMEFILE, "w") as fh:
        fh.write("%s\n" % labname)
    fh.close()
    WATERMARK_NAMEFILE = os.path.join(TEMPLOCAL, ".watermark")
    string_to_be_hashed = '%s:%s' % (lab_instance_seed, user_email)
    mymd5 = md5.new()
    mymd5.update(string_to_be_hashed)
    watermark = mymd5.hexdigest()
    labutils.logger.DEBUG("watermark %s" % watermark)
    with open(WATERMARK_NAMEFILE, "w") as fh:
        fh.write("%s\n" % watermark)
    fh.close()

    # Copy 'config' and 'instr_config' from LABPATH to TEMPLOCAL
    LAB_CONFIG = os.path.join(lab_path, "config")
    LAB_INSTRCONFIG = os.path.join(lab_path, "instr_config")
    TEMP_LAB_CONFIG = os.path.join(TEMPLOCAL, "config")
    TEMP_LAB_INSTRCONFIG = os.path.join(TEMPLOCAL, "instr_config")
    shutil.copytree(LAB_CONFIG, TEMP_LAB_CONFIG)
    shutil.copytree(LAB_INSTRCONFIG, TEMP_LAB_INSTRCONFIG)

    # Get a list of any executable in '_bin' directory
    # except fixlocal.sh, treataslocal, startup.sh
    binfilelist = glob.glob("%s/*/_bin/*" % TEMPLOCAL)
    for binfilepath in binfilelist:
        binfilename = os.path.basename(binfilepath)
        if not (binfilename == "fixlocal.sh" or 
                binfilename == "treataslocal" or
                binfilename == "startup.sh"):
            if binfilename not in executefilelist:
                executefilelist.append(binfilename)

    email_labname = "%s.%s" % (user_email.replace("@","_at_"), labname)

    return lab_instance_seed, start_config.grade_container, email_labname

# Usage: validate.py <labname>
# Arguments:
#    <labname> - the lab to validate
def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        sys.stderr.write("Usage: validate.py <labname> [-q]\n")
        sys.stderr.write("   -q will load the lab using a predetermined email.\n")
#	tell user list of lesson/folder names in "/labtainer/trunk/labs/"
	sys.stderr.write("List of available labs:\n\n")
	dir_path = os.path.dirname(os.path.realpath(__file__))
	dir_path = dir_path[:dir_path.index("scripts/labtainer-instructor")]	
	path = dir_path + "labs/"
	dirs = os.listdir(path)
	for loc in sorted(dirs):
                description = '  '+loc
		aboutFile = path + loc + "/config/about.txt"
		if(os.path.isfile(aboutFile)):
                    description += ' - '
		    with open(aboutFile) as fh:
		        for line in fh:
                            description += line
                else:
                    description += "\n"
                sys.stderr.write(description)
        sys.exit(1)
    labname = sys.argv[1]
    labutils.logger = LabtainerLogging.LabtainerLogging("labtainer.log", labname, "../../config/labtainer.config")
    labutils.logger.INFO("Begin logging validate.py for %s lab" % labname)
    labutils.logger.DEBUG("Instructor CWD = (%s), Student CWD = (%s)" % (instructor_cwd, student_cwd))
    lab_path = os.path.join(os.path.abspath('../../labs'), labname)
    labutils.is_valid_lab(lab_path)

    container_list = []
    lab_instance_seed, grade_container, email_labname = setup_to_validate(lab_path, labname)
    labutils.logger.DEBUG("grade_container %s" % grade_container)
    container_list.append(grade_container)
 
    LabDirName = os.path.join(TEMPDIR, email_labname)
    # Just validating - not actual parsing
    actual_parsing = False
    configfilelines, resultidlist = ResultParser.ParseValidateResultConfig(actual_parsing, TEMPDIR, LabDirName, container_list, labname, labutils.logger)

    parameter_list = GoalsParser.ParseGoals(TEMPDIR, TEMPDIR, labutils.logger)
    # GoalsParser created goals.json in parent directory
    parent_dir = os.path.dirname(TEMPDIR)
    goalsjsonfname = os.path.join(parent_dir, '.local','result','goals.json')
    goalsjson = open(goalsjsonfname, "r")
    goals = json.load(goalsjson)
    goalsjson.close()
    labutils.logger.DEBUG("Goals JSON config is")
    labutils.logger.DEBUG(goals)

    validate_goals(parameter_list, resultidlist, goals)
    return 0

if __name__ == '__main__':
    sys.exit(main())

