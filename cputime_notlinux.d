#!/usr/sbin/dtrace -s
#pragma D option quiet
/*this doesn't actually necessarily work yet...*/
profile:::profile-400hz /pid/ {@run[cpu]=count();}
profile:::tick-4hz {printa("%@8u ", @run); printf("\n"); clear(@run)}
