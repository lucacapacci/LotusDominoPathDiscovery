import requests
import time


# - by Luca Capacci ---------------------------------------------------------------------------------------------------------------------


starting_points = ["http://vulnerablewebsite/subpath/",
                   "https://vulnerablewebsite/subpath/",
                   "http://vulnerablewebsite/subpath2/subsubpath/"]

fail_page_contents = ["<title>ACME inc - Login Page</title>", 
                      "need authentication"]

fail_status_codes = [400, 404, 500]

sleep_time_seconds = 1

paths = ["/$Preferences.nsf?OpenPreferences&Argument",
         "/$Preferences.nsf",
         "/log.nsf",
         "/vpuserinfo.nsf",
         "/puserinfo.nsf",
         "/cpa.nsf",
         "/dirassist.nsf",
         "/doc/dspug.nsf",
         "/events4.nsf",
         "/mail.box",
         "/statmail.nsf",
         "/agentrunner.nsf",
         "/Bookmark.nsf",
         "/certsrv.nsf",
         "/cldbdir.nsf",
         "/doladmin.nsf",
         "/domadmin.nsf",
         "/domcfg.nsf",
         "/domcfg.nsf/?open",
         "/mail1.box",
         "/mail2.box",
         "/webadmin.nsf",
         "/%00",
         "/%00%20.nsf/../../lotus/domino/notes.ini",
         "/%00%c0%af.nsf/../../lotus/domino/notes.ini",
         "/%00...nsf/../../lotus/domino/notes.ini",
         "/%00.nsf.nsf/../../lotus/domino/notes.ini",
         "/%00.nsf/../../lotus/domino/notes.ini",
         "/%00.nsf/..//lotus/domino/notes.ini",
         "/%00.nsf/../lotus/domino/notes.ini",
         "/%00.nsf//../lotus/domino/notes.ini",
         "/%00/",
         "/.nsf/../notes.ini",
         "/.nsf/../winnt/win.ini",
         "/852566C90012664F",
         "/852566C90012664F/DBList?ReadForm",
         "/?Open",
         "/?OpenServer",
         "/@CGIDIRScom5.java",
         "/@CGIDIRScom5.pl",
         "/@CGIDIRSftp.pl",
         "/AgentRunner.nsf",
         "/BusyTime.nsf",
         "/Certlog.nsf",
         "/CitiPayPro.nsf",
         "/Cpa.nsf",
         "/DEASAppDesign.nsf",
         "/DEASLog.nsf",
         "/DEASLog01.nsf",
         "/DEASLog02.nsf",
         "/DEASLog03.nsf",
         "/DEASLog04.nsf",
         "/DEASLog05.nsf",
         "/DEESAdmin.nsf",
         "/Dspug.nsf",
         "/LotusTraveler.nsf",
         "/Mtatbls.nsf",
         "/OpenServer",
         "/Setup.nsf",
         "/a_domlog.nsf",
         "/account.nsf",
         "/accounts.nsf",
         "/activity.nsf",
         "/admin.nsf",
         "/admin4.nsf",
         "/admin5.nsf",
         "/alog.nsf",
         "/archive/a_domlog.nsf",
         "/archive/l_domlog.nsf",
         "/billing.nsf",
         "/bookmark.nsf",
         "/bookmarks.nsf",
         "/books.nsf",
         "/busytime.nsf",
         "/calendar.nsf",
         "/catalog.nsf",
         "/cersvr.nsf",
         "/certa.nsf",
         "/certlog.nsf",
         "/chatlog.nsf",
         "/citipaypro.nsf",
         "/clbusy.nsf",
         "/clubusy.nsf",
         "/clusta4.nsf",
         "/collect4.nsf",
         "/customerdata",
         "/customerdata.nsf",
         "/da.nsf",
         "/database.nsf",
         "/database.nsf/$DEFAULTNAV?OpenNavigator",
         "/database.nsf?OpenDatabase",
         "/db.nsf",
         "/dba4.nsf",
         "/dclf.nsf",
         "/ddm.nsf",
         "/decsadm.nsf",
         "/decsdoc.nsf",
         "/decslog.nsf",
         "/default.nsf",
         "/deslog.nsf",
         "/dircat.nsf",
         "/doc/domguide.nsf",
         "/doc/help4.nsf",
         "/doc/helpadmin.nsf",
         "/doc/helpadmn.nsf",
         "/doc/helplt4.nsf",
         "/doc/internet.nsf",
         "/doc/javapg.nsf",
         "/doc/lccon.nsf",
         "/doc/migrate.nsf",
         "/doc/npn_admn.nsf",
         "/doc/npn_rn.nsf",
         "/doc/readmec.nsf",
         "/doc/readmes.nsf",
         "/doc/smhelp.nsf",
         "/doc/srvinst.nsf",
         "/doc/sthelpad.nsf",
         "/doc/stinstall.nsf",
         "/doc/strn20.nsf",
         "/doc/wksinst.nsf",
         "/dols_help.nsf",
         "/domchange.nsf",
         "/domguide.nsf",
         "/domino.nsf",
         "/domlog.nsf",
         "/download/filesets/l_LOTUS_SCRIPT.inf",
         "/download/filesets/l_SEARCH.inf",
         "/download/filesets/n_LOTUS_SCRIPT.inf",
         "/download/filesets/n_SEARCH.inf",
         "/dspug.nsf",
         "/dspv.ntf",
         "/event.nsf",
         "/events.nsf",
         "/events5.nsf",
         "/group.nsf",
         "/groups.nsf",
         "/help/decsdoc.nsf",
         "/help/decsdoc6.nsf",
         "/help/dols_help.nsf",
         "/help/domguide.nsf",
         "/help/dspug.nsf",
         "/help/help4.nsf",
         "/help/help5_admin.nsf",
         "/help/help5_client.nsf",
         "/help/help5_designer.nsf",
         "/help/help65_admin.nsf",
         "/help/help65_client.nsf",
         "/help/help65_designer.nsf",
         "/help/help6_admin.nsf",
         "/help/help6_client.nsf",
         "/help/help6_designer.nsf",
         "/help/help7_admin.nsf",
         "/help/help7_client.nsf",
         "/help/help7_designer.nsf",
         "/help/help8_admin.nsf",
         "/help/help8_client.nsf",
         "/help/help8_designer.nsf",
         "/help/helpadmin.nsf",
         "/help/helplt4.nsf",
         "/help/internet.nsf",
         "/help/javapg.nsf",
         "/help/lccon.nsf",
         "/help/lccon6.nsf",
         "/help/lsxlc.nsf",
         "/help/lsxlc6.nsf",
         "/help/migrate.nsf",
         "/help/npn_admn.nsf",
         "/help/npn_rn.nsf",
         "/help/readme.nsf",
         "/help/readmec.nsf",
         "/help/readmes.nsf",
         "/help/smhelp.nsf",
         "/help/srvinst.nsf",
         "/help4.nsf",
         "/help5_admin.nsf",
         "/help5_client.nsf",
         "/help5_designer.nsf",
         "/helpadmin.nsf",
         "/helplt4.nsf",
         "/hidden.nsf",
         "/homepage.nsf",
         "/iNotes/Forms5.nsf",
         "/iNotes/Forms5.nsf/$DefaultNav",
         "/iNotes/Forms6.nsf",
         "/iNotes/Forms7.nsf",
         "/iNotes/Forms8.nsf",
         "/internet.nsf",
         "/ispy50.nsf",
         "/javapg.nsf",
         "/jotter.nsf",
         "/kbccv11.nsf",
         "/kbnv11.nsf",
         "/kbssvv11.nsf",
         "/l_domlog.nsf",
         "/lccon.nsf",
         "/lcon.nsf",
         "/ldap.nsf",
         "/leiadm.nsf",
         "/leilog.nsf",
         "/leivlt.nsf",
         "/lndfr.nsf",
         "/log4a.nsf",
         "/loga4.nsf",
         "/lotustraveler.nsf",
         "/lsxlc.nsf",
         "/mab.nsf",
         "/mab45.ntf",
         "/mail/aadmin.nsf",
         "/mail/admin.nsf",
         "/mail/adminisist.nsf",
         "/mail/administrator.nsf",
         "/mail10.box",
         "/mail3.box",
         "/mail4.box",
         "/mail5.box",
         "/mail6.box",
         "/mail7.box",
         "/mail8.box",
         "/mail9.box",
         "/mailadmin.nsf",
         "/mailbox.nsf",
         "/mailw46.nsf",
         "/migrate.nsf",
         "/msdwda.nsf",
         "/mtatbls.nsf",
         "/mtdata/mtstore.nsf",
         "/mtstore.nsf",
         "/names.nsf",
         "/names.nsf/$Users",
         "/nntp/nd000000.nsf",
         "/nntp/nd000001.nsf",
         "/nntp/nd000002.nsf",
         "/nntp/nd000003.nsf",
         "/nntp/nd000004.nsf",
         "/nntppost.nsf",
         "/notes.nsf",
         "/npn_admn.nsf",
         "/npn_rn.nsf",
         "/ntsync4.nsf",
         "/ntsync45.nsf",
         "/open?",
         "/perweb.nsf",
         "/private.nsf",
         "/products.nsf",
         "/proghelp/KBCCV11.NSF",
         "/proghelp/KBNV11.NSF",
         "/proghelp/KBSSV11.NSF",
         "/public.nsf",
         "/qpadmin.nsf",
         "/qstart.nsf",
         "/quickplace/quickplace/main.nsf",
         "/quickstart/qstart50.nsf",
         "/quickstart/wwsample.nsf",
         "/readme.nsf",
         "/readmec.nsf",
         "/readmes.nsf",
         "/reports.nsf",
         "/resrc7.nsf",
         "/sample/faqw46.nsf",
         "/sample/framew46.nsf",
         "/sample/pagesw46.nsf",
         "/sample/siregw46.nsf",
         "/sample/site1w46.nsf",
         "/sample/site2w46.nsf",
         "/sample/site3w46.nsf",
         "/schema.nsf",
         "/schema50.nsf",
         "/secret.nsf",
         "/secure.nsf",
         "/servlet/SchedulerTransfer",
         "/servlet/auth/admin",
         "/servlets/SchedulerTransfer",
         "/setup.nsf",
         "/setupweb.nsf",
         "/smbcfg.nsf",
         "/smconf.nsf",
         "/smency.nsf",
         "/smhelp.nsf",
         "/smmsg.nsf",
         "/smquar.nsf",
         "/smsolar.nsf",
         "/smtime.nsf",
         "/smtp.box",
         "/smtp.nsf",
         "/smtpibwq.nsf",
         "/smtpobwq.nsf",
         "/smtptbls.nsf",
         "/smvlog.nsf",
         "/software.nsf",
         "/srvinst.nsf",
         "/srvnam.htm",
         "/srvnam.nsf",
         "/stadmin.nsf",
         "/statauths.nsf",
         "/statautht.nsf",
         "/statrep.nsf",
         "/statrep.nsf/$%64efaultNav",
         "/statrep.nsf/$defaultNav?OpenNavigator",
         "/statrep.nsf?ReadEntries",
         "/stats217.nsf",
         "/stats521.nsf",
         "/stats572.nsf",
         "/stats675.nsf",
         "/stats988.nsf",
         "/stauths.nsf",
         "/stautht.nsf",
         "/stcenter.nsf",
         "/stconf.nsf",
         "/stconfig.nsf",
         "/stdnaset.nsf",
         "/stdomino.nsf",
         "/stlog.nsf",
         "/stnames.nsf",
         "/streg.nsf",
         "/stsrc.nsf",
         "/test.nsf",
         "/today.nsf",
         "/user.nsf",
         "/userreg.nsf",
         "/users.nsf",
         "/web.nsf",
         "/webuser.nsf",
         "/welcome.nsf",
         "/welcome.nsf?OpenServer",
         "/wksinst.nsf",
]


# ----------------------------------------------------------------------------------------------------------------------

results = set()

for starting_point in starting_points:
    if starting_point.endswith("/") is True:
        starting_point = starting_point[:-1]
    for path in paths:
        test_path = u'{0}{1}'.format(starting_point, path)
        print u"testing", test_path
        r = requests.get(test_path, verify=False)

        valid = True
        if r.status_code in fail_status_codes:
            valid = False
        else:
            for fail_page_content in fail_page_contents:
                if fail_page_content in r.text:
                    valid = False
                    break

        if valid is True:
            results.add(test_path)
            print "+++ valid path:", test_path
        else:
            print "--- invalid path: ", test_path

        time.sleep(sleep_time_seconds)


print "============= RESULTS ===================="
print "COUNT:", len(results)
for result in results:
    print result
