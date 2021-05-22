#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Coro
Version  : 6.57
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Coro-6.57.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Coro-6.57.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl BSD-2-Clause GPL-2.0
Requires: perl-Coro-license = %{version}-%{release}
Requires: perl-Coro-perl = %{version}-%{release}
Requires: perl(AnyEvent)
Requires: perl(AnyEvent::AIO)
Requires: perl(AnyEvent::BDB)
Requires: perl(AnyEvent::Util)
Requires: perl(BDB)
Requires: perl(Canary::Stability)
Requires: perl(EV)
Requires: perl(Event)
Requires: perl(Guard)
Requires: perl(Scalar::Util)
Requires: perl(Storable)
Requires: perl(common::sense)
BuildRequires : buildreq-cpan
BuildRequires : perl(AnyEvent)
BuildRequires : perl(Canary::Stability)
BuildRequires : perl(EV)
BuildRequires : perl(Event)
BuildRequires : perl(Guard)
BuildRequires : perl(common::sense)

%description
NAME
Coro - the only real threads in perl
SYNOPSIS
use Coro;

async {
# some asynchronous thread of execution
print "2\n";
cede; # yield back to main
print "4\n";
};
print "1\n";
cede; # yield to coro
print "3\n";
cede; # and again

# use locking
my $lock = new Coro::Semaphore;
my $locked;

$lock->down;
$locked = 1;
$lock->up;

%package dev
Summary: dev components for the perl-Coro package.
Group: Development
Provides: perl-Coro-devel = %{version}-%{release}
Requires: perl-Coro = %{version}-%{release}

%description dev
dev components for the perl-Coro package.


%package license
Summary: license components for the perl-Coro package.
Group: Default

%description license
license components for the perl-Coro package.


%package perl
Summary: perl components for the perl-Coro package.
Group: Default
Requires: perl-Coro = %{version}-%{release}

%description perl
perl components for the perl-Coro package.


%prep
%setup -q -n Coro-6.57
cd %{_builddir}/Coro-6.57

%build
## build_prepend content
# Get rid of #!/opt/bin/perl

find . -type f -exec sed -s -i '1s|^#!/opt/bin/perl|#!/usr/bin/perl|' {} +

# Avoid being prompted by ExtUtils::MakeMaker or Canary::Stability
export PERL_MM_USE_DEFAULT=1
export PERL_CANARY_STABILITY_NOPROMPT=1
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Coro
cp %{_builddir}/Coro-6.57/Coro/libcoro/LICENSE %{buildroot}/usr/share/package-licenses/perl-Coro/40a2be7ced057c47d12a095fb029d4c19c790f5b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Coro.3
/usr/share/man/man3/Coro::AIO.3
/usr/share/man/man3/Coro::AnyEvent.3
/usr/share/man/man3/Coro::BDB.3
/usr/share/man/man3/Coro::Channel.3
/usr/share/man/man3/Coro::Debug.3
/usr/share/man/man3/Coro::EV.3
/usr/share/man/man3/Coro::Event.3
/usr/share/man/man3/Coro::Handle.3
/usr/share/man/man3/Coro::Intro.3
/usr/share/man/man3/Coro::LWP.3
/usr/share/man/man3/Coro::MakeMaker.3
/usr/share/man/man3/Coro::RWLock.3
/usr/share/man/man3/Coro::Select.3
/usr/share/man/man3/Coro::Semaphore.3
/usr/share/man/man3/Coro::SemaphoreSet.3
/usr/share/man/man3/Coro::Signal.3
/usr/share/man/man3/Coro::Socket.3
/usr/share/man/man3/Coro::Specific.3
/usr/share/man/man3/Coro::State.3
/usr/share/man/man3/Coro::Storable.3
/usr/share/man/man3/Coro::Timer.3
/usr/share/man/man3/Coro::Util.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Coro/40a2be7ced057c47d12a095fb029d4c19c790f5b

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/AIO.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/AnyEvent.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/BDB.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Channel.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/CoroAPI.h
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Debug.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/EV.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Event.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Handle.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Intro.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/LWP.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/MakeMaker.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/RWLock.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Select.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Semaphore.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/SemaphoreSet.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Signal.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Socket.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Specific.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/State.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Storable.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Timer.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/jit-amd64-unix.pl
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Coro/jit-x86-unix.pl
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Coro/EV/EV.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Coro/Event/Event.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Coro/State/State.so
