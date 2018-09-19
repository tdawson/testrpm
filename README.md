# testrpm
A set of rpm spec files that show how to do various rpm things

Currently, none of these spec files have any source, or files in them.  This allows them to be built without any setup.

## Setup
Download the git repo, and build each of the spec files.

- git clone https://github.com/tdawson/testrpm.git
- rpmbuild -ba testrpm/testrpm.1.0-1.spec
- rpmbuild -ba testrpm/testrpm.1.0-2.spec
- rpmbuild -ba testrpm/testrpm2.1.0-1.spec
- rpmbuild -ba testrpm/testrpm2.1.0-2.spec

## Usage
Install, and update the rpms, to see what order the scripts are run, and what their "counting" variable is.  Your path may vary from the example depending on your rpmbuild settings.

- sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/testrpm-1.0-1.noarch.rpm
- sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/testrpm2-1.0-1.noarch.rpm
- sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/testrpm-1.0-2.noarch.rpm
- sudo rpm -Uvh ~/rpmbuild/RPMS/noarch/testrpm2-1.0-1.noarch.rpm
- sudo rpm -e testrpm2
- sudo rpm -e testrpm
