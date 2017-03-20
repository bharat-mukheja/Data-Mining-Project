function y = recall(M)
  y = round(100*diag(M) ./ sum(M,2),1);
  y(isnan(y))=0;
end