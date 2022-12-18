# Ensemble Method
## Ensembles
This whole lesson is about how we can combine (or ensemble) the models that we have already seen in a way that makes the combination of these models better at predicting than the individual models.
Why Would We Want to Ensemble Learners Together?
There are two competing variables in finding a well-fitting machine learning model:

- Bias
- Variance.

It is common in job interviews for you to be asked about this topic and how it pertains to different modeling techniques.

### Bias: 
When a model has a high bias, this means that means it doesn't do a good job of bending to the data. An example of an algorithm that usually has a high bias is linear regression. Even with completely different datasets, we end up with the same line fit to the data. When models have high bias, this is bad.

Four diagrams showing high and low bias along with high and low variance
Variance: When a model has high variance, this means that it changes drastically to meet the needs of every point in our dataset. Linear models like the one above has low variance, but high bias. An example of an algorithm that tends to have high variance and low bias is a decision tree (especially decision trees with no early stopping parameters). A decision tree, as a high variance algorithm, will attempt to split every point into its own branch if possible. This is a trait of high variance, low bias algorithms - they are extremely flexible to fit exactly whatever data they see.

Commonly the "weak" learners you use are decision trees. In fact, the default for most ensemble methods is a decision tree in sklearn. However, this value can change to any of the models seen so far.


## Random Forest
### The problem with decision trees
Let's say we have a large table with lots and lots of columns. So, we create our Decision Tree. And we end up with answers like the following.

If a client is a male between 15 and 25 in the US, on Android, in school, likes tennis, pizza, but does not like long walks on the beach, then they're likely to download Pokemon Go.

This is not good. This almost looks like the tree just memorized the data. It's overfitting. Decision Trees tend to overfit a lot.

In the continuous case, this can also happen. The Decision Tree has many nodes which end up giving us a complicated boundary that pretty much borders every point with a small square. This is also overfitting as it doesn't generalize well to the data.

How do we solve this?

Pick some of the columns randomly from our data. Build a Decision Tree in those columns. Now, pick some other columns randomly and build a Decision Tree in those, and do it again. When we have a new data point, say this person over here, we just let all the trees make a prediction and pick the one that appears the most.

For example, these trees decided that this person will download Snapchat, WhatsApp, and WhatsApp. So, the ensemble of trees will recommend WhatsApp. Since we used a bunch of trees on randomly picked columns, this is called a random forest.

##Glossary
| Key Term |	Definition |
| ----- | ------ |
| AdaBoost |	(Ada)ptive (Boost)ing, is an ensemble ethod technique that re-assigns weights to each instance, with higher weights to incorrectly classified instances.|
| Bagging	| (B)ootstrap (agg)regating is an ensemble algorithm designed to improve the stability and accuracy of machine learning algorithms used in statistical classification and regression. It also reduces variance and helps to avoid overfitting, by sampling subsets of data.|
| Ensembles |	You can combine (or ensemble) models in a way that makes the combination of these models better at predicting than the individual models.|
| Random forest |	Using 2+ decision trees on randomly picked columns.|



## References
### Further Learning and Resources
#### Bias and Variance
this Wikipedia article on the bias-variance tradeoff discusses the central problem in supervised learning.

##### Ensemble methods in the scikit-learn library:
#### BaggingClassifier
Discusses how the Bagging classifier is used to fit base classifiers each on random subsets of the original dataset and then aggregate their individual predictions (either by voting or by averaging) to form a final prediction.
#### RandomForestClassifier
Discusses how the RandomForest classifier fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting.
#### AdaBoostClassifier
Discusses how the AdaBoost classifier fits on the original dataset and then fits additional copies of the classifier on the same dataset but where the weights of incorrectly classified instances are adjusted such that subsequent classifiers focus more on difficult cases.
Another really useful guide for ensemble methods, which can also all be extended to regression problems, can be found [in the documentation here](http://scikit-learn.org/stable/modules/ensemble.html).

#### Boosting
[The original paper](https://learn.udacity.com/nanodegrees/nd229/parts/cd0025/lessons/0cd1c220-ba5e-4cdb-8b13-ec008a63c0aa/concepts/11220722-cd60-4846-9132-9c02340b14e1#:~:text=Boosting-,The%20original%20paper,-%2D%20A%20link%20to) - A link to the original paper on boosting by Yoav Freund and Robert E. Schapire.
[An explanation about why boosting is so important](http://blog.kaggle.com/2017/01/23/a-kaggle-master-explains-gradient-boosting/) - A great article on boosting by a Kaggle master, Ben Gorman.
[A useful Quora post](https://www.quora.com/What-is-an-intuitive-explanation-of-Gradient-Boosting) - A number of useful explanations about boosting.
#### AdaBoost
Here is the original [paper](https://cseweb.ucsd.edu/~yfreund/papers/IntroToBoosting.pdf) from Freund and Schapire that is a short overview paper introducing the boosting algorithm AdaBoost, and explains the underlying theory of boosting, including an explanation of why boosting often does not suffer from overfitting as well as boosting’s the relationship to support-vector machines.
A follow-up [paper](https://cseweb.ucsd.edu/~yfreund/papers/boostingexperiments.pdf) from the same authors regarding several experiments with Adaboost.
A great [tutorial](http://rob.schapire.net/papers/explaining-adaboost.pdf) by Schapire explaining the many perspectives and analyses of AdaBoost that have been applied to explain or understand it as a learning method, with comparisons of both the strengths and weaknesses of the various approaches.