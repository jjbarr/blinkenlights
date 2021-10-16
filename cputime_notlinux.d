#!/usr/bin/env dtrace
#pragma D option quiet
profile:::profile-400hz /pid/ {@run[cpu]=count();}
profile:::profile-4hz {printa("%@8u ", @run); printf("\n"); clear(@run)}
