Summary: A test install rpm to test rpm installing
Name: testrpm
Version: 1.0
Release: 2
License: GPL v2.0
URL: https://github.com/tdawson/testrpm
BuildArch: noarch

%description
This is just to test how rpm's install

%pre
echo "%name-%version-%release : PRE : \$1=$1"

%post
echo "%name-%version-%release : POST : \$1=$1"

%preun
echo "%name-%version-%release : PREUN : \$1=$1"
if [ "$1" -eq 0 ] ; then
  echo "  We are the last rpm, we should really run our script"
fi
if [ "$1" -ge 1 ] ; then
  echo "  We are not the last rpm, run our script with care"
fi

%postun
echo "%name-%version-%release : POSTUN : \$1=$1"
if [ "$1" -eq 0 ] ; then
  echo "  We are the last rpm, we should really run our script"
fi
if [ "$1" -ge 1 ] ; then
  echo "  We are not the last rpm, run our script with care"
fi

%pretrans
echo "%name-%version-%release : PRETRANS : \$1=$1"

%posttrans
echo "%name-%version-%release : POSTTRANS : \$1=$1"

%triggerin -- testrpm2
echo "%name-%version-%release : TRIGGERIN : testrpm2 : \$1=$1  \$2=$2"

%triggerun -- testrpm2
echo "%name-%version-%release : TRIGGERUN : testrpm2 : \$1=$1  \$2=$2"

%triggerpostun -- testrpm2
echo "%name-%version-%release : TRIGGERPOSTUN : testrpm2 : \$1=$1  \$2=$2"

%files

%changelog
* Wed Sep 19 2018 Troy Dawson <tdawson@redhat.com> 1.0-2
- Bump release version so we can upgrade our packages
* Wed Sep 19 2018 Troy Dawson <tdawson@redhat.com> 1.0-1
- Initial checking
