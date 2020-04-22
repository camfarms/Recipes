#! /usr/bin/awk -f
BEGIN{

	printf "Enter Search Query"
	getline query < "-"
	print query  > "tempFile"
}
