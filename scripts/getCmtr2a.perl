#!/usr/bin/perl
use lib ("$ENV{HOME}/lookup", "$ENV{HOME}/lib64/perl5", "/home/audris/lib64/perl5","$ENV{HOME}/lib/perl5", "$ENV{HOME}/lib/x86_64-linux-gnu/perl", "$ENV{HOME}/share/perl5");
#
use strict;
use warnings;
use Error qw(:try);
use cmt;

use TokyoCabinet;
use Compress::LZF;
my $flat="n"; 
$flat = $ARGV[0] if defined $ARGV[0];

my $fname="/data/play/DEB/cmtr2aFullS";
my (%clones);

my $split = 32;
my $offset = 0;
my $f1 = "s";
my $f2 = "cs";

sub get {
  my ($c, $s) = @_;
  return $clones{$s}{$c} if defined $clones{$s};
  if ($split > 1){
    if(!tie(%{$clones{$s}}, "TokyoCabinet::HDB", "$fname.$s.tch",
       TokyoCabinet::HDB::OREADER | TokyoCabinet::HDB::ONOLCK)){
      die "tie error for $fname.$s.tch\n";
    }
  }else{
    if(!tie(%{$clones{"0"}}, "TokyoCabinet::HDB", "$fname.tch", 
        TokyoCabinet::HDB::OREADER | TokyoCabinet::HDB::ONOLCK)){
      die "tie error for $fname.tch\n";
    }
  }
  return $clones{$s}{$c};
}

while (<STDIN>){
    chop();
    my $large = 0;
    my ($ch, @rest) = split(/;/, $_, -1);
    my $extra = "";
    $extra = join ';', @rest if $#rest >= 0;
    my $l = length($ch);
    my $c = $ch;
    my $s = sHash ($c, $split);
    my $v = get ($c, $s);
    if (!defined $v){
    my $lF = "$fname.$s.tch.large.";
    $lF .= sprintf "%.8x", sHashV ($c);
    if (-f $lF){
        $large = 1;
        my $len = -s $lF;
        open VAL, "zcat $lF|";
        <VAL>; #drop first line: it is just the key
        $v="";
        while (<VAL>){ 
            $v .= $_;
        }
    }else{
        print STDERR "no $ch in $fname\n";
        next;
    }
    }
    my $res = ";$v";
    if ($f2 =~ /cs/){
        if ($large){
        $res = ";".$v;
        }else{
        $res = ';'.safeDecomp ($v);
        }
    }      
    if ($flat eq "n"){
        if ($extra eq  ""){
            print "$ch$res\n";
        }else{ 
            print "$ch;$extra$res\n";
        }
    }else{
        $res =~ s/^;//;
        $ch .= ";$extra" if $extra ne "";
        for my $vv (split(/;/, $res, -1)){
            print "$ch;$vv\n";
        }
    }
	
  $offset++;
}
for my $s (0..($split-1)){
  untie %{$clones{$s}} if defined $clones{$s};
}