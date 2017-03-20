function [ accuracy,rms,c ] = imdb_dt( train_m, test_m )
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
[row,col]=size(m);
B = TreeBagger(400,m(1:round(.7*row),1:col-1),m(1:round(.7*row),col));
labels=predict(B,m(round(.7*row)+1:end,1:col-1));
labels1=str2num(cell2mat(labels));
 c=confusionmat(m(round(.7*row)+1:end,col),labels1);
accuracy=trace(c)/sum(sum(c));
rms=sqrt(mean((m(round(.7*row)+1:end,col)-labels1).^2));
end