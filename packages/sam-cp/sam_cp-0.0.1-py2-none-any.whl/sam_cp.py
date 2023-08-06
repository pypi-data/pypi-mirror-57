#!/usr/bin/env
import sys
import os
import os.path
#import ifdh
try:
    import ConfigParser as configparser
except:
    import configparser
import re
import time


matchall = re.compile(".*")

class rule:
    def __init__(self, cfg, section):
         self.name = section
         for retype in ("srcre" , "dstre"):
            if cfg.has_option(section,retype):
                self.__dict__[retype] = re.compile(cfg.get(section,retype))
            else:
                self.__dict__[retype] = matchall

         for string in ("srcrepl", "dstrepl", "envset", "command","lscommand", "mkdircommand"):
	     if cfg.has_option(section,string):
		self.__dict__[string] = cfg.get(section,string) 
             else:
		self.__dict__[string] = None
 
    def __repr__(self):
         return "rule: " + self.__dict__.__repr__()

    def apply(self, srcuri, dsturi):
         envsets = None
         command = None
         lscommand = None
         mkdircommand = None
         if self.srcre.match(srcuri) and self.dstre.match(dsturi):
             if self.srcrepl:
                  srcuri = self.srcre.sub(self.srcrepl, srcuri)
             if self.dstrepl:
                  dsturi = self.dstre.sub(self.dstrepl, dsturi)
             envsets = self.envset
             command = self.command
             lscommand = self.lscommand
             mkdircommand = self.mkdircommand

         return (srcuri, dsturi, envsets, command, lscommand, mkdircommand)

class ruleset:
    def __init__(self, cfg):
        self.rules = []
        for section in cfg.sections():
            self.rules.append( rule(cfg, section) )
        
    def __repr__(self):
        return "ruleset: " + self.__dict__.__repr__()

    def error(self, msg):
        raise RuntimeError(msg)

    def apply(self, srcuri, dsturi):
        envsets = []
        command = None
        lscommand = None
        mkdircommand = None
        for rule in self.rules:
            srcuri, dsturi, renvset, rcommand, rlscommand, rmkdircommand = rule.apply(srcuri,dsturi)

            if command and rcommand:
                self.error("multiple rules give commands for (%s, %s)" % srcuri, dsturi)
            if not command and rcommand:
                command = rcommand

            if not lscommand and rlscommand:
                lscommand = rlscommand

            if not mkdircommand and rmkdircommand:
                mkdircommand = rmkdircommand

            if renvset:
                for e in renvset.split(";"):
                   envsets.append(e)

        return srcuri, dsturi, ";".join(envsets), command, lscommand, mkdircommand


class sam_cp_manager:
    """
        As roughed out, this version of sam_cp uses ifdh copy.

        It has a config file that lets you replace path components
        with regular expressions, and set ifdh flags with regular
        expressions.  So a config file like:
          -------------
          [sam_cp]
          logfile=/tmp/cplogs  # used to keep track of copies we've already done
	  log_age=3600         # how old log can get before renaming logfile.old

          [bozo_src]
          srcregexp: bozodata:/dir1
          srcrepl: srm://bozodata.fnal.gov:1234/foo/bar?SFN=/

          [bozo_dst]
          dstregexp: bozodata:/dir1
          dstrepl: srm://bozodata.fnal.gov:1234/foo/bar?SFN=/

          [bar]
          dstregexp: bozodata:/dir2
          envset: IFDH_FORCE=cpn

          [bozodata_dir3]
          dstregexp: boozodata:/dir3
          dstrepl: sam@\1
          command: scp -O 'GSSAPIDelegateCredentials No'
          --------
         would send bozodata:/dir1 to an srm copy on bozodata.fnal.gov,
         but bozodata:/dir2 would be done via cpn, while bozodata/dir3
         would be done with scp and we would put sam@ on the front of
         such paths...
    """
    def __init__(self, arglist):
        self.debug = 0
        for arg in arglist[1:]:
           if arg[0] == '-':
               del arglist[1]
               if arg[1] == 'd':
                   self.debug = 1
               elif arg[1] == 'P':
                   if self.debug: print("setting process group..."); sys.stdout.flush()
		   os.setpgrp()
               elif arg[1] == '-':
                   if self.debug: print("double dash - not looking further for flags"); sys.stdout.flush()
                   break
               else:
                   print("unsupported flag: ", arg)
           else:
               break
        self.cfg = configparser.SafeConfigParser({'debug': self.debug.__repr__(), 'log_age': '3600'})
        self.cfg.read("%s/sam_cp.cfg" % os.environ["SAM_CP_CONFIG_DIR"])
        self.debug = self.cfg.getint("sam_cp", "debug")
        self.ruleset = ruleset(self.cfg)
        self.log_age = self.cfg.getint("sam_cp", "log_age")
        if self.debug: print("got log_age of ", self.log_age); sys.stdout.flush()
        self.logfile = os.path.expanduser(os.path.expandvars(self.cfg.get("sam_cp", "logfile")))
        self.logfile_old = self.logfile + ".old"
        self.logformat = "%c %06d %s\n"
        self.pid = os.getpid()

        if self.debug: print("init: " , self.ruleset); sys.stdout.flush()
    

    def parent(self, path):
        slash = path.rfind('/')
        if slash > 9:
            path = path[0:slash]
            return path
        else:
            raise KeyError

    def make_parent_dirs(self,path,lscmd,mkdircmd):
        if lscmd == None:
            lscmd="ifdh ls"
        if mkdircmd == None:
            mkdircmd="ifdh mkdir"
        if self.debug: print("make_parent_dirs(%s) " % path); sys.stdout.flush()
        if lscmd.find("ifdh") == 0:
            suffix = " 0"
        else:
            suffix = ""

        parent = None
        try:
            parent =  self.parent(path)
            res = os.system("%s %s%s" % (lscmd, parent, suffix))
        except:
            res = 1

        if res != 0  and parent:
           self.make_parent_dirs(parent,lscmd, mkdircmd)
           res = os.system("%s %s" % (mkdircmd, parent))
    #
    # You wouldn't think recording copies by open for append/write/close
    # would neccesarily be safe, but it seems to work, in  tests
    # with 80 copies in paralell, it seems to work properly.
    # this does require some logfile maintenance, but it's quick
    # and easy.
    #
    def record_copy_start(self, path):
        self.record(self.logformat % ("s", self.pid, path))

    #
    # avoid double logfile rolls by 
    #
    def roll_log(self, count):
        if self.debug: print("roll_log: entering ..."); sys.stdout.flush()

        uniqfile = self.logfile_old + "%d"%os.getpid()
        if self.debug: print("roll_log: here1.1 ..."); sys.stdout.flush()
        lockfile = self.logfile + ".lock"
        if self.debug: print("roll_log: here1.2 ..."); sys.stdout.flush()
        have_lock = False
        if self.debug: print("roll_log: here1.3 ..."); sys.stdout.flush()

        try:
	    # dink old locks, if any
	    # rolling locks should be quick, so 2 seconds?
	    mtime = os.stat(lockfile).ST_CTIME
	    if mtime - time.time() > 2:
		print("Breaking stale lock:", lockfile)
		os.unlink(lockfile)
        except Exception as e:
            if self.debug: print("exception breaking lock:", e)

        if self.debug: print("roll_log: here1.4 ..."); sys.stdout.flush()

        try:
           # do symlink lock check
           open(uniqfile,"w").close()
           os.symlink(uniqfile,lockfile )
           if self.debug: print("roll_log: here2 ..."); sys.stdout.flush()
           # actually, symlink should raise if we don't get the lock
           # but just to be paranoid, check it.
           res = os.readlink(lockfile)
           if self.debug: print("roll_log: here3 ..."); sys.stdout.flush()
           if res != uniqfile:
               raise LogicError("did not get lock")
           have_lock=True
        except Exception as e:
           print("roll_log: Notice: Exception locking log:",  e)
           try:
               os.unlink(uniqfile)
           except:
               pass

        if self.debug: print("roll_log: here4 ..."); sys.stdout.flush()

        if not have_lock:
           if self.debug: print("roll_log: didn't get lock, not rolling log."); sys.stdout.flush()
           os.unlink(uniqfile)
           return

        try:
           if self.debug: print("roll_log: actually rolling log."); sys.stdout.flush()
           # actually roll log
           os.rename(self.logfile, self.logfile_old)
           if ( count > 0 ):
               # supposed to also toss old log
               open(self.logfile_old,"w").close()
        except Exception as e:
           print("roll_log: Exception rolling: ",  e)
           pass

        try:
           os.unlink(lockfile)
        except:
           pass

        try:
           os.unlink(uniquefile)
        except:
           pass

        print("roll_log: finishing")

    def roll_log_if_needed(self):

        # if no old file, make an empty one
        if not os.path.exists(self.logfile_old):
            open(self.logfile_old,"w").close()

        # now the old file should be when we created the current
        # one, or now
        try:
            delta = time.time() - os.stat(self.logfile_old).st_mtime
            if self.debug: print("delta is: ", delta)
            if delta > self.log_age * 2:
               if self.debug: print("clearing log..."); sys.stdout.flush()
               self.roll_log(2)
            elif delta > self.log_age:
               if self.debug: print("renaming log..."); sys.stdout.flush()
               self.roll_log(1)
        except:
            pass

    def record(self, msg):
        self.roll_log_if_needed()
        f = open(self.logfile,"a",0)
        f.write(msg)
        f.close()

    def record_copy_done(self, path):
        self.record(self.logformat % ("d", self.pid, path))
 
    def record_copy_fail(self, path):
        self.record(self.logformat % ("f", self.pid, path))
 
    def check_already_copied(self,path):

        self.roll_log_if_needed()
        if self.debug: print("entering check_already_copied(%s)..." % path); sys.stdout.flush()
        res = (None, None)
        f = None
        try:
          for fn in [self.logfile, self.logfile_old]:
            if not os.access(fn, os.R_OK):
               print("no logfile %s: " % fn)
               continue
            print("checking logfile %s: " % fn)
	    f = open(fn,"r",0)
            if self.debug: print("opened..."); sys.stdout.flush()
	    for l in f:
                if self.debug: print("check_already_copied line: '%s'" % l); sys.stdout.flush()
                try:
                    h = l[0]
                    pid = int(l[2:8])
		    l = l[9:-1]
                except:
                    print("Syntax error in log file!")
                    continue
                if self.debug: print("check_already_copied split: %s %d %s" % (h,pid, l)); sys.stdout.flush()
                if h == "s" and  l == path:
		    res = ("s", pid)  # copy was started, might have finished
                if h == "d" and  l == path:
		    res = ("d", pid)  # copy was completed, no need to keep looking
                    break
                if h == "f" and  l == path:
		    res = (None, pid) # copy failed, no need to keep looking
                    
                    break
	    f.close()
          return res
        except:
            if self.debug: print("Ouch!" , sys.exc_info()); sys.stdout.flush()
            if f: f.close()
            return res

    def exists_pid(self,pid):
        try:
            os.kill(pid, 0)
            return True
        except:
            return False

    def already_copied(self,dsturi):

        if self.debug: print("entering: already_copied"); sys.stdout.flush()

        (already,pid) = self.check_already_copied(dsturi)

        if already == "s" and not self.exists_pid(pid):
            # NFS logfile race condition?
            time.sleep(2)
	    (already, pid) = self.check_already_copied(dsturi)

        # wait for copy already in progress to complete for up to an hour(?)
        if already == "s" and self.exists_pid(pid):
            print("file %s copy in progress, waiting..." % dsturi)
	    count = 0
	    while already == "s" and count < 360 and self.exists_pid(pid):
		time.sleep(3)
		count = count + 1
		(already, pid) = self.check_already_copied(dsturi)

        if already == "s":
            print("timed out or process died waiting for in progress copy. copying anyway...")

        if already == "d":
            print("file %s already copied." % dsturi)
            return 1

        if self.debug: print("not already copied.."); sys.stdout.flush()
        return 0

    def cp(self, src, dst):
        if self.debug: print("Entering: cp %s %s " % (src, dst)); sys.stdout.flush()
        args =  []

        srcuri, dsturi, envset, cpcmd, lscmd, mkdircmd = self.ruleset.apply(src, dst)

        if self.debug: print("after rules: %s %s %s %s %s " % (cpcmd, lscmd, mkdircmd, srcuri, dsturi)); sys.stdout.flush()

        # last two arguments are source and dst
        args.append(srcuri)
        args.append(dsturi)

        if self.already_copied(dsturi):
            return 0

        self.record_copy_start(dsturi)

        envsave = {}
        if envset:
           if self.debug: print("doing envsets:"); sys.stdout.flush()
           for i in envset.split(';'):
               name, val = i.split('=',1)
               envsave[name] = os.environ.get(name,'')
               if self.debug: print("envset %s <- %s" % (name,val)); sys.stdout.flush()
               os.environ[name] = val
               if self.debug: print("after, getenv(%s) -> %s" , name, "->", os.getenv(name)); sys.stdout.flush()

        # if they overrode the cmd, call it, else have ifdh cp do it.
        if not cpcmd:
            cpcmd = "ifdh cp"

        self.make_parent_dirs(dsturi,lscmd,mkdircmd)

	fullcpcmd = cpcmd + " " + " ".join(args)
	if self.debug: print("os.system(%s)" % fullcpcmd); sys.stdout.flush()
        res = -1
        try:
	    res =  os.system(fullcpcmd)
        except:
            pass

	if 0 == res:
	    self.record_copy_done(dsturi)
        else:
            self.record_copy_fail(args[-1])

        # put environment back
        for k in list(envsave.keys()):
            os.environ[k] = envsave[k]

        return res

if __name__ == "__main__":
    scm = sam_cp_manager(sys.argv)
    res = scm.cp(sys.argv[-2], sys.argv[-1])
    print("got back %d from scm.cp" % res)
    if res == 0:
        sys.exit(res)
    else:
        sys.exit(1)
