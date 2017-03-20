function [ accuracy,rms,c ] = imdb_knn(m )
[row,col]=size(m);
B = fitcknn(m(1:round(.7*row),1:col-1),m(1:round(.7*row),col));
labels=predict(B,m(round(.7*row)+1:end,1:col-1));
c=confusionmat(m(round(.7*row)+1:end,col),labels);
accuracy=trace(c)/sum(sum(c));
rms=sqrt(mean((m(round(.7*row)+1:end,col)-labels).^2));
end

