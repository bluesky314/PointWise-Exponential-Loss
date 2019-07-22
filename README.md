
# PointWise-Exponential-Loss


We introduce PointWise Exponential Loss for more accurate semantic segmentation. Consider a trained segmentation network that achives respectible IoU score. Visualising the absolute deviation map between predictions and ground truth(GT) for any sample one can observe that the largest deviations from the GT occour at the edges and within small regions of the image. We would typically expect the network to continue to optimize for these regions since they contribute largly to the loss function. However, there are minute deviations from the GT all over the map which occur at a significantly higher frequency than these larger loss regions. Upon inspection, it was observed that these smaller regions contribute almost equally to the loss. These regions of low loss causes the true signal in the gradient to be diluted leading to important regions not being optimized once the network reaches a certain level of performance. This can be combated through methods like distance maps and hinge loss but we present a more dynamic solution of dealing with noisy gradients.

From this insight we introduce PointWise Exponential Loss(P.E.L) which aims to dynamically create a weight map to largen the gap between the true signal and the noise in the gradient. It assigns a weight to each pixel depending on the magnitude of loss that pixel contributes. P.E.L is a modified version of the popular Dice Loss for semantic segmentation and is to be used on a trained model to furthur fine tune it.

The Dice Loss can be formulated as:


<a href="https://www.codecogs.com/eqnedit.php?latex=Dice=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Dice=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" title="Dice=1-\frac{\sum_{i=1}^{N} p_{0 i} g_{0 i}}{\sum_{i=1}^{N} p_{0 i} g_{0 i}+ \sum_{i=1}^{N} p_{0 i} g_{1 i}+\sum_{i=1}^{N} p_{1 i} g_{0 i}}" /></a>

where p is the prediction vector and g the ground truth


The formulation of P.E.L is as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L=1-\frac{\alpha&space;\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L=1-\frac{\alpha&space;\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" title="P.E.L=1-\frac{\alpha \sum_{i=1}^{N} p_{0 i}^n g_{0 i}}{\sum_{i=1}^{N} p_{0 i} g_{0 i}+ \sum_{i=1}^{N} p_{0 i} g_{1 i}+\sum_{i=1}^{N} p_{1 i} g_{0 i}}" /></a>

A slight change of raising the prediction map to a power has the effect of weighing each point according to the deviation of the ground truth at the point. This effectively creates a attention map per sample allowing the network to focus on regions of large loss. The hyperparamater alpha has the effect of multiplying into the learning rate to make the learning faster.

In vectorized notation this can simply be represented as:

<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L&space;=&space;1&space;-&space;\frac{\alpha&space;p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L&space;=&space;1&space;-&space;\frac{\alpha&space;p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" title="P.E.L = 1 - \frac{\alpha p^n \cdot g}{p + g}" /></a>

For segmentation tasks where we have multiple instances of the target class like nuclei segmentation, we recommend training on patches after the inital whole image training and applying P.E.L along with Cross Entropy on each patch seperately. We generally observe an increase of 1-3 dice points after P.E.L is applied in this fasion. Experimental results on specific datasets to be uploaded soon
 
