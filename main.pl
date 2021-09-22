#!/usr/bin/perl
use strict;
use warnings;

my $file= $ARGV[0] or die "No arguments given for the csv file\n";

my $sum =0;
open(my $data, '<', $file) or die "could not open file";


my $max_temp=0;
my $temp= 0;
my $hottest_card_or_device = "";
my %map = ();
my @my_array = ();

my @mainArr =(); 

while (my $line = <$data>){
	
	chomp $line;
	
	my @fields= split ";" , $line;

	my $control = $fields[0];
	if ($control eq "Device") {
		print " \n";
		# body...
	}
	else{



	if ($max_temp < $fields[2]) {
		$max_temp = $fields[2];
		$hottest_card_or_device = $fields[1]."/".$fields[0]; 
	} 
	push(@my_array, $line);
	
	#$map{$fields[0]} = \@fields;
	
	if (exists($map{$fields[0]})) {
		# it has been added before we need to modify it
		my $y= $map{$fields[0]};
		@$y[0] = @$y[0]+1;
		if ($fields[2]>=70) {
			# body...
			@$y[1] = @$y[1]+1;
		}
		if($fields[2]>@$y[2]){
			@$y[2] = $fields[2];
		}
		@$y[3] = @$y[3]+ $fields[2];


	}
	else{
		# we need to add the value to the map, if it doesnt exist in the map
		
		my @temp_arr = ();
		push(@temp_arr, 1);
		if($fields[2] >= 70){ # high temperature means it is above 70degree celcius
			push(@temp_arr, 1);
		}else{
			push(@temp_arr,0);
		}
		push(@temp_arr, $fields[2]); #max temperature 
		push(@temp_arr, $fields[2]); #avg. temp

		$map{$fields[0]}=[@temp_arr];

	}
	}
}
my $len = $#my_array+1;
my $size = keys %map;



my @outputArr = ();
my $k;
my $v;
while ( ($k,$v) = each %map ) {
#    print "$k\n";
#    print "@$v[0]\n";
    @$v[3] = @$v[3]/ @$v[0];
#    print "@$v[1]\n";
#    print "@$v[2]\n";
#    print "@$v[3]\n";
}


my @outputArray = split "\\.", $ARGV[0];
my $temporary = $outputArray[0];
my $output_file = $temporary.".html";
my $filename = $output_file;
open(my $fh, '>', $filename) or die "Could not open file '$filename' $!";

print $fh "<font size=\"+7\">Summary</font>";
print $fh "<table border=\"1\" class=\"dataframe\" style=\"border:2px solid black;\">";
print $fh "<tr><th>Total Devices</th><td>$size</td></tr><tr><th>Total Cards</th><td>$len</td></tr><tr><th>Max Card Temperature</th><td>$max_temp</td></tr><tr><th>Hottest Card/Device</th><td>$hottest_card_or_device</td></tr></table>";

print $fh "<font size=\"+5\">Devices</font><table border=\"1\" class=\"dataframe\">";
print $fh "<tr>";
print $fh "<th>";
print $fh "Device";
print $fh "</th>";
print $fh "<th>";
print $fh "Total # of cards";
print $fh "</th>";
print $fh "<th>";
print $fh "High Temperature Cards #";
print $fh "</th>";
print $fh "<th>";
print $fh "Max Temperature";
print $fh "</th>";
print $fh "<th>";
print $fh "Avg Temperature";
print $fh "</th>";
print $fh "</tr>";

while ( ($k,$v) = each %map ) {
	print $fh "<tr>";
    print $fh "<th>";
    print $fh "$k";
    print $fh "</th>";
    print $fh "<th>";
    print $fh "@$v[0]";
    print $fh "</th>";
    print $fh "<th>";
    print $fh "@$v[1]";
    print $fh "</th>";
    print $fh "<th>";
    print $fh "@$v[2]";
    print $fh "</th>";
    print $fh "<th>";
    print $fh "@$v[3]";
    print $fh "</th>";
    print $fh "</tr>";
}
print $fh "</table>";
print $fh "<h>(High Temperature >= 70)</h>";


close $fh;







