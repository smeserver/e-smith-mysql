Summary: e-smith specific mysql configuration and templates.
%define name e-smith-mysql
Name: %{name}
%define version 1.12.0
%define release 9
Version: %{version}
Release: %smerelease %{release}
Packager: %{_packager}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-mysql-1.12.0-setpassword.patch2
Patch1: e-smith-mysql-1.12.0-flushprivssemicolon.patch 
Patch2: e-smith-mysql-1.12.0-innodb-optional.patch
Patch3: e-smith-mysql-1.12.0-install_db.patch
Patch4: e-smith-mysql-1.12.0.disabled_pre_backup.patch
Patch5: e-smith-mysql-1.12.0.failed_restore.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: mysql-server
Requires: mysql
Requires: e-smith-base
Requires: e-smith-lib >= 1.15.1-19
AutoReqProv: no

%changelog
* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Nov  9 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-08
- Ensure that failed restore is detected during mysql.init. [SME: 1652]

* Mon Sep 25 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-07
- Fix pre-backup failure if mysqld is disabled in config db. [SME: 1937]

* Tue Jun 27 2006 Filippo Carletti <carletti@mobilia.it> 1.12.0-06
- Execute mysql_install_db using sh [SME: 1654]

* Sun Apr 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.12.0-05
- Make innodb optional, and configure it as recommended, if enabled.
  [SME: 1013]

* Tue Apr 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-04
- Add missing semi-colon to FLUSH PRIVILEGES statement [SME: 1229]

* Mon Apr 10 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-03
- Revise last patch - it backed out the db restore [SME: 1229]

* Mon Apr 10 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-02
- Move expansion of user table into set.password so it works
  for command line runs as well as db restores [SME: 1229]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.12.0-01
- Roll stable stream version. [SME: 1016]

* Mon Feb 13 2006 Charlie Brady <charlie_brady@mitel.com> 1.11.1-16
- Update dependencies to include mysql-server RPM. Remove obsolete
  dependency on e-smith-packetfilter. [SME: 737]

* Fri Jan  6 2006 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-15
- Remove explicit permission setting for /home/e-smith/db from
  genfilelist call [SME: 371]

* Sun Jan  1 2006 Charlie Brady <charlieb@e-smith.com> 1.11.1-14
- Ensure that mysql is restarted after restore, and avoid race conditions
  during mysqld restart during fix_privilege_tables. [SME: 73]
- Remove unnecessary mkdirs in build section - they're done by createlinks
  script.

* Wed Dec 14 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-13
- Call fix_privilege_tables much earlier and call mysqladmin shutdown 
  after doing so - Thanks Paul Floor [SME: 73]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-12
- Call mysql fix_privilege_tables in mysql.init [SME: 73]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.11.1-11
- Bump release number only

* Tue Nov 15 2005 Gordon Rowell <gordonr@e-smith.com>
- [1.11.1-10]
- Reset the format of the MySQL root password for old dumps [SF: 1325378]

* Wed Aug 31 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-09]
- Avoid error from db-delete action if db files are not present
  (e.g. because they have already been deleted). [SF: 1273797]

* Mon Aug 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-08]
- Fix restore of dumped tables after restore from backup.
  Reset root password after restore of dumped dbs. [SF: 1273797]

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-07]
- Ensure that 'status' property of mysql.init is honoured at
  startup. [MN00061795]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-06]
- Work around race condition between mysql startup and
  mysql.init. [SF: 1217966]

* Fri Apr 29 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-05]
- Use -f flag in mysql-delete-dumped-tables so that backup
  doesn't fail if the file is missing.

* Fri Apr 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-04]
- Change /root/.my.cnf template to use esmith::util::LdapPassword
  rather than read of ldap.pw file, to eliminate ordering
  depenendence on ldap.pw template expansion.

* Fri Apr 15 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-03]
- Restore old mysql.init behaviour, to leave any failed scripts
  behind for a later attempt, or for admin investigation. [MN00079643]

* Wed Apr 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-02]
- Fix up import of tables after a restore. Remove a few bogus
  symlinks.

* Wed Apr 13 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.1-01]
- Roll new development stream - 1.11.1

* Mon Apr 11 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-16]
- Fix typo and runtime error in run script. Detect table dump
  to be restored and set it up for mysql.init to restore it.

* Sun Apr 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-15]
- Remove trap stuff in run script (which works around mysqld brokenness)
  and add custom control/{t,q,d,i} scripts.

* Sun Apr 10 2005 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-14]
- Remove obsolete e-smith-packetfilter Requires: header.
- Do db initialisation in run script, as required, rather than via
  special action script.
- Replace all restart-, start- and reload- actions with calls to
  'adjust-services'. Update e-smith-lib version dependency. [MN00065576]
- Use generic_template_expand action where possible, in place
  of specific actions. Update e-smith-lib dependency. [MN00064130]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-13]
- Fix permissions on log/run script. Add missing /var/log/mysqld dir.
  [charlieb MN00061220]

* Wed Dec 29 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-12]
- Add missing down file in service directory.. Fix permissions
  on run script. [charlieb MN00061220]

* Tue Dec 28 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-11]
- Add missing /service/mysqld symlink [charlieb MN00061220]

* Mon Dec 20 2004 Charlie Brady <charlieb@e-smith.com>
- [1.11.0-10]
- Run mysqld under supervise. [charlieb MN00061220]
- Replace deprecated Copyright header with License. [charlieb]

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-09]
- Added restart to valid arguments to mysql.init. [msoulier 10866]

* Tue Jan  6 2004 Michael Soulier <msoulier@e-smith.com>
- [1.11.0-08]
- Fixed mysql.init leaving behind failed scripts, and the lack of proper
  initscript command-line arguments. [msoulier 10866]

* Wed Dec 24 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-07]
- Updating comments in my.cnf [tonyc 10862]
- Don't show redundant log-error option in mysqld_safe [tonyc 10862]

* Mon Dec 22 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-06]
- fixing initscript symlink [tonyc 10862]

* Mon Dec 22 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-05]
- Add /var/run/mysqld dir for mysql.com compatibility [tonyc 10862]
- Fix initscript symlink [tonyc 10862]

* Mon Dec 22 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-04]
- Add initscript symlink for mysql.com compatibility [tonyc 10862]
- Adding /etc/logrotate.d/mysqld templates [tonyc 8662]

* Thu Dec 18 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-03]
- Clean up /etc/my.cnf templates and add comments [tonyc 10862]
- Add a more --user=mysql options to actions for 100% coverage [tonyc 10862]
- Remove redundant basedir/datadir options from actions [tonyc 10862]
- Clean up mysql-preload fork/exec stuff [tonyc 10862]

* Tue Dec 16 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-02]
- Add --user=mysql to mysqld args in conf-mysql-password [tonyc 10853]
- Future-proof /etc/my.cnf for s/safe_mysqld/mysqld_safe/ change [tonyc 8662]

* Tue Dec 16 2003 Tony Clayton <apc@e-smith.com>
- [1.11.0-01]
- Changing version to development stream number - 1.11.0

* Thu Jun 26 2003 Charlie Brady <charlieb@e-smith.com>
- [1.10.0-01]
- Changing version to stable stream number - 1.10.0

* Wed Apr 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-03]
- Remove stray " in mysql-dump-tables. [charlieb 8475]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-02]
- Restrict mysql by default to use only unix domain socket. [charlieb 6430]
- Change mysql dump in pre-backup to use quotes, to fix backup/restore problem.
  [charlieb 7953]
- Remove conf-mysql-startup - use db initialisation fragments instead
  [charlieb 5665]

* Tue Apr  1 2003 Charlie Brady <charlieb@e-smith.com>
- [1.9.0-01]
- Roll development version to 1.9.0

* Mon Mar 17 2003 Lijie Deng <lijied@e-smith.com>
- [1.8.0-03]
- Deleted template-begin/end file [lijied 3295]

* Thu Jan 23 2003 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-02]
- Fix typo in mysql-restart action script (mysql => mysqld). [charlieb 4774]

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Rolling stable version number to 1.8.0

* Fri Oct 11 2002 Charlie Brady <charlieb@e-smith.com>
- [1.8.0-01]
- Rolling stable version number to 1.8.0

* Wed Sep 25 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-10]
- Reverse the recent logic change in mysql.init, now that action() function
  in /etc/rc.d/init.d/functions is repaired. Replace deprecated use
  of backticks. [charlieb 4728]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-09]
- Actually expand /etc/my.cnf template - that's what it's for! [charlieb 4731]

* Mon Sep 23 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-08]
- Fix logic problem in mysql.init [charlieb 4728]

* Tue Sep 10 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-07]
- Add fragment to my.cnf template to disable (for now) innoDB tables, and
  hence prevent log file noise. [charlieb 4731]

* Mon Sep  9 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-06]
- Update mysql-restart action and link into timezone-update event
  [charlieb 4774]

* Mon Sep  9 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-05]
- Set $HOME in mysql.init script itself, otherwise it's not set when
  run from the rc run script. Fix filenames displayed in progress message.
  [charlieb 4782]
- Remove redundant mysql.conf action script [charlieb 4782]

* Fri Sep  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-04]
- Create newly required email-update event directory. [charlieb 4782]

* Fri Sep  6 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-03]
- Change mysql-dump-tables and mysql-delete-dumps events to pre-backup and
  post-backup events. [charlieb 2745]
- Add mysql-start-if-required action, which checks if mysqld is running,
  and start it, then runs mysql.init, if not. Linked into email-update event.
  [charlieb 4782]
- Redo conf-mysql-startup using ConfigDB and remove no longer necessary
  serviceControl() calls. [charlieb 4782]
- Redo mysql-conf using esmith::templates. [charlieb 4782]
- Change mysql.init script so that it can run programs or just load sql.
  [charlieb 4782]

* Wed Aug 28 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-02]
- Create missing /etc/e-smith/sql/init directory [charlieb 4333]

* Thu Aug 22 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.4-01]
- Remove 45DenyMySQL template fragment - it's no longer needed since we
  are using connection tracking. [charlieb 4499]

* Tue Aug 20 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.3-01]
- Add rc7.d symlinks and don't set obsolete InitscriptsOrder property
  of services. [charlieb 4458]

* Wed Jul 17 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.2-01]
- Change masq script fragment to use iptables. [charlieb 1268]

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.1-01]
- Test build to verify CVS conversion

* Wed Jun 5 2002 Charlie Brady <charlieb@e-smith.com>
- [1.7.0-01]
- rollRPM: Rolled version number to 1.7.0-01. Includes patches up to 1.6.0-01.

* Tue Dec 11 2001 Jason Miller <jay@e-smith.com>
- [1.6.0-01]
- rollRPM: Rolled version number to 1.6.0-01. Includes patches up to 1.5.0-03.

* Thu Dec  6 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-03]
- Adding more verbose error messages to mysql-dump-tables.
- It should exit 0 if an error occurs, it should exit 1, and complain.

* Wed Oct 31 2001 Adrian Chung <adrianc@e-smith.com>
- [1.5.0-02]
- mysql-restart now restarts mysql if it is running, rather
  than only starting it if it is stopped.
- mysql-shutdown has been added
- conf-mysql is now mysql-initialize-db
- new template /etc/my.cnf added
- new action mysql-conf which expands /etc/my.cnf linked to
  bootstrap-console-save

* Mon Oct 29 2001 Adrian Chung <mac@e-smith.com>
- [1.5.0-01]
- Rolled version number to 1.5.0-01. Includes patches upto 1.4.0-03.
- Removed directive to remove post-restore event.

* Tue Aug 28 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.4.0-03]
- Removed deprecated post-restore event directory

* Fri Aug 17 2001 gordonr
- [1.4.0-02]
- Autorebuild by rebuildRPM

* Wed Aug 8 2001 Charlie Brady <charlieb@e-smith.com>
- [1.4.0-01]
- Rolled version number to 1.4.0-01. Includes patches upto 1.3.0-18.

* Wed Aug 08 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-18]
- force mysql.init to sort files in init directory

* Tue Aug  7 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-17]
- Fix uninitialised variable problem in masq fragment.

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-16]
- Added use esmith::util to mysql-dump-tables

* Wed Jul 04 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-15]
- Use esmith::util::LdapPassword rather than direct file read

* Tue May 29 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-14]
- fixed actions that had tied %conf when calling serviceControl (2 actions)

* Sat Apr 07 2001 Gordon Rowell <gordonr@e-smith.com>
- [1.3.0-13]
- Forward port patches from 1.2.0-05 to 1.2.0-08

* Fri Apr 06 2001 Tony Clayton <tonyc@e-smith.com>
- [1.2.0-08]
- fixed mkdir calls in mysql-delete-dumped-tables (arguments in wrong order)
 
* Thu Apr 05 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-12]
- force mysql.init to print to stderr instead of stout

* Wed Mar 23 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-11]
- fixed uninitialized value error in conf-mysql-startup

* Wed Mar 21 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-10]
- fixed error on empty glob in mysql.init

* Wed Mar 21 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-09]
- fixed harmless errors thrown by mysql.init

* Wed Mar 21 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-08]
- fixed tie bug in conf-mysql-startup script which prevented the mysqld service
  from being initialized properly.

* Thu Mar 15 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-07]
- created mysql.init initscript
- added serviceControl code for mysql.init in conf-mysql-startup

* Sat Mar 10 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-06]
- fixed mysql call in /sbin/e-smith/mysql-preload

* Sat Mar 10 2001 Tony Clayton <tonyc@e-smith.com>
- [1.3.0-05]
- fixed bugs in /sbin/e-smith/mysql-preload

* Fri Mar  9 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-04]
- added /sbin/e-smith/mysql-preload

* Sat Mar  3 2001 Charlie Brady <charlieb@e-smith.com>
- [1.2.0-07]
- add packetfilter template fragment to deny tcp/3306
  Make packet filter fragment depend on the service db. Only block
  TCP SYN packets.
- add Requires for e-smith-packetfilter.
- Add required permissions parameter to mkdir calls.

* Thu Mar  1 2001 Charlie Brady <charlieb@e-smith.com>
- [1.3.0-03]
- Make packet filter fragment depend on the service db. Only block
  TCP SYN packets.
- Add required permissions parameter to mkdir calls.

* Thu Mar  1 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-02]
- add packetfilter template fragment to deny tcp/3306
- add Requires for e-smith-packetfilter.

* Thu Mar  1 2001 Adrian Chung <adrianc@e-smith.com>
- [1.3.0-01]
- Development stream, includes all patches up to and including
  1.2.0-05.
- Ported Charlie's MySQL->mysql requires change to development
  stream.  Was 1.2.0-06, but not built.

* Fri Feb 16 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-05]
- changed -C option to useradd to a -c for comments.

* Thu Feb  8 2001 Adrian Chung <adrianc@e-smith.com>
- Rolling release number for GPG signing.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-03]
- changed conf-mysql-account to 08 instead of 05.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.2.0-02]
- remove rc0.d/rc6.d symlinks and replace with links to 
  e-smith-service instead.

* Thu Jan 25 2001 Peter Samuel <peters@e-smith.com>
- [1.2.0-01]
- Rolled version number to 1.2.0-01. Includes patches upto 1.1.0-31.

* Thu Jan 25 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-31]
- take expansion of logrotate.d/mysqld template out
  of conf-mysqld

* Wed Jan 24 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-30]
- leave logrotate.d/mysqld alone now, back out patch
- expanding /root/.my.cnf with the password alleviates
  need to pass -p to mysqladmin

* Wed Jan 24 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-29]
- expand logrotate.d/mysqld template
- add template directory for logrotate.d/mysqld

* Wed Jan 24 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-28]
- Create new mysql-conf-account script - set up mysql account and add it
  to the accounts db. Called from post-install and post-upgrade

* Wed Jan 17 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-27]
- default mysql to enabled

* Wed Jan 17 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-26]
- added mysql-delete-dumped-tables action to post-upgrade event

* Wed Jan 17 2001 Peter Samuel <peters@e-smith.com>
- [1.1.0-25]
- mysql-dump-tables and mysql-import-tables actions do nothing if mysqld
  is not running.
- mysql-dump-tables action does nothing if the dump directory does
  not exist.
- mysql-import-tables action does nothing if there is no dump file from
  which to import.
- created 2 new events - mysql-delete-dumps and mysql-dump-tables
- removed mysql-import-tables action from post-restore
- added mysql-import-tables action to post-upgrade
- created new action mysql-delete-dumped-tables
- added patch22 to list of patches to be applied - must have been
  missed in 1.1.0-24.

* Sat Jan 13 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-24]
- typo $action => restart

* Sat Jan 13 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-23]
- mysql-{import,dump}-tables checks for enabled status of mysqld
  before attempting to dump/import

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-22]
- changed "Couldn't $action mysqld" to "Couldn't restart mysqld".

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-21]
- $ in front of ENV{'PATH'}

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-20]
- add PATH setting to conf-mysql

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-19]
- get rid of --no-defaults

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-18]
- --force mysql_install_db

* Fri Jan 12 2001 Tony Clayton <tonyc@e-smith.com>
- [1.1.0-17]
- converted to using serviceControl

* Fri Jan 12 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-16]
- conf-mysql needs to run even if the service isn't enabled
  so that during runtime, it can be enabled, and just go.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-15]
- datadir check should be /var/lib/mysql/mysql.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-14]
- conf-mysql-password checks for MySQL datadir first
- mysql-{dump,import}-tables moved to
  /etc/e-smith/events/actions
- mysql-import-tables added to post-restore action

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-13]
- conf-mysql-password resets the root password, and
  gets rid of two blank account entries
- /sbin/e-smith/mysql-dump-tables has been added
  which dumps mysql.dump to /home/e-smith/db/mysql
- /sbin/e-smith/mysql-import-tables has been added
  which imports a mysql.dump text file back into a
  running system

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-12]
- conf-mysql-password now runs in console-save as well.
- if the system is started up without mysqld enabled, 
  a password won't be set, since there are no mysql tables
  initialized yet.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-11]
- conf-mysql-password runs without checking whether mysql
  is enabled.  It does not require mysqld to be started, and
  should always at least keep the root password in sync, in
  case mysqld is enabled, and started during a running system
  session.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-10]
- add mysql-conf-startup to post-install/upgrade.

* Thu Jan 11 2001 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-9]
- make conf-mysql-password set the mysql password, instead of
  setting up a once-run script.

* Wed Jan 10 2001 Charlie Brady <charlieb@e-smith.com>
- [1.1.0-8]
- Create new mysql-conf-startup script - split from mysql-conf
- Create new bootstrap-console-save event and install mysql-conf into it

* Mon Dec 18 2000 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-7]
- added configuration database to db command.(typo).

* Mon Dec 18 2000 Adrian Chung <adrianc@e-smith.com>
- [1.1.0-6]
- added UnsavedChanges wrapper around script so that it resets
  UnsavedChanges flag appropriately.

* Fri Dec 15 2000 Adrian Chung <adrianc@e-smith.com>
- Added chmod 0755 for mysqld-password init script.
- Moved /etc/etc/rc.d to /etc/rc.d

* Fri Dec 15 2000 Adrian Chung <adrianc@e-smith.com>
- Added conf-mysql-password to post-install which sets 
  up mysqld-password in rc7.d to be run once to set the 
  password.  The mysqld-password script removes it's link
  from runlevel 7 and updates the configuration/services
  database.

* Fri Nov 24 2000 Adrian Chung <adrianc@e-smith.com>
- Changed mysql to mysqld.

* Wed Nov 22 2000 Adrian Chung <adrianc@e-smith.com>
- Minor modifications to conf-mysql script to make it work
  with the RH7.0 version of mysql.

* Wed Nov 22 2000 Adrian Chung <adrianc@e-smith.com>
- Rolled to 1.1.0, for 4.1/7.0 stream.  Changed mysql to mysqld.

* Tue Nov 14 2000 Adrian Chung <adrianc@e-smith.com>
- initial release

%description
This package adds necessary startup and configuration items for
mysql.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
mkdir -p root/etc/e-smith/sql/init
perl createlinks

# add this for mysql.com rpm compatibility
mkdir -p root/var/run/mysqld

mkdir -p root/etc/rc.d/init.d/supervise
ln -s ../daemontools root/etc/rc.d/init.d/supervise/mysqld

mkdir -p root/etc/rc.d/rc7.d
ln -s /etc/rc.d/init.d/e-smith-service root/etc/rc.d/rc7.d/S50mysqld
ln -s /etc/rc.d/init.d/e-smith-service root/etc/rc.d/rc7.d/S99mysql.init

mkdir -p root/service
ln -s /var/service/mysqld root/service
touch root/var/service/mysqld/down

mkdir -p root/var/log/mysqld
mkdir -p root/home/e-smith/db/mysql


%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/run/mysqld 'attr(0755,mysql,mysql)' \
    --file /var/service/mysqld/run 'attr(0755,root,root)' \
    --file /var/service/mysqld/control/t 'attr(0750,root,root)' \
    --file /var/service/mysqld/control/d 'attr(0750,root,root)' \
    --file /var/service/mysqld/control/i 'attr(0750,root,root)' \
    --file /var/service/mysqld/control/q 'attr(0750,root,root)' \
    --file /var/service/mysqld/log/run 'attr(0755,root,root)' \
    --dir '/var/log/mysqld' 'attr(2750,smelog,smelog)' \
    --dir '/home/e-smith/db/mysql' 'attr(0750,root,root)' \
    > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%pre
%preun

%post
# mysql.com compatibility
[ -e /etc/rc.d/init.d/mysqld ] || ln -s ./mysql /etc/rc.d/init.d/mysqld

%postun
if [ $1 == 0 ]; then
  [ -l /etc/rc.d/init.d/mysqld ] && rm /etc/rc.d/init.d/mysqld
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
