# Validation Metrics


This section provides an explanation on the implemented metrics used for analysis of the model predictions vs ground truth and comparison of annotations to derive agreement score between two or more annotators.

The results from each problem type are explained as follows.

## Classification
Following are the validation metrics used in classification

- **Accuracy** <br>
The proportion of correct predictions out of all predictions made. It gives a general idea of how often the model is correct.<br>
<br>

- **AUC** <br>
Area Under Curve represents the ability of the model to distinguish between classes. Higher values indicate better performance. "Macro" AUC is averaged over all classes, and "Micro" AUC is calculated globally.<br>
<br>
- **F1 Score** <br>
The harmonic mean of Precision and Sensitivity (Recall). It's useful when you need a balance between Precision and Recall. For "Macro F1," it's averaged over all classes, and "Micro F1" is calculated globally.<br>
<br>
- **Precision** <br>
The ratio of correctly predicted positive observations to the total predicted positives. It's about how many of the predicted positives are actually positive. "Macro Precision" is averaged over all classes, and "Micro Precision" is calculated globally.<br>
<br>
- **Sensitivity** <br>
The ratio of correctly predicted positive observations to all the observations in the actual class. It shows how well the model captures all positives. "Macro Sensitivity" is averaged over all classes, and "Micro Sensitivity" is calculated globally.<br>
<br>
- **Specificity** <br>
The ratio of correctly predicted negative observations to all actual negatives. It indicates how well the model identifies negatives. "Macro Specificity" is averaged over all classes, and "Micro Specificity" is calculated globally.<br>
<br>
- **Matthews Correlation Coefficient (MCC)** <br>
Provides a balanced measure for binary classifications, even when classes are imbalanced. It ranges from -1 to 1, where 1 means perfect prediction, 0 means no better than random, and -1 indicates total disagreement.<br>
<br>
- **Matthews Classwise Correlation Coefficient (MCCC)** <br>
Evaluates the quality of the binary classifications, where 0.0 suggests no correlation.<br>
<br>
- **Diversity Index** <br>
Measures the diversity in the model’s predictions. Higher values suggest more diverse predictions.<br>
<br>
- **Sample / Class size** <br>
The number of samples used in the evaluation.<br>
<br>
- **Class Distributions** <br>
The distribution of classes in the validation data batch used for validation metrics.<br>
<br>
- **False Positive Rate (FPR)** <br>
The ratio of false positives out of all negatives.<br>
<br>
- **False Negative Rate (FNR)** <br>
The ratio of false negatives out of all positives. A higher FNR means more positive cases are missed.<br>
<br>
- **Class Performances** <br>
Validaiton metrics on each of the classes to understand individual class performance. <br>
<br>
- **Confusion Matrix** <br>
A confusion matrix is a table used to evaluate the performance of a classification model. It shows the number of correct and incorrect predictions made by the model compared to the actual outcomes.
  - True Positive (TP): The number of actual positives correctly predicted by the model.
  - True Negative (TN): The number of actual negatives correctly predicted by the model.
  - False Positive (FP): The number of actual negatives incorrectly predicted as positives (Type I error).
  - False Negative (FN): The number of actual positives incorrectly predicted as negatives (Type II error).
By analyzing these values, you can derive various metrics like Accuracy, Precision, Sensitivity (Recall), Specificity, and F1 Score. It gives a comprehensive understanding of how well the model is performing, especially when dealing with imbalanced datasets.<br>
<br>
- **Lift Chart** <br>
A lift chart, also known as a gains chart, is a visual tool used to measure the effectiveness of a classification model, especially in marketing and risk analysis.
Think of it like this: if you were to rank all your predictions from most confident to least confident and then group them into buckets, the lift chart would show you how much better your model is at making correct predictions compared to random guessing within those buckets.
A perfect model's lift chart would shoot straight up to 100% positive outcomes quickly. A random model would line up along a 45-degree diagonal line. The better your model, the steeper the lift in the curve compared to the diagonal.<br>
<br>
- **Meta Distributions** <br>
Distribution of classes and prediction quality as per the metadata. <br>
<br>
- **Most confused**  <br>
The most confused shows the confusion between different classes in a bar chart format.
The most confused class images contains images and their respective metrics along with the rank that are most confused.
for example
```
image_id: 'image_reference'
rank: 1
loss: 0.2
ground_truth: "class label" with 90% confidence
Prediction: "class label" with 90% confidence
```
<br>
<br>


- **Top Losses** <br>
Top losses provides a list of images with their associated metrics. Each image's data include image_id for the reference,
rank to set the order in ascending order where the lower values of rank represents higher importance, loss representing the loss
value, confidence score, ground truth label, prediction label and metadata associated to the data provided for validation.  
<br>
<br>

- **Traning - Validation comparison** <br>
The validation metrics are applied on the training dataset and validation dataset separately, and compared to Under
how model performs between training dataset and validation dataset.
<br>
<br>

- **Class Based Statistics** <br>
All the above mentioned validation metrics are applied on a class / label level and compared get more nuanced results of model predictions.
<br>
<br>



## Segmentation

The segmentation is associated to semantic segmentation at the moment. 
*Instance segmentation is work in progress.*


- **mean Intersection over Union (IoU)** <br>
Measures the overlap between the predicted segmentation and the ground truth, 1.0 indicates a perfect overlap.
<br>
<br>

- **Pixel Accuracy (pAccs)** <br>
The ratio of correctly predicted pixels to the total number of pixels. A value of 1.0 means all pixels are correctly classified.
<br>
<br>

- **Frequency weighted Intersection over union (fwIoU)** <br>
An adjusted version of IoU that takes into account the Frequency of different classes. A very small value suggests there's a problem.
<br>
<br>

- **DICE score** <br>
Similar to IoU, it measures the overlap between two samples. A score of 1.0 indicates perfect segmentation.
<br>
<br>


- **Average Perpendicular Distance (Avg. Perp. Dist)** <br>
The average distance between the predicted contour and the ground truth contour. A value of 0.0 means no distance, hence perfect prediction.
<br>
<br>

- **% of good contours** <br>
The percentage of contours that meet a certain quality threshold. 100% means all contours are good.
<br>
<br>

- **Average Hausdorff Distance (Avg. Hausdorff Dist.)** <br>
Measures the largest distance from a point in one set to the closest point in the other set. 
A value of 0.0 indicates no distance, hence perfect prediction.
<br>
<br>

- **mean Sensitivity** <br>
The ratio of true positive observations to all actual positives. A value of 1.0 means the model captures all positives.
<br>
<br>


- **mean Specificity** <br>
The ratio of true negative observations to all actual negatives. A value of 1.0 means the model captures all negatives.
<br>
<br>

- **mean AUC** <br>
Represents the ability of the model to distinguish between classes. A value of 1.0 indicates perfect distinction.
<br>
<br>

- **mean Kappa** <br>
Measures the agreement between predicted and actual classes. A value of 1.0 indicates perfect agreement.
<br>
<br>

- **Confusion Matrix** <br>
A confusion matrix is a table used to evaluate the performance of a classification model. It shows the number of correct and incorrect predictions made by the model compared to the actual outcomes.
  - True Positive (TP): The number of actual positives correctly predicted by the model.
  - True Negative (TN): The number of actual negatives correctly predicted by the model.
  - False Positive (FP): The number of actual negatives incorrectly predicted as positives (Type I error).
  - False Negative (FN): The number of actual positives incorrectly predicted as negatives (Type II error).
By analyzing these values, you can derive various metrics like Accuracy, Precision, Sensitivity (Recall), Specificity, and F1 Score. It gives a comprehensive understanding of how well the model is performing, especially when dealing with imbalanced datasets.<br>
<br>
<br>
- **Average Hausdorff Distance** <br>
Measures the largest distance from a point in one set to the closest point in the other set.
A value of 0.0 indicates no distance, hence perfect prediction.
<br>
<br>

- **Simple Hausdorff Distance** <br>
Another version of Hausdorff Distance, also indicating perfect prediction if value is 0.0
<br>
<br>

- **AUC trapezoid** <br>
AUC trapezoid is a method used to calculate the Area under the curve which is common metric in evaluating
the performance of classification models, especially in ROC Curves. This method implements the trapezoidal
rule, which is a numerical integration method. It approximates the area under curve by dividing the curve into
a series of trapezoids and then summing the areas of these trapezoids.
<br>
<br>

- **Adjusted Rand Index** <br>
Measures the similarity between two data clusterings. A value of 1 indicates perfect agreement.
<br>
<br>

- **Balanced Accuracy** <br>
The average of Sensitivity and Specificity. A value of 1.0 indicates perfect balance.
<br>
<br>


- **Volumetric Similarity** <br>
Volumetric Similarity is a metric used to evaluate the similarity between two 3D volumes, often used in medical imaging to compare the segmented regions of interests against reference volumes. 
This measures how similar the predicted volume is to the actual volume. 
<br>
<br>

- **Mean Frequency Weighted Intersection over Union (meanfwIoU)** <br>
An adjusted version of IoU that accounts for the frequency of different classes.
It's a refined metric that extends the basic IoU calculation to account for the frequency of different classes in a dataset, 
providing a balanced view of model performance, especially in datasets with class imbalances.
<br>
<br>

- **Class Based Statistics** <br>
All the above mentioned validation metrics are applied on a class / label level and compared get more nuanced results of model predictions.
<br>
<br>


## Object Detection

Following are the validation metrics used in the object detection. 

- **Mean Average Precision (mAP)** <br>
It is a measure used to evaluate the performance of an object detection model. It summarizes the precision-recall curve into a single number.
mAP gives an overall measure of the model's performance across all classes, considering both precision and recall. 
By averaging APs, it accounts for performance across classes, even if some are underrepresented.
<br>
<br>

- **mAP@10** <br>
Measures mean average precision at 10 detections per image. Higher values indicate better precision.
<br>
<br>

- **AP@10, AP@50, AP@75** <br>
Mean average precision at IoU thresholds of 10, 50 amd 75. shows accuracy at different overlap levels.
<br>
<br>

- **AP@[.50, .95]** <br>
Mean average precision across IoU thresholds from 50 to 95.
<br>
<br>

- **AR@max=1, AR@max=10, AR@max=100** <br>
Average Recall measures how well a model captures all true positives across multiple classes or detections.
It's average of recall values for each class, prodiving a single summary metric. Reflects model's ability
to deetect true positives across all classes. It helps assess performance, especially with imbalanced classes. Average recall at 1, 10, and 100 maximum detections. Higher recall means fewer misses.
<br>
<br>

- **Top Misses** <br>
Top misses provides a list of images with their associated mIOU. Each image's data include image_id for the reference,
rank to set the order in ascending order where the lower values of rank represents higher importance, and mean IOU for the bounding boxes for the 
respective class.  
<br>
<br>


- **Class Based Statistics** <br>
All the above mentioned validation metrics are applied on a class / label level and compared get more nuanced results of model predictions.
<br>
<br>

## Annotation Agreements

*TBA*
