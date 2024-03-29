

# PointWise-Exponential-Loss

Files are yet to be uploaded along with corrections and more details. 

## Abstract 
We introduce PointWise Exponential Loss for more accurate semantic segmentation. Consider a trained segmentation network that achives respectible IoU score. Visualising the absolute deviation map between predictions and ground truth(GT) for any sample, it can be observed that the largest deviations from the GT occour at the edges and within small regions of the image. We would typically expect the network to continue to optimize for these regions since they contribute largly to the loss function. However, there are minute deviations from the GT all over the map which occur at a significantly higher frequency than these larger loss regions. These minute deviations in aggregate contribute almost equally to the loss as the areas of intrest. Thus, these regions of low loss causes the true signal in the gradient to be diluted leading to noisy and unstable gradients once the network has reached a create performace. Thus, we introduce PointWise Exponential Loss(P.E.L) which largens the gap between the true signal and noise in the gradient by making points of large loss significantly more prominent than their minute counter parts. P.E.L's action can be thought of as dynamically creating a weight map for the output mask where the weight at a point is proportional to that point's absolute deviation from the ground truth. We test our loss on multiple saturated models to find an average increase of about 1-3 points. P.E.L is a modified version of the popular Dice Loss for semantic segmentation and is to be used on a trained model to furthur fine tune it. 

## Formulation


P.E.L introduces two important hyper-paramaters to the Dice loss <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a>. <a href="https://www.codecogs.com/eqnedit.php?latex=n" target="_blank"><img src="https://latex.codecogs.com/gif.latex?n" title="n" /></a> is the power the prediction map is raised to. Since exponentiating is a transformation that largens the distance between two values in a non-linear fasion, the gap between large and smaller losses is widened allowing for larger ones to contribute more strongly to the loss. <a href="https://www.codecogs.com/eqnedit.php?latex=\alpha" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\alpha" title="\alpha" /></a> has the effect of multiplying into the learning rate to appropriate it.

Let <a href="https://www.codecogs.com/eqnedit.php?latex=p" target="_blank"><img src="https://latex.codecogs.com/gif.latex?p" title="p" /></a> and <a href="https://www.codecogs.com/eqnedit.php?latex=g" target="_blank"><img src="https://latex.codecogs.com/gif.latex?g" title="g" /></a> be the prediction and ground truth vectors respectively. Then:


<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L=1-\frac{\alpha&space;\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L=1-\frac{\alpha&space;\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" title="P.E.L=1-\frac{\alpha \sum_{i=1}^{N} p_{0 i}^n g_{0 i}}{\sum_{i=1}^{N} p_{0 i} g_{0 i}+ \sum_{i=1}^{N} p_{0 i} g_{1 i}+\sum_{i=1}^{N} p_{1 i} g_{0 i}}" /></a>

A slight change of raising the prediction map to a power has the effect of weighing each point according to the deviation of the ground truth at the point. This effectively creates a attention map per sample allowing the network to focus on regions of large loss. The hyperparamater alpha has the effect of multiplying into the learning rate to make the learning faster.

In vectorized notation this can simply be represented as:

<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L&space;=&space;1&space;-&space;\frac{\alpha&space;p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L&space;=&space;1&space;-&space;\frac{\alpha&space;p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" title="P.E.L = 1 - \frac{\alpha p^n \cdot g}{p + g}" /></a>

For segmentation tasks where we have multiple instances of the target class like nuclei segmentation, we recommend training on patches after the inital whole image training and applying P.E.L along with Cross Entropy on each patch seperately. We generally observe an increase of 1-3 dice points after P.E.L is applied in this fasion. 

## Results

Details yet to be upoaded
<!--On average we observe an increase of 1-3 points for histopathology datasets. We are currently testing on natural image datasets and results will be uploaded soon. The code for the loss is present in the repo in loss.py 
--> 
