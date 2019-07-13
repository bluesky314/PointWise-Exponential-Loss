# PointWise-Exponential-Loss


Here we introduce our PointWise Exponential Loss for more accurate semantic segmentation. Consider a trained segmentation network that achives respectible IoU score. When we visualize the absolute deviation map between predictions and ground truth(GT) for any sample we observe that the largest deviations from the GT occour at the edges and within small regions of the image. We would typically expect the network to continue to optimize for these regions since they contribute largly to the loss function. However, there are minute deviations from the GT all over the map which occur at a significantly higher frequency than these larger loss regions. Upon inspection, we saw that these smaller regions contribute almost equally to the loss. These regions of low loss causes the true signal in the gradient to be diluted leading to important regions not being optimized once the network reaches a certain level of performance. This can be combated through methods like distance maps and hinge loss but we present a more dynamic solution of dealing with noisy gradients.

From this insight we introduce PointWise Exponential Loss(PEL) which aims to dynamically create a weight map to largen the gap between the true signal and the noise in the gradient. It assigns a weight to each pixel depending on the magnitude of loss that pixel contributes. PEL is a modified version of the popular Dice Loss for semantic segmentation.

The Dice Loss can be formulated as:


<a href="https://www.codecogs.com/eqnedit.php?latex=Dice=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?Dice=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" title="Dice=1-\frac{\sum_{i=1}^{N} p_{0 i} g_{0 i}}{\sum_{i=1}^{N} p_{0 i} g_{0 i}+ \sum_{i=1}^{N} p_{0 i} g_{1 i}+\sum_{i=1}^{N} p_{1 i} g_{0 i}}" /></a>

where p is the prediction vector and g the ground truth


The formulation of P.E.L is as follows:

<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L=1-\frac{\sum_{i=1}^{N}&space;p_{0&space;i}^n&space;g_{0&space;i}}{\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{0&space;i}&plus;&space;\sum_{i=1}^{N}&space;p_{0&space;i}&space;g_{1&space;i}&plus;\sum_{i=1}^{N}&space;p_{1&space;i}&space;g_{0&space;i}}" title="P.E.L=1-\frac{\sum_{i=1}^{N} p_{0 i}^n g_{0 i}}{\sum_{i=1}^{N} p_{0 i} g_{0 i}+ \sum_{i=1}^{N} p_{0 i} g_{1 i}+\sum_{i=1}^{N} p_{1 i} g_{0 i}}" /></a>

A slight change of raising the prediction map to a power has the effect of weighing each point according to the deviation of the ground truth at the point. This effectively creates a attention map per sample allowing the network to focus on regions of large loss.

In vectorized notation this can simply be represented as:

<a href="https://www.codecogs.com/eqnedit.php?latex=P.E.L&space;=&space;1&space;-&space;\frac{p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?P.E.L&space;=&space;1&space;-&space;\frac{p^n&space;\cdot&space;g}{p&space;&plus;&space;g}" title="P.E.L = 1 - \frac{p^n \cdot g}{p + g}" /></a>
