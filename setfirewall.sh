#!/bin/bash
if test "$1" = "+36301234567" ; then
	echo "Firewall open"
	ufw allow 22/tcp
fi

