#!/usr/bin/perl
use CGI;

print <<'EOS';
Content-type: text/html; charset=utf-8

<!DOCTYPE html>
<html>
<head>
<title>A SCANDAL IN BOHEMIA</title>
</head>
<body>
<h1>A SCANDAL IN BOHEMIA</h1>
<div>
<a href="/~q26/index.pl/a_scandal_in_bohemia_1.txt">A SCANDAL IN BOHEMIA I</a>&nbsp;
<a href="/~q26/index.pl/a_scandal_in_bohemia_2.txt">A SCANDAL IN BOHEMIA II</a>&nbsp;
<a href="/~q26/index.pl/a_scandal_in_bohemia_3.txt">A SCANDAL IN BOHEMIA III</a>&nbsp;
</div>
<hr>
<div>
EOS



# Can you crack me? :P
open(F,'cracked.txt');
my $t = <F>;
chomp($t);
if ($t eq 'h@ck3d!') {
print 'FLAG_****************<br><br>';
}
unlink('cracked.txt');
####



open(F,substr($ENV{'PATH_INFO'},1));

my $cgi = new CGI;
$cgi->charset('utf-8');
while(<F>) {
chomp;
s/FLAG_\w+/FLAG_****************/g;
print $cgi->escapeHTML($_)."<br>\n";
}

print <<'EOS';
</div>
<hr>
<address>
http://www.gutenberg.org/files/1661/1661-h/1661-h.htm
</address>
</body>
</html>
EOS
