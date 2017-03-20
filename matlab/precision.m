function y = precision(M)
  y = round(diag(M)*100 ./ sum(M,1)',1);
  y(isnan(y))=0;
end