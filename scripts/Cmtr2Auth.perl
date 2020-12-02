#!/usr/bin/perl
use lib ("$ENV{HOME}/lookup", "$ENV{HOME}/lib64/perl5", "/home/audris/lib64/perl5","$ENV{HOME}/lib/perl5", "$ENV{HOME}/lib/x86_64-linux-gnu/perl", "$ENV{HOME}/share/perl5");

use strict;
use warnings;
use Error qw(:try);

use TokyoCabinet;
use Compress::LZF;

sub toHex{
    return unpack "H*", $_[0];
}

sub fromHex{
    return pack "H*", $_[0];
}

sub extrAuthCmtr {
  my ($codeC, $str) = @_;
  my $code = safeDecomp ($codeC, $str);

  my ($auth, $cmtr, $ta, $tc) = ("","","","","","");
  my ($pre, @rest) = split(/\n\n/, $code, -1);
  for my $l (split(/\n/, $pre, -1)){
     ($auth) = ($1) if ($l =~ m/^author (.*)$/);
     ($cmtr) = ($1) if ($l =~ m/^committer (.*)$/);
  }
  ($auth, $ta) = ($1, $2) if ($auth =~ m/^(.*)\s(-?[0-9]+\s+[\+\-]*\d+)$/);
  ($cmtr, $tc) = ($1, $2) if ($cmtr =~ m/^(.*)\s(-?[0-9]+\s+[\+\-]*\d+)$/);
  ($auth, $cmtr);
}

sub safeDecomp {
  my ($codeC, $par) = @_;
  try {
    my $code = decompress ($codeC);
    return $code;
  } catch Error with {
    my $ex = shift;
    print STDERR "Error: $ex par=$par\n";
    return "";
  }
}

my %map;
my $fbase="/data/All.blobs/commit_";
my $part = $ARGV[0];

for my $s ($part, $part + 32, $part + 64, $part + 96) {
    print STDERR "reading $s\n";
    open A, "$fbase$s.idx";
    open FD, "$fbase$s.bin";
    binmode(FD);
    while (<A>) {
        chop();
        my ($nn, $of, $len, $hash) = split (/\;/, $_, -1);
        my $h = fromHex ($hash);
        my $codeC = "";
        my $rl = read (FD, $codeC, $len);
        my ($auth, $cmtr) = extrAuthCmtr ($codeC, $hash);
        print "$cmtr\;$auth\n";
    }
}
