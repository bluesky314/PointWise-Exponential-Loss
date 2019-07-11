# PointWise-Exponential-Loss


Here we introduce our PointWise Exponential Loss for more accurate semantic segmentation. Consider a trained segmentation network that achives respectible IoU score. When we visualize the absolute deviation map between predictions and ground truth(GT) for any sample we observe that the largest deviations from the GT occour at the edges and within small regions of the image. We would typically expect the network to continue to optimize for these regions since they contribute largly to the loss function. However, there are minute deviations from the GT all over the map which occur at a significantly higher frequency than these larger loss regions. Upon inspection, we saw that these smaller regions contribute almost equally to the loss. These regions of low loss causes the true signal in the gradient to be diluted leading to those regions not being optimized for once the network reaches a certain level of performance. 

From this insight we introduce PointWise Exponential Loss(PEL) which aims to dynamically create a weight map to largen the gap between the true signal and the noise in the gradient. It assigns a weight to each pixel depending on the magnitude of loss that pixel contributes. PEL is a modified version of the popular Dice Loss for semantic segmentation.

The Dice Loss is formulated as:

Let $a$ be the flattened predicted vector
Let $b$ be the flattened binary ground truth mask

$ Dice Loss = 1 - \frac{a \cdot b}{a + b}

The formulation of PEL is as follows:

$ PEL = 1 - \frac{a^n \cdot b}{a + b}


