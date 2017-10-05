#!/usr/bin/perl -w
#Just a basic method to retrieve AccessToken. you could try this to see if you are able to get the token. While actually using, do not put credentials plainly.
use strict;
use HTTP::Request::Common;
require LWP::UserAgent;
my $username = '[your_username]';
my $password = "[your_password]";
my $URL = "[link]"; #url to the application you want the accessToken of.
my $consumerKey = "[consumerKey]";

my $ua = new LWP::UserAgent;
$ua->timeout(20);

my $request = HTTP::Request->new(GET => $URL);
$request->authorization_basic($username,$password);
$request->push_header("X-ConsumerKey" => $consumerKey);
print $ua->request($request)->as_string;