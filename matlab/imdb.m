matrix=importfile('Transformed.csv',1,inf)
% calculate the mode RMS
[ mode_rms, mode_accuracy ] = imdb_mode( matrix )
% calculate the decision tree accuracy and RMS
[ dt_accuracy,dt_rms,dt_confusion ] = imdb_dt( matrix )
dt_precision = precision(dt_confusion)
dt_recall = recall(dt_confusion)
% calculate the knn accuracy ant RMS
[ knn_accuracy,knn_rms,knn_confusion ] = imdb_knn( matrix )
knn_precision = precision(knn_confusion)
knn_recall = recall(knn_confusion)
% calculate the NB accuracy and RMS
[ nb_accuracy,nb_rms,nb_confusion ] = imdb_nb( matrix )
nb_precision = precision(nb_confusion)
nb_recall = recall(nb_confusion)