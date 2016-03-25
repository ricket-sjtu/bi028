#!/bin/awk -f

function date2sec(date) {
	cmd="date +%s --date="date
	cmd|getline sec
	#close(cmd)
	return sec
}

BEGIN {
	print date2sec(20150120)
	print date2sec(20150123)
}

{
	t=date2sec($1)
	print $1"|"t
}
