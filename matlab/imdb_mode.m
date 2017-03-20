function [ list_mode, rms, accuracy ] = imdb_mode(m)
[row,col]=size(m);
list_mode = mode(m(:,col));
rms=sqrt(mean((m(~isnan(m(:,col)))-list_mode).^2));
accuracy = (sum(m(:,col) == list_mode)/row);
end

