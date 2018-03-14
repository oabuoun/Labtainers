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

import os
import sys
import re
import AddPkgLogging
import ParsePackages

TMPDIR="/tmp/.addpkgdir"
UBUNTUHOME="/var/www/html/ubuntumirror.uc.nps.edu/ubuntu"
DISTHOME="%s/dists" % UBUNTUHOME
POOLHOME="%s/pool" % UBUNTUHOME
URLPATH="http://us.archive.ubuntu.com/ubuntu"

# Dictionary of packages
pkgsdict = {}

LIST=[
      "xenial/main/binary-amd64/Packages",
      "xenial/restricted/binary-amd64/Packages",
      "xenial/universe/binary-amd64/Packages",
      "xenial/multiverse/binary-amd64/Packages",
      "xenial-updates/main/binary-amd64/Packages",
      "xenial-updates/restricted/binary-amd64/Packages",
      "xenial-updates/universe/binary-amd64/Packages",
      "xenial-updates/multiverse/binary-amd64/Packages"
     ]

def process_filename_list(finalflist):
    os.chdir(TMPDIR)
    for fname in finalflist:
        localfname = "%s/%s" % (UBUNTUHOME, fname)
        if os.path.exists(localfname):
            # skip if already exists
            continue
        else:
            remotefname = "%s/%s" % (URLPATH, fname)
            os.system("wget %s" % remotefname)
            basefname = os.path.basename(localfname)
            dirname = os.path.dirname(localfname)
            os.system("mkdir -p %s" % dirname)
            os.system("cp %s %s" % (basefname, localfname))
    os.system("chown -R apache:apache %s" % POOLHOME)

def collect_dependencies_filenames(packages, pkgname, deplist, finaldeplist, finalflist, logger):
    for dependency in deplist:
        if "|" in dependency:
            dependency = dependency.split('|')[0]
        if "(" in dependency:
            dependency = dependency.split('(')[0]
        dependency = dependency.strip()
        if dependency not in finaldeplist:
            finaldeplist.append(dependency)
            # Recursive here
            # Get the corresponding package first
            found = False
            packagefile = ""
            for listname in LIST:
                packagefile = "%s/%s" % (DISTHOME,listname)
                pkginfo = pkgsdict[listname]
                packages = pkginfo.GetPackages()
                for name in packages:
                    if name == dependency:
                        #logger.INFO("package file is %s" % packagefile)
                        #logger.INFO("package filename is %s" % packages[name].fname)
                        #logger.INFO("package dependencies is %s" % str(packages[name].deplist))
                        finalflist.append(packages[name].fname)
                        found = True
                        break
                if found:
                    break
            if not found:
                logger.WARNING("Package (%s) not found" % dependency)
            else:
                finaldeplist, finalflist = collect_dependencies_filenames(packages, dependency, packages[dependency].deplist, finaldeplist, finalflist, logger)
    return finaldeplist, finalflist

def main():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage: AddPackage.py <packagename>\n")
        sys.exit(1)

    if os.geteuid() != 0:
        sys.stderr.write("This script requires root privileges\n")
        sys.exit(1)

    # Remove and re-create TMPDIR
    os.system("rm -rf %s" % TMPDIR)
    os.system("mkdir %s" % TMPDIR)

    packagename = sys.argv[1]
    ParsePackages.logger = AddPkgLogging.AddPkgLogging("addpackage.log")
    ParsePackages.logger.INFO("AddPackage - package name is (%s)" % packagename)
    #ParsePackages.logger.INFO("packagename is (%s)" % packagename)
    #ParsePackages.logger.INFO("UBUNTUHOME is (%s)" % UBUNTUHOME)
    #ParsePackages.logger.INFO("DISTHOME is (%s)" % DISTHOME)

    # Pre-parse all "Packages" file
    for listname in LIST:
        packagefile = "%s/%s" % (DISTHOME,listname)
        pkginfo = ParsePackages.ParsePackages(packagefile)
        pkgsdict[listname] = pkginfo

    found = False
    packagefile = ""
    for listname in LIST:
        packagefile = "%s/%s" % (DISTHOME,listname)
        pkginfo = pkgsdict[listname]
        packages = pkginfo.GetPackages()
        for name in packages:
            if name == packagename:
                #ParsePackages.logger.INFO("package filename is %s" % packages[name].fname)
                #ParsePackages.logger.INFO("package dependencies is %s" % str(packages[name].deplist))
                found = True
                break
        if found:
            break
    finalflist = []
    finaldeplist = []
    if found:
        #ParsePackages.logger.INFO("found the package (%s) in (%s)" % (packagename, packagefile))
        finalflist.append(packages[name].fname)
        finaldeplist, finalflist = collect_dependencies_filenames(packages, packagename, packages[name].deplist, finaldeplist, finalflist, ParsePackages.logger)
        ParsePackages.logger.INFO("final dependencies list is (%s)" % finaldeplist)
        ParsePackages.logger.INFO("final filename list is (%s)" % finalflist)
    else:
        ParsePackages.logger.ERROR("Package (%s) is not found in xenial or xenial-updates" % packagename)

    process_filename_list(finalflist)

if __name__ == '__main__':
    sys.exit(main())
