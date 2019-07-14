
# Standard Dice Loss
def dice_loss(inpu, target):  

    ip=inpu[:,0,:,:].contiguous().view(-1)
    tar=target[:,0,:,:].contiguous().view(-1)
    intersection1=(ip * tar).sum() 
    union1= ip.sum() + tar.sum()
    score1=1-2*(intersection1/union1)
    

    ip=inpu[:,1,:,:].contiguous().view(-1)
    tar=target[:,1,:,:].contiguous().view(-1)
    intersection2=(ip * tar).sum() 
    union2= ip.sum() + tar.sum()
    score2=1-2*(intersection2/union2)

    return score1,score2



# PointWise Exponential 

alpha=20
beta=3
def PEL(inpu, target):  
    ip=inpu[:,0,:,:].contiguous().view(-1)
    tar=target[:,0,:,:].contiguous().view(-1)
    intersection1= (alpha*(ip * tar).pow(beta) ).sum()
    union1= ip.sum()  + tar.sum()
    score1 = 1 - intersection1/union1
    
    ip=inpu[:,1,:,:].contiguous().view(-1)
    tar=target[:,1,:,:].contiguous().view(-1)
    intersection2=(alpha*(ip * tar).pow(beta)).sum()
    union2= ip.sum() + tar.sum()
    
    score2 = 1- intersection2/union2
    
    return score1, score2

