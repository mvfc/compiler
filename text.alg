start
varstart
A literal;
B integer;
D integer;
C real; 
varend;
write "Type B";
read B;
write "Type A:";
read A;
if(B>2)
then
if(B<=4)
then
write "B is between 2 and 4";
endif
endif
B<-B+1;
B<-B+2;
B<-B+3;
D<-B;
C<-5.0;
write "\nB=\n";
write D;
write "\n";
write C;
write "\n";
write A;
end$
