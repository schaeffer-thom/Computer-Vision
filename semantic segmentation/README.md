# Semantic Segmentation and CIFAR-100 Image Classification with PyTorch

This project explores two fundamental computer vision tasks using PyTorch:
1. **Semantic Segmentation** using a pretrained Fully Convolutional Network (FCN)
2. **Image Classification** on CIFAR-100 using both a fine-tuned VGG16 and a custom CNN model

---

##  1. Semantic Segmentation

A pretrained `fcn_resnet50` model from `torchvision.models.segmentation` is used to generate semantic masks for real-world images. The pipeline includes:

- Loading and preprocessing images with `PIL` and `torchvision.transforms`
- Forward-passing images through the FCN model
- Extracting and visualizing:
  - Raw feature maps
  - Predicted segmentation masks


### Example Outputs:
- Original image
- Semantic mask prediction
- Intermediate feature map visualizations

> Model: `fcn_resnet50(pretrained=True)`  
> Dataset: Custom real-world images  
> Output: Semantic label masks

---

##  2. CIFAR-100 Image Classification

### A. Fine-Tuned VGG16 Model

- Used `torchvision.models.vgg16` pretrained on ImageNet
- Replaced the final fully-connected layer for CIFAR-100 (100 output classes)
- Only the last layer was trainable (`feature extractor frozen`)
- Trained over 10 epochs using SGD optimizer and learning rate scheduler

```python
model.classifier[6] = nn.Linear(in_features=4096, out_features=100)
