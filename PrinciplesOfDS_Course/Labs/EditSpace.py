# training model of full training data with best regularization term 
clf_10 = LogisticRegression(penalty='l2', C=best_reg, solver='lbfgs')    
clf_10.fit(X_train_val_10, y_train_val_10)

y_prediction_10 = clf_10.predict(X_test_10)
acc_10 = accuracy_score(y_test_10, y_prediction_10)
f1_10 = f1_score(y_test_10, y_prediction_10)
recall_10 = recall_score(y_test_10, y_prediction_10)
precision_10 = precision_score(y_test_10, y_prediction_10)

print("Evaluation Metrics for _10 component PCA decomp + Logistic Regression:\n")
print("accuracy: {:.3f}, recall: {:.3f}, precision: {:.3f}, f1: {:.3f},".format(acc_10, recall_10, precision_10, f1_10))