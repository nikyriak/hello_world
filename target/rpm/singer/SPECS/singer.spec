%define __jar_repack 0
Name: singer
Version: 0.2.7
Release: SNAPSHOT20180623110251
Summary: singer
License: (c) null
Group: Development/Tools
autoprov: yes
autoreq: yes
Prefix: /usr/local
BuildArch: noarch
BuildRoot: /home/user9/demo_bin/target/rpm/singer/buildroot

%description

%install

if [ -d $RPM_BUILD_ROOT ];
then
  mv /home/user9/demo_bin/target/rpm/singer/tmp-buildroot/* $RPM_BUILD_ROOT
else
  mv /home/user9/demo_bin/target/rpm/singer/tmp-buildroot $RPM_BUILD_ROOT
fi

%files

%attr(755,root,root)  "/usr/local/singer/music/FileList.class"
%attr(755,root,root)  "/usr/local/singer/music/Singer.class"
%attr(755,root,root)  "/usr/local/singer/list.txt"
%attr(755,root,root)  "/usr/local/singer/music/music/FileList.class"
%attr(755,root,root)  "/usr/local/singer/music/music/Singer.class"
%attr(755,root,root)  "/usr/local/singer/music/list.txt"

%pre
echo "installing singer now"
